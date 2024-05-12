# FastAPI backend and Angular frontend template

This is a template for building web applications with FastAPI and Angular. The backend is built with FastAPI, PostgreSQL, SQLAlchemy, and Pydantic. The frontend is built with Angular, Angular Material, and Angular Flex-Layout. The project structure is organized in such a way that the backend and frontend are separated into their own directories for easy development and deployment. The backend is served by Uvicorn and the frontend is served by the Angular CLI development server. Both the backend and frontend can be deployed using Docker and Docker Compose.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Development](#development)
- [Deployment](#deployment)

## Project Structure

The project structure should be organized as follows:

```
src
│
└───backend
│   │   main.py
│   │   requirements.txt
│   │
│   └───app
│       │   __init__.py
│       │   db.py
│       │   models.py
│       │   routers.py
│       │   schemas.py
```

### Frontend
```
src
│
└───frontend
│   │   angular.json
│   │   package.json
│   │   tsconfig.json
│   │   ...
│   │
│   └───src
│       │   app
│       │   assets
│       │   environments
│       │   ...
```

## Features

- Backend:
  - FastAPI
  - PostgreSQL
  - SQLAlchemy
  - Alembic
  - Pydantic
  - Uvicorn
  - Docker
  - Docker Compose
- Frontend:
  - Angular
  - Angular Material
  - Angular Flex-Layout
  - Angular CLI
  - Docker
  - Docker Compose

## Requirements

- [Python](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en/download/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Development

1. Clone the repository:

    ```bash
    git clone https://github.com/lpl212757/fastapi-angular-template
    ```

2. Navigate to the project directory:

    ```bash
    cd src
    ```

3. Install the dependencies for the backend:

    ```bash
    pip install -r backend/requirements.txt
    ```

4. Install the dependencies for the frontend:

    ```bash
    cd frontend
    npm install
    ```

5. Start the backend server:

    ```bash
    uvicorn main:app --reload
    ```

6. Start the frontend development server:

    ```bash
    ng serve
    ```

7. Open your browser and visit `http://localhost:4200` to see the application.

8. Happy coding!

## Deployment

1. Build the Docker images:

    ```bash
    docker-compose build
    ```

2. Start the containers:

    ```bash
    docker-compose up -d
    ```

3. Open your browser and visit `http://localhost` to see the application.

4. Happy coding!