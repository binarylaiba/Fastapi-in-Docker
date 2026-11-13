# FastAPI Docker Application

A simple web application built using **FastAPI** and containerized with **Docker**.

## About the Project

This project demonstrates how to build a REST API using FastAPI, create a Docker image, and run the application inside a Docker container.

## Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- Docker

## Project Structure

```text
Fastapi-Docker/
│
├── app/
│   └── main.py
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

## Run Locally

1. Clone the repository:

```bash
git clone https://github.com/binarylaiba/Fastapi-in-Docker.git
```

2. Navigate to the project directory:

```bash
cd Fastapi-in-Docker
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the application:

```bash
uvicorn app.main:app --reload
```

Open http://localhost:8000 in your browser.

## Run with Docker

1. Build the Docker image:

```bash
docker build -t fastapi-app .
```

2. Run the Docker container:

```bash
docker run -p 8000:8000 fastapi-app
```

3. Open the application:

http://localhost:8000

## API Documentation

FastAPI automatically generates interactive API documentation.

Open:

http://localhost:8000/docs

## Docker Hub

Docker image: `binarylaiba/fastapi-app`

## Author

**Laiba Mushtaq**

GitHub: [@binarylaiba](https://github.com/binarylaiba)
