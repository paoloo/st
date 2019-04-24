FROM python:alpine3.7

ARG COMMIT
ENV COMMIT=${COMMIT}

EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

CMD ["flask", "run", "-h", "0.0.0.0"]
