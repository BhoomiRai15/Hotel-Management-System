# 🏨 Hotel Management System (Tkinter + MySQL)

A GUI-based hotel management system developed in **Python** using **Tkinter** for the front-end and **MySQL** for the backend. It allows hotel staff to manage customer data, room bookings, room details, and view reports—all in a user-friendly interface.

---

## 📂 Project Modules Overview

| File Name      | Description                                      |
|----------------|--------------------------------------------------|
| `login.py`     | Login window for secure access                   |
| `hotel.py`     | Main dashboard that connects all modules         |
| `room.py`      | Room booking system with billing and meal plans |
| `customer.py`  | Add, update, delete, and search customer details |
| `details.py`   | Room details management (floor, room no, type)   |
| `report.py`    | Static hotel services and information report     |

---

## 🧰 Technologies Used

- **Python 3.x**
- **Tkinter** (GUI)
- **MySQL**
- **Pillow** (Image support)
- **Visual Studio** or **VS Code**

---

## 🛠 Setup Instructions

### 📁 Folder Structure

```
HotelManagementSystem/
│
├── login.py
├── hotel.py
├── room.py
├── customer.py
├── details.py
├── report.py
├── README.md
│
└── images/
    ├── logohotel.png
    ├── LoginIconAppl.png
    └── SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg
```

---

### 📦 Required Libraries

Install dependencies:

```bash
pip install mysql-connector-python Pillow
```

---

### 🛢 MySQL Database Setup

Run these SQL commands to set up the required tables:

```sql
CREATE DATABASE IF NOT EXISTS management;
USE management;

CREATE TABLE IF NOT EXISTS customer (
    Ref VARCHAR(20) PRIMARY KEY,
    Name VARCHAR(100),
    Mother VARCHAR(100),
    Gender VARCHAR(10),
    PostCode VARCHAR(20),
    Mobile VARCHAR(20),
    Email VARCHAR(100),
    Nationality VARCHAR(50),
    Idproof VARCHAR(50),
    Idnumber VARCHAR(50),
    Address VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS details (
    Floor VARCHAR(10),
    RoomNo VARCHAR(10) PRIMARY KEY,
    RoomType VARCHAR(50)
);
```

Ensure MySQL is running and accessible at `localhost` with:

- Username: `root`
- Password: `Bhoomikaraijyothi1503` *(change if needed)*

---

## ▶️ How to Run in Visual Studio / VS Code

1. Open the project folder in **Visual Studio** or **VS Code**.
2. Right-click `login.py` and choose **Set as Startup File** (in Visual Studio).
3. Run the project with `Ctrl + F5` or the **Run** button.
4. Use the login credentials to access the system.

---

### 🔐 Login Credentials

| Username | Password |
|----------|----------|
| `User`   | `abcd`   |

---

## ✨ Features

- 🔐 Secure Login System  
- 📋 Customer Management (CRUD operations)  
- 🛏 Room Booking with Meal Plan & Bill  
- 🏠 Room Details Entry (Floor, Room No, Type)  
- 📊 Report View of Hotel Services  
- 🔍 Search & Filter Capabilities  
- 💾 MySQL Data Persistence  
- 🖼 Image Integration with Pillow  
- 📑 Treeview Tables for Data Display  

---

## 📜 Module Descriptions

### `login.py`
- Handles secure login with basic username/password check.
- Redirects to hotel dashboard on success.

### `hotel.py`
- Main dashboard window, allows access to other modules.

### `customer.py`
- Add new customers, view existing ones.
- Update/delete customer details.
- Search by mobile or reference number.

### `room.py`
- Assign rooms to customers.
- Input room type, meal plan, calculate bill.
- Simple tax and total computation included.

### `details.py`
- Add new room details like room number, floor, and type.
- View and delete existing room records.

### `report.py`
- Static text-based info window showing hotel description.
- Displays list of services and facility timings.

---

## 🖼 Image Requirements

Make sure the following images are present in the `/images` folder:

| File Name                                      | Purpose         |
|-----------------------------------------------|-----------------|
| `logohotel.png`                                | App logo        |
| `LoginIconAppl.png`                            | Login icon      |
| `SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg` | Login background |

---

## 🧪 Sample Bill Calculation Logic (room.py)

- Room Type: Deluxe / Single / Double
- Meal Plan: Breakfast / Lunch / Dinner
- Number of Days: `checkout - checkin`
- Tax: 9% GST applied
- Final bill: `room_price + meal_price + tax`

---

## ⚠️ Notes

- Always ensure MySQL server is running before launching the app.
- If you get database connection errors, update:
  ```python
  mysql.connector.connect(
      host="localhost",
      username="root",
      password="YOUR_PASSWORD",
      database="management"
  )
  ```

- This app does not use hashed passwords. Consider adding secure authentication for real deployments.

---

## 🔮 Future Improvements

- Export bill as PDF  
- Room availability calendar  
- Admin login system  
- Input validation & error logs  
- Night mode UI  
- REST API connection

---

