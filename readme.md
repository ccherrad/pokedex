# Pokedex Application
## Description

The Pokedex Application is a web-based Pokedex that provides detailed information about various Pokemon species. It allows users to browse and search for Pokemon, view their stats, abilities, and more. This application is built using Nuxt.js for the frontend and Django for the backend.

## Getting Started

To run the Pokedex Application on your local machine, you'll need the following prerequisites:

- **Docker**: Ensure you have Docker installed on your system. You can download and install Docker from [the official Docker website](https://www.docker.com/get-started).

- **Docker Compose**: Docker Compose is used to manage multi-container Docker applications. It should be included with your Docker installation.

- **Internet Connection**: The application relies on downloading Docker images and assets from the internet, so you'll need an active internet connection.

Follow these steps to start the application:

1. **Clone the Repository**: Open your terminal and clone the Pokedex Application repository from GitHub:

   ```bash
   git clone https://github.com/ccheerad/pokedex.git

2. **Build Docker Containers**: Navigate to the project directory and use Docker Compose to build the Docker containers for the application:
    ```bash
    cd pokedex
    docker-compose build

3. **Start the Containers**: Once the containers are built, start the application by running:
    ```bash
    docker-compose up

4. **Run Migrations**: To set up the database, execute the following command to run the Django migrations:
    ```bash
    docker-compose exec api python manage.py migrate

5. **Access the Application**: You can now access the Pokedex Application in your web browser by navigating to:

http://localhost:3000/

This will take you to the Pokedex web interface, where you can start exploring the world of Pokemon.

Enjoy using the Pokedex Application to discover information about your favorite Pokemon!
