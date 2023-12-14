FROM python:3
EXPOSE 5000
WORKDIR ./
COPY dependencies.txt .
RUN pip install -r dependencies.txt
COPY . .
CMD ["python3", "main.py"]