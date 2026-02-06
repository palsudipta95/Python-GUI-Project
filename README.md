# 🎓 Student Record Management System (Python GUI)

A **desktop-based Student Record Management System** built using **Python**, **Tkinter**, and **MySQL**, developed as part of my **Software Development–I** course.  
This project demonstrates **Object-Oriented Programming (OOP)** concepts and full **CRUD operations** through an interactive graphical user interface.

---

## 📌 Project Overview

The **Student Record Management System** is designed to manage student information efficiently using a clean and user-friendly GUI.  
It allows users to **add, view, search, update, and delete** student records stored in a MySQL database.

This project helped me gain hands-on experience with:
- Python GUI development
- Object-Oriented Programming
- Database connectivity
- SQL-based CRUD operations

---

## 🚀 Features

✔ Add new student records  
✔ View all registered students in a tabular format  
✔ Search students by **ID, Name, or Course**  
✔ Update student details (Name, Department, Course, Grade)  
✔ Delete student records  
✔ Scrollable table view using `ttk.Treeview`  
✔ User-friendly interface with validations and alerts  

---

## 🛠️ Technologies Used

- **Programming Language:** Python  
- **GUI Framework:** Tkinter & ttk  
- **Database:** MySQL  
- **Database Connector:** PyMySQL  
- **Concepts Applied:**
  - Object-Oriented Programming (OOP)
  - CRUD Operations
  - Event-driven programming
  - SQL Queries

---

## 🧠 Learning Outcomes

Through this project, I learned and applied:

- Designing GUI applications using **Tkinter**
- Structuring applications using **classes and methods**
- Connecting Python applications with **MySQL databases**
- Implementing **Create, Read, Update, Delete (CRUD)** functionality
- Handling user inputs and error validation
- Displaying data dynamically in a GUI table

---

## 🖥️ Application Modules

| Module | Description |
|------|------------|
| Add Student | Registers a new student into the database |
| Search Student | Searches records using ID, name, or course |
| Update Record | Modifies existing student details |
| Show All | Displays all registered students |
| Delete Student | Removes a student record permanently |

---

## 🗄️ Database Structure

**Database Name:** `record`  
**Table Name:** `student`

```sql
CREATE TABLE student (
    std_id INT PRIMARY KEY,
    name VARCHAR(100),
    dept VARCHAR(100),
    course VARCHAR(100),
    grade VARCHAR(10)
);
