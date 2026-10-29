# Contact Management System

A RESTful Contact Management System API built using **Django** and **Django REST Framework (DRF)**.

This project was developed as part of the **CodSoft Backend Development Internship – Task 2**. The API allows users to manage personal and professional contacts with CRUD operations, validation, searching, sorting, and pagination.

## 📌 Task Overview

The objective of this task is to build a backend system that manages personal and professional contacts.

The API provides functionality to:

- Create and manage contact records
- Store contact names, email addresses, phone numbers, addresses, and company information
- Retrieve, update, and delete contacts
- Search contacts by name, email, or phone number
- Sort and paginate contact records
- Validate user input and prevent duplicate contact entries
- Handle invalid requests with meaningful API responses

## 🚀 Features

### Contact Management

- Create a new contact
- Retrieve all contacts
- Retrieve a single contact
- Update contact information
- Partially update contact information
- Delete a contact
- Store name, email, phone number, address, and company information
- Email uniqueness validation
- Phone number uniqueness validation
- Indian phone number validation
- Name validation
- Address validation
- Company validation
- Automatic whitespace cleanup for validated fields

### Search and Filtering

- Search contacts by name
- Search contacts by email
- Search contacts by phone number
- Support search using query parameters
- Django REST Framework filtering support

### Sorting and Pagination

- Sort contacts by name
- Sort contacts by email
- Sort contacts by phone number
- Sort contacts by company
- Support ascending and descending order
- Paginate contact lists
- Configure the page size to 3 contacts per page

### Validation and Error Handling

- Prevent duplicate email addresses
- Prevent duplicate phone numbers
- Validate email format
- Validate Indian phone number format
- Reject blank names, addresses, and company names
- Return validation errors for invalid input
- Handle requests for non-existent contact IDs using Django REST Framework responses


# 🛠️ Technologies Used

- **Python**
- **Django**
- **Django REST Framework**
- **django-filter**
- **SQLite**
- **Git**
- **GitHub**
- **Postman** for API testing

# 🔗 API Endpoint Summary

Base URL: `http://127.0.0.1:8000/api/`

| Resource | Method | Endpoint |
|---|---|---|
| Contacts | GET | `/api/contacts/` |
| Contacts | POST | `/api/contacts/` |
| Contact Detail | GET | `/api/contacts/{id}/` |
| Contact Detail | PUT | `/api/contacts/{id}/` |
| Contact Detail | PATCH | `/api/contacts/{id}/` |
| Contact Detail | DELETE | `/api/contacts/{id}/` |

Replace `{id}` with the actual contact ID.

## 🔎 Search Endpoints

Search contacts using the `search` query parameter.

| Search By | Endpoint |
|---|---|
| Name | `/api/contacts/?search=Rahul` |
| Email | `/api/contacts/?search=gmail` |
| Phone | `/api/contacts/?search=9876` |

## ↕️ Sorting Endpoints

| Operation | Endpoint |
|---|---|
| Sort by name | `/api/contacts/?ordering=name` |
| Sort by name descending | `/api/contacts/?ordering=-name` |
| Sort by email | `/api/contacts/?ordering=email` |
| Sort by phone | `/api/contacts/?ordering=phone` |
| Sort by company | `/api/contacts/?ordering=company` |

## 📄 Pagination Endpoints

The API returns **3 contacts per page**.

| Page | Endpoint |
|---|---|
| Page 1 | `/api/contacts/?page=1` |
| Page 2 | `/api/contacts/?page=2` |
| Page 3 | `/api/contacts/?page=3` |

Search, sorting, and pagination can also be combined.

Example:

`/api/contacts/?search=Rahul&ordering=name&page=1`

---

# 📁 Project Structure

contact-management-system/
│
├── contact/
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── paginations.py
│
├── contact_management/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── .gitignore
├── db.sqlite3
├── manage.py
└── README.md



# 📝 Example API Request

### Create a Contact

**Method:** `POST`

**Endpoint:** `/api/contacts/`

Request body:

```json
{
    "name": "Rahul Sharma",
    "email": "rahul@example.com",
    "phone": "9876543210",
    "address": "New Delhi, India",
    "company": "Tech Solutions"
}
```

The API returns the created contact with its assigned ID when the request is successful.

---

# 🧪 API Testing

The API can be tested using Postman or the Django REST Framework browsable API.

Recommended test cases:

- Create a contact with valid information
- Retrieve all contacts and individual contacts
- Update and partially update contact details
- Delete a contact
- Search by name, email, and phone
- Test ascending and descending sorting
- Verify pagination
- Submit duplicate email addresses
- Submit duplicate phone numbers
- Test invalid email and phone formats
- Submit blank name, address, and company fields
- Request a contact ID that does not exist

---

# 📚 Learning Outcomes

Through this project, I practiced:

- Building REST APIs using Django REST Framework
- Creating Django models and managing database records
- Using ModelSerializers for serialization and validation
- Implementing CRUD operations with ModelViewSet and routers
- Implementing search, sorting, and pagination
- Applying field-level validation
- Using database uniqueness constraints
- Handling API validation errors
- Organizing a Django backend project
- Testing REST APIs with Postman



# 🎯 Internship Task

**Internship:** CodSoft Backend Development Internship

**Task:** Task 2 – Contact Management System

**Category:** Backend Development

**Objective:** Build a REST API that enables the management of personal and professional contacts with validation, search, sorting, and pagination.



**Technologies:** Python | Django | Django REST Framework | REST APIs | SQLite
