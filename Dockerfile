FROM python:3.8-slim-buster

WORKDIR /app
COPY  . /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt



RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate 
RUN pip install transformers accelerate

EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]

