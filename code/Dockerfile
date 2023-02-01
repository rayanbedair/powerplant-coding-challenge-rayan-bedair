FROM python:3.8

WORKDIR /powerplant_app
COPY . /powerplant_app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["python3", "main.py"]