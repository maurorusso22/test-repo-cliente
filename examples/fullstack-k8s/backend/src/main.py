from fastapi import FastAPI

app = FastAPI(title="Fullstack K8s Example")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/hello")
def hello():
    return {"message": "Hello from backend"}
