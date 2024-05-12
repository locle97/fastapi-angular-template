# FastAPI backend and Angular frontend template

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