FROM python:latest
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir flask requests\
ADD client.py ./
ENTRYPOINT ["python", "client.py"]