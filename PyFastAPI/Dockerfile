FROM python:3.14-slim
WORKDIR /app
RUN pip install --no-cache-dir fastapi uvicorn
COPY Fast_api.py .
EXPOSE 8000
CMD ["uvicorn", "Fast_api:app", "--host", "0.0.0.0", "--port", "8000"]