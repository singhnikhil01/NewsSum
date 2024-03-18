FROM python:3.8-slim-buster
WORKDIR /app
COPY  . .

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate 
RUN pip install transformers accelerate

CMD [ "python3","app.py"]

