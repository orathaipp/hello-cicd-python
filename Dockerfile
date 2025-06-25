# ใช้ Python base image
FROM python:3.10-slim

# ตั้ง working directory
WORKDIR /app

# ติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอก source code เข้า container (โฟลเดอร์ app/)
COPY app ./app

# รัน FastAPI ด้วย uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
