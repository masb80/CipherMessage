FROM python:3.5

WORKDIR /usr/src/app

COPY chypermessage_python3.py .

COPY requirements.txt .

RUN pip3 install -r requirements.txt


CMD ["python3", "./chypermessage_python3.py"] 



