import json

try:
    with open("student.json", "r") as file:
        data = json.load(file)

    print("Student Name:", data["name"])
    print("Course:", data["course"])
    print("Skills:", data["skills"])

except FileNotFoundError:
    print("JSON file not found!")

except json.JSONDecodeError:
    print("Invalid JSON format!")

except Exception as e:
    print("Something went wrong:", e)