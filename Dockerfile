FROM python:3.9

WORKDIR /usr/src/backend

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY backend/ .

CMD [ "flask", "run", "--host=0.0.0.0"]