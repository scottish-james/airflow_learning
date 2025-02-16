# **Airflow Learning Project**

## **Overview**
This project is designed for **learning and experimenting with Apache Airflow**, focusing on **AWS automation, Docker-based deployment, and best practices**. It provides hands-on experience in:
- **Building and debugging Airflow DAGs**
- **Managing configurations in a containerized environment**
- **Automating AWS IAM role creation**
- **Using Airflow XComs for inter-task communication**
- **Understanding connection management and Airflow Hooks**
- **Testing and troubleshooting DAGs effectively**

This setup is structured to explore **real-world data pipeline scenarios** and **infrastructure automation**, making it ideal for both **beginners and experienced developers** looking to refine their Airflow skills.

---

## **Project Structure**
```
airflow-project/
├── dags/
│   └── AWS_Setup_DAG.py       # DAG for automating AWS IAM role creation
├── config/
│   └── iac.cfg                # Configuration file for AWS and Airflow settings
├── docker-compose.yaml        # Docker setup for Airflow with PostgreSQL
└── README.md                  # Project documentation
```
📌 **Note:** The `dags/`, `config/`, and `logs/` directories must be correctly mapped in Docker for the setup to work.

---

## **Key Learning Areas**
This project demonstrates a complete Airflow-based AWS automation workflow, covering:

### **1. Airflow DAG Development**
✅ Created a **DAG** to automate AWS IAM role creation  
✅ Learned about **task dependencies** and **sequencing**  
✅ Used **Python Operators** for executing AWS tasks  
✅ Implemented **error handling and logging** for resilience  

### **2. Configuration Management**
✅ Used **ConfigParser** to manage `.cfg` files in a **Dockerized Airflow environment**  
✅ Ensured **case-sensitive key handling**  
✅ Converted config data into a **dictionary for XCom storage**  

### **3. AWS Integration with Airflow**
✅ Used **Airflow's AWS Hook** for **secure credential management**  
✅ Handled **temporary AWS credentials** (access key, secret key, session token)  
✅ Programmatically **created and managed IAM roles**  
✅ Attached **multiple policies** to IAM roles  

### **4. Dockerized Airflow Setup**
✅ Understood **Docker paths vs local paths** for file mounting  
✅ Proper **volume mapping** for `config/` and `dags/`  
✅ Used `docker-compose` for **managing Airflow services**  
✅ Cleaned up containers efficiently with `--remove-orphans`  

### **5. Airflow Core Concepts**
✅ Used **XComs** for task communication between operators  
✅ Managed **task context, dependencies, and execution flow**  
✅ Configured and listed **Airflow connections** for external services  
✅ Debugged **task execution** using logs and Airflow UI  

### **6. Best Practices in Workflow Automation**
✅ Implemented **secure credential management**  
✅ Validated **configuration files** before use  
✅ Followed **proper logging and error-handling patterns**  
✅ Used **Airflow's built-in Hooks** for better maintainability  

### **7. Debugging & Testing Airflow DAGs**
✅ Used `airflow tasks test` to run individual tasks  
✅ Analyzed logs for **task failures and AWS connectivity issues**  
✅ Troubleshot **configuration errors and invalid IAM permissions**  

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone git@github.com:scottish-james/airflow_learning.git
cd airflow_learning
```

### **2. Start the Airflow Environment**
```bash
docker-compose up -d
```
This starts:
- **PostgreSQL** (Airflow's metadata database)
- **Airflow Webserver** (UI at `http://localhost:8080`)
- **Airflow Scheduler** (task execution engine)

### **3. Initialize Airflow**
```bash
docker-compose run airflow-init
```
Creates an **admin user** for login:
- **Username:** `admin`
- **Password:** `admin`

### **4. Access Airflow UI**
- Open [http://localhost:8080](http://localhost:8080)
- Login using the credentials:
  - **Username:** `admin`
  - **Password:** `admin`

---

## **Running & Debugging DAGs**
### **Testing an Individual Task**
```bash
docker-compose run airflow-webserver airflow tasks test [dag_id] [task_id] [date]
```
Example:
```bash
docker-compose run airflow-webserver airflow tasks test aws_setup create_iam_role 2025-02-16
```

### **Checking Airflow Connections**
```bash
docker-compose run airflow-webserver airflow connections list
```

### **Cleaning Up Containers**
```bash
docker-compose down --remove-orphans
```

---

## **AWS IAM Role Setup via Airflow**
The `AWS_Setup_DAG.py` script automates **AWS IAM role creation** using Airflow, covering:
- Creating **IAM roles** with trust relationships
- Attaching **multiple policies** to roles
- Managing **existing IAM roles**
- Handling **temporary AWS session tokens**

**Pre-requisites for AWS Integration:**
1. **Ensure AWS credentials are configured** in Airflow:
   - Go to **Admin → Connections** in Airflow UI.
   - Create an **AWS connection** with:
     - `aws_access_key_id`
     - `aws_secret_access_key`
     - `aws_session_token` (if needed)

2. Modify `AWS_Setup_DAG.py` to fit your **AWS environment**.

---

## **Stopping and Restarting**
### **Stopping Services**
```bash
docker-compose down
```
### **Restarting Services**
```bash
docker-compose up -d
```
### **Resetting Everything (Deletes Data & Volumes)**
```bash
docker-compose down --volumes
```

---

## **Lessons Learned from This Project**
✅ **How to build and deploy Airflow in a containerized environment**  
✅ **How to structure DAGs with proper task dependencies**  
✅ **How to integrate AWS services with Airflow**  
✅ **How to manage Airflow configurations and credentials securely**  
✅ **How to debug and troubleshoot Airflow workflows effectively**  


