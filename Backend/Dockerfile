FROM python:3.9

RUN apt update -y

ADD requirements.txt /backend/

RUN pip install -r /backend/requirements.txt

ADD ./ /backend/

WORKDIR /backend


ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

