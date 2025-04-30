# Delivery Management System

## 📌 Overview

This is a basic Delivery Management System built using Django.  
It allows assigning delivery persons to orders and tracking those assignments.

---

## ✅ Features

- 🧍 Add and manage delivery persons
- 📦 Create orders with pickup & delivery locations
- 🔁 Automatically assign available delivery persons to pending orders
- 🗂 Track assignments with timestamps
- 🔧 Admin panel to manage everything
- 📡 APIs to assign orders and list current assignments

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/delivery_management_assignment.git
cd delivery_management_assignment
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser (Admin Access)

```bash
python manage.py createsuperuser
```

### 6. Run the Server

```bash
python manage.py runserver
```

---

## 🔐 Admin Panel

- Open: `http://127.0.0.1:8000/admin`
- Manage:
  - **DeliveryPerson** (name, phone, is_available)
  - **Order** (pickup, delivery location)
  - **DeliveryAssignment** (auto-generated after assignment)

---

## 📡 API Endpoints

### 🚚 Assign Order (POST)

**URL:**
```
POST /api/assign-order/
```

**Request Body:**
```json
{
  "order_id": 1
}
```

**Success Response:**
```json
{
  "message": "Order #1 assigned to Raju Delivery"
}
```

---

### 📋 List Assignments (GET)

**URL:**
```
GET /api/assignments/
```

**Response:**
```json
[
  {
    "order_id": 1,
    "delivery_person": "Raju Delivery",
    "pickup_location": "Andheri West, Mumbai",
    "delivery_location": "Bandra East, Mumbai",
    "assigned_at": "2025-04-30 02:15:00"
  }
]
```

---

## 🛠 Technologies Used

- Python 3.10+
- Django 5.x
- SQLite (default DB)
- Postman (for testing APIs)

---

## 📝 Notes

- Orders are only assigned to **available** delivery persons.
- After assignment, delivery person becomes unavailable.
- One order can have only one assigned person.

---

## 📄 License

This project is for educational and assignment evaluation purposes only.
