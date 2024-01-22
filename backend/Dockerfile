FROM python:3
WORKDIR /app
COPY dependencies.txt /app/
RUN pip install -r dependencies.txt
COPY . .
EXPOSE 5000
CMD ["python3", "main.py"]
