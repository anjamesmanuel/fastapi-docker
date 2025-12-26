from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI CI/CD with Docker and GitHub Actions"}

@app.get("/health")
def health():
    return {"status": "healthy"}