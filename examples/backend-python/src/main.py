from fastapi import FastAPI

app = FastAPI(title="Backend Python Example")


@app.get("/health")
def health_check():
    return {"status": "ok"}
