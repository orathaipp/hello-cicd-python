FROM python:3.10-slim

WORKDIR /app

# Copy requirements.txt จาก root repo เข้าไปใน /app
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy source code ใน /app เข้า container
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
