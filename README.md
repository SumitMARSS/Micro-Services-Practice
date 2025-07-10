# 🧩 Microservice Example with Docker & Kubernetes

This project demonstrates how to build, containerize, and deploy a simple microservice architecture using **Docker**, **Docker Compose**, and **Kubernetes (Minikube)** with visual dashboards and metrics.

------------------------------------------------------------------------

## 🚀 Project Structure

    MicroService-Example/
    ├── docker-compose.yml
    ├── user-service/
    │ ├── Dockerfile
    │ └── app.js / main.py
    ├── product-service/
    │ ├── Dockerfile
    │ └── app.js / main.py
    ├── k8s/
    │ ├── user-deployment.yaml
    │ ├── product-deployment.yaml
    │ └── service.yaml


------------------------------------------------------------------------

## 🔧 1. Docker Setup & Verification

### ✅ Install Docker
    sudo apt update
    sudo apt install docker.io

### ✅ Verify Docker Installation
    sudo docker version
    sudo docker run hello-world
### ✅ Allow Docker Without Sudo
    sudo usermod -aG docker $USER
    newgrp docker


----------------------------------------------------------------------------

##  📦 2. Docker Basics

### 🔹 Docker Image
        A Docker image is a packaged snapshot of your application and environment.

### 🔹 Docker Container
        A container is a running instance of an image.

### ✅ Build Docker Images
    docker build -t user-service ./user-service
    docker build -t product-service ./product-service
### ✅ List Docker Images
    docker images
### ✅ Run a Container
    docker run -p 3000:3000 user-service

----------------------------------------------------------------------------

##  🔄 3. Docker Compose (Multi-Service)

### ✅ Start All Services
    docker compose up --build

----------------------------------------------------------------------------

##  ☸️ 4. Kubernetes with Minikube

### ✅ Start Minikube
    minikube start
### ✅ View Dashboard
    minikube dashboard

----------------------------------------------------------------------------

##  🧠 5. Kubernetes Concepts

### Term	        Description
    Pod	          The smallest deployable unit. Wraps one or more containers.
    Deployment	  Manages stateless replicas of pods (e.g., APIs).
    StatefulSet	  For stateful pods like DBs. Ensures stable identity and storage.
    Service	      A stable endpoint to expose a set of pods.
    ReplicaSet	  Ensures a specified number of pod replicas are running at all times.
    DaemonSet	    Runs one pod per node, usually for log collectors, metrics agents, etc.

----------------------------------------------------------------------------

##  📦 6. Deploying with kubectl

### ✅ Apply K8s Manifests
    kubectl apply -f k8s/user-deployment.yaml
    kubectl apply -f k8s/product-deployment.yaml
    kubectl apply -f k8s/service.yaml
    
### ✅ Check Resources
    kubectl get pods
    kubectl get services
    kubectl logs <pod-name>

----------------------------------------------------------------------------

##  🌐 7. Expose Services

### ✅ Access Services in Browser
    minikube service user-service
    minikube service product-service
    
----------------------------------------------------------------------------
    
##  📊 8. Enable Metrics Server

### ✅ Enable & View Resource Usage
    minikube addons enable metrics-server
    kubectl top pods

----------------------------------------------------------------------------


##  🧪 9. Debugging Tips
    Check Pod Details - kubectl describe pod <pod-name>
    Check Pending State
      Look for:
        Missing storage (PVC)
        Insufficient memory
        Image pull errors

        
----------------------------------------------------------------------------

##  📁 10 .gitignore (Recommended)
        gitignore

        **/node_modules/
        **/__pycache__/
        *.env
        *.log
        .DS_Store
        .vscode/
        .idea/
        volumes/

----------------------------------------------------------------------------


## ✅ Summary of Tools

  ## Tool	          Purpose
    Docker	        Containerize individual services
    Docker          Compose	Manage multiple containers locally
    Minikube	      Run Kubernetes cluster locally
    kubectl	        CLI to manage Kubernetes
    K8s Dashboard	  View deployments, pods, services visually
    Metrics Server	Monitor CPU & memory usage

----------------------------------------------------------------------------

