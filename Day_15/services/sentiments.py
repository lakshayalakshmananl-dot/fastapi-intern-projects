from transformers import pipeline
import asyncio

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

def analyze_sentiment(text: str):
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "score": round(result["score"], 4)
    }

async def analyze_sentiment_async(text: str):
    loop = asyncio.get_running_loop()

    return await loop.run_in_executor(
        None,
        lambda: analyze_sentiment(text)
    )