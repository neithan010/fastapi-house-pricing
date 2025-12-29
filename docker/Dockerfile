FROM python:3.11-slim

WORKDIR /app

# Como el contexto será la raíz, encontrará requirements.txt sin problemas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo lo de la raíz (main.py, routers, etc.)
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]