FROM python:latest

COPY ./ ./ 

CMD ["python3", "src/add.py"]
