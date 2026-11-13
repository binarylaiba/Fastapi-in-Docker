from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello! My FastAPI app is working."
    }

@app.get("/about")
def about():
    return {
        "app": "FastAPI Docker App",
        "status": "Running"
    }