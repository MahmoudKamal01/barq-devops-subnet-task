FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY subnet_analyzer.py visualize.py ./

ENTRYPOINT ["sh", "-c", "python subnet_analyzer.py \"$@\" && python visualize.py", "--"]