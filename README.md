# Django Blog

This repository contains the source code for creating a blog using Django. Follow the instructions below to quickly set up the blog on your computer using Docker.

## Installation

Before getting started, make sure you have the following tools installed:

- [Docker](https://www.docker.com/get-started)

## Running the Blog

1. Clone the repository to your computer:

    ```bash
    git clone https://github.com/Flayzex/first_blog.git
    ```

2. Navigate to the project folder:

    ```bash
    cd first_blog/blog
    ```

3. Run Docker Compose to build and start the containers:

    ```bash
    docker-compose up
    ```

    This command will create and launch Django and PostgreSQL containers. Ensure that port 8000 on your computer is available.

4. Open your web browser and go to:

    ```
    http://localhost:8000/
    ```

    You should now see the running blog.

## Stopping the Blog

To stop the blog, execute the following command in the terminal:

```bash
docker-compose down