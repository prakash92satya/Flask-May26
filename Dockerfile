FROM python:3.10.11-slim-bullseye
WORKDIR /docker

# Install the application dependencies
COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# Copy in the source code
COPY . .
#run
CMD ["python3","-m", "flask", "--app", "loan", "run", "--host", "0.0.0.0"]