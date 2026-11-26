from fastapi import FastAPI

app=FastAPI(title="Student API")

@app.get("/")
def Home():
    return {
        "message":"Welcome to Student API"
    }