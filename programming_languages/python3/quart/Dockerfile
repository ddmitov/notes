FROM python:3.9-slim

RUN pip install --no-cache \
    hypercorn \
    quart

CMD ["python"]

# docker build -t quart .

# docker run --rm -it -p 8000:8000 -v $PWD:/app quart python /app/quart_server.py
# docker run --rm -it -p 8000:8000 -v $PWD:/app quart hypercorn --bind '0.0.0.0:8000' /app/quart_server:app

# http://localhost:8000/

# Cache cleaning:
# docker run --rm -it -p 8000:8000 -v $PWD:/app quart bash
#   rm -rf /app/__pycache__
