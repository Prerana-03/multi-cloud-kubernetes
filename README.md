Adopting Multi-Cloud Strategy with Docker and Kubernetes

📌 Overview

This project demonstrates a multi-cloud deployment strategy using Docker and Kubernetes. We build a simple Flask web app, containerize it with Docker, and deploy it on AWS EKS, GCP GKE, and Azure AKS.

📂 Project Structure

multi-cloud-app/
├── app.py              # Simple Flask web app
├── Dockerfile          # Docker build file
├── deployment.yaml     # Kubernetes Deployment file
├── service.yaml        # Kubernetes Service file
└── README.md           # Project documentation

🚀 Prerequisites

Before running the project, make sure you have:

✅ Docker (Install)✅ Kubernetes (kubectl) (Install)✅ Minikube (Optional for local Kubernetes) (Install)✅ Cloud CLIs:

AWS CLI + eksctl (Install)

GCP CLI (gcloud) (Install)

Azure CLI (az) (Install)

🏗️ Step 1: Create a Flask App

Create a project folder

mkdir multi-cloud-app && cd multi-cloud-app

Create app.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Multi-Cloud with Docker and Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

🐳 Step 2: Create and Run Docker Container

Create Dockerfile

FROM python:3.9
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5000
CMD ["python", "app.py"]

Build and run Docker container

docker build -t multi-cloud-app .
docker run -d -p 5000:5000 multi-cloud-app

✅ Check: Open http://localhost:5000 in the browser.

☁️ Step 3: Push Docker Image to Docker Hub

Login to Docker Hub

docker login

Tag & Push Image

docker tag multi-cloud-app YOUR_DOCKER_USERNAME/multi-cloud-app
docker push YOUR_DOCKER_USERNAME/multi-cloud-app

☸️ Step 4: Deploy to Kubernetes

Create deployment.yaml

apiVersion: apps/v1
kind: Deployment
metadata:
  name: multi-cloud-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: multi-cloud-app
  template:
    metadata:
      labels:
        app: multi-cloud-app
    spec:
      containers:
      - name: multi-cloud-app
        image: YOUR_DOCKER_USERNAME/multi-cloud-app
        ports:
        - containerPort: 5000

Create service.yaml

apiVersion: v1
kind: Service
metadata:
  name: multi-cloud-service
spec:
  selector:
    app: multi-cloud-app
  ports:
    - protocol: TCP
      port: 80
      targetPort: 5000
  type: LoadBalancer

Apply to Kubernetes

kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get svc

🌍 Step 5: Deploy on Multi-Cloud

1️⃣ Deploy on AWS EKS

eksctl create cluster --name multi-cloud-cluster --region us-east-1
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get svc

2️⃣ Deploy on GCP GKE

gcloud container clusters create multi-cloud-cluster --zone us-central1-a
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get svc

3️⃣ Deploy on Azure AKS

az aks create --resource-group myResourceGroup --name myAKSCluster --node-count 2
az aks get-credentials --resource-group myResourceGroup --name myAKSCluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get svc

✅ Final Steps

Check running pods: kubectl get pods

View logs: kubectl logs POD_NAME

Access the app: kubectl get svc → Copy LoadBalancer IP

🎯 Next Steps

🔹 Add CI/CD with GitHub Actions🔹 Implement Multi-Cloud Networking🔹 Set up Monitoring (Prometheus + Grafana)
