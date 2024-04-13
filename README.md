# House Rent Prediction

This repository contains code for a House Rent Prediction web application.

## Steps to Run the Application

### Step 1: Install Docker
Download and install Docker Desktop for your operating system from the [official Docker website](https://www.docker.com/products/docker-desktop).

### Step 2: Clone the Repository
Clone the House Rent Prediction repository to your local machine:
```bash
git clone https://github.com/Anubhav-Goyal01/House-Rent-Prediction.git

### Step 3: Navigate to the Project Directory
Navigate to the directory of the cloned House Rent Prediction repository:
```bash
cd House-Rent-Prediction

###Step 4: Build Docker Image
Build the Docker image using the provided Dockerfile:
```bash
docker build -t house-rent-prediction .

###Step 5: Run Docker Container
Run the Docker container from the built image:
```bash
docker run -p 5000:5000 house-rent-prediction

###Open a web browser and navigate to http://localhost:5000 to access the House Rent Prediction web app.

