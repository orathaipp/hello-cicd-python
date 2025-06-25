from fastapi.testclient import TestClient
from app.main import app  # ชี้ไปยัง main.py ที่อยู่ใน app/

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
    assert "pod_name" in response.json()

def test_test():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"message": "Test, Hello World!"}

def test_plus2():
    response = client.get("/plus2/3")
    assert response.status_code == 200
    assert response.json() == {"message": 5}

def test_christmas():
    response = client.get("/chistmas")
    assert response.status_code == 200
    assert response.json() == {"message": "mary ChrismastX"}

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}
