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

@app.get("/test")
def test():
    return {"message": "Test, Hello World!"} 

@app.get("/plus2/{x}")
def test(x: int):
    return {"message": x + 2}

@app.get("/chistmas")
def test():
    return {"message": "mary ChrismastX"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/status")
def status():
    return {"status": "ok", "message": "Service is running smoothly!"}

@app.get("/add/{x}/{y}")
def add(x: int, y: int):
    """
    Add two numbers and return the result.
    """
    result = x + y
    return {"result": result}

@app.get("/santa")
def test():
    return {"message": "if santa, you got gift"}

@app.get("/fact/{x}")
def test(x: int):
    res = x
    for i in x:
        res = res*x
    return {"message": f"is value {x} correct?"}
