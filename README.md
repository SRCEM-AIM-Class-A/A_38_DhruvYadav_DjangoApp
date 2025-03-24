
### **StudentProject - Multi-App Django Application with Docker & Jenkins**  

#### **📌 Project Overview**  
This is a simple **multi-app Django project** named `StudentProject`, designed for containerization with **Docker** and automated deployment using **Jenkins**.  

It includes:  
✅ Multiple Django apps (`app1` and `app2`)  
✅ Static views and templates (no database)  
✅ Dockerfile for containerization  
✅ Jenkinsfile for CI/CD automation  
✅ Docker Hub image hosting  

## **📂 Project Structure**  
```
StudentProject/
│── app1/
│   ├── templates/
│   │   ├── home.html
│   ├── views.py
│   ├── urls.py
│── app2/
│   ├── templates/
│   │   ├── page.html
│   ├── views.py
│   ├── urls.py
│── StudentProject/
│   ├── settings.py
│   ├── urls.py
│── templates/   # Global templates directory
│   ├── base.html
│── Dockerfile
│── Jenkinsfile
│── requirements.txt
│── README.md
```


## **🚀 How to Run the Project Locally**  
### **1️⃣ Clone the Repository**  
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/StudentProject.git
cd StudentProject
```

### **2️⃣ Install Dependencies**  
Make sure you have **Python** and **pip** installed. Then, install dependencies:  
```sh
pip install -r requirements.txt
```

### **3️⃣ Run the Django Development Server**  
```sh
python manage.py runserver
```
Now, visit **http://127.0.0.1:8000/** in your browser.

---

## **🐳 Run the Project with Docker**  
### **1️⃣ Build the Docker Image**  
```sh
docker build -t studentproject .
```

### **2️⃣ Run the Container**  
```sh
docker run -p 8000:8000 studentproject
```
Now, visit **http://localhost:8000/**.

---

## **🤖 Jenkins CI/CD Pipeline**  
This project includes a **Jenkinsfile** for automation. The pipeline:  
1️⃣ Pulls the latest code from GitHub  
2️⃣ Builds a Docker image  
3️⃣ Pushes it to Docker Hub  

---

## **📦 Deploying to Docker Hub**  
### **1️⃣ Log in to Docker Hub**  
```sh
docker login
```
### **2️⃣ Tag and Push the Image**  
```sh
docker tag studentproject dhruv1974/studentproject:latest
docker push dhruv1974/studentproject:latest
```
Find your image at:  
🔗 [Docker Hub - dhruv1974/studentproject](https://hub.docker.com/r/dhruv1974/studentproject)  

---
