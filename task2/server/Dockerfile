FROM python:latest
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir flask requests
ADD server.py ./
ENTRYPOINT ["python", "server.py"]