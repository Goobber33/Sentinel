from fastapi import FastAPI

app = FastAPI(
    title="Sentinel API",
    description="Security monitoring and threat detection platform",
    version="0.1.0",
)


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "sentinel-api",
    }
