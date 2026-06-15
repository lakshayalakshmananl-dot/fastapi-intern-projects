from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from models import Task, User
from schemas import TaskCreate, TaskResponse, TaskUpdate
from security_dependencies import get_current_user
from services.sentiments import analyze_sentiment_async

router = APIRouter()
@router.get("/ping")
async def ping():
    return {"msg": "router working"}


# Create Task
@router.post("/tasks", response_model=TaskResponse)
async def create_task(
    task: TaskCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title=task.title,
        description=task.description,
        user_id=current_user.id
    )

    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)

    return new_task


# Get All Tasks
@router.get("/tasks", response_model=list[TaskResponse])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    return result.scalars().all()


# Get Task By ID
@router.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task


# Update Task
@router.put("/tasks/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed

    await db.commit()
    await db.refresh(task)

    return task


# Delete Task
@router.delete("/tasks/{task_id}")
async def delete_task(
    task_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Task).where(Task.id == task_id))
    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    await db.delete(task)
    await db.commit()

    return {"message": "Task deleted successfully"}


# Get Tasks for User
@router.get("/users/{user_id}/tasks")
async def get_user_tasks(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Task).where(Task.user_id == user_id))
    return result.scalars().all()


# Sentiment Analysis Endpoint 
# Sentiment Analysis Endpoint
@router.post("/tasks/{task_id}/sentiment")
async def task_sentiment(
    task_id: int,
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(
        select(Task).where(Task.id == task_id)
    )

    task = result.scalar_one_or_none()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    text = f"{task.title} {task.description or ''}"

    sentiment = await analyze_sentiment_async(text)

    return sentiment