from fastapi import FastAPI


app = FastAPI(
    title="STT Service",
    description="Speech-to-text inference API for the voice pipeline",
    version="0.1.0",
)

@app.get("/health")
def health():
    return {"status": "ok", "message": "STT service is running"}