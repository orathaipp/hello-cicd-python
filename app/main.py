from fastapi import FastAPI
import os
import logging

app = FastAPI()

# ตั้งค่า logging
logging.basicConfig(level=logging.INFO)

@app.get("/")
def hello():
    pod_name = os.environ.get("HOSTNAME", "unknown")
    logging.info(f"Responding from pod: {pod_name}")
    return {"message": "Hello CI/CD V2 🚀", "pod_name": pod_name}