from fastapi import FastAPI

app = FastAPI(title="Config Service")


@app.get("/health")
def health():
    return {"status": "ok"}



@app.get("/version")
def version():
    return {"service": "config-service", "version": "0.1.0"}
