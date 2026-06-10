# 🛒 MyShop — Flask E-Commerce Platform
 
A full-stack e-commerce web application built with Python, Flask, and MySQL. Features a complete shopping experience for customers and a powerful admin panel for store management.

 
### Customer Side
-  Homepage with hero section, categories, and featured products
-  Shop page with product search
-  Product detail page with stock info
-  Shopping cart (add, remove, view items)
-  Checkout with Cash on Delivery
-  Order confirmation with order details
-  User registration and login
### Admin Panel
-  Dashboard with revenue, order, and product stats
-  Add, edit, and delete products with image upload
-  View all customer orders
-  Update order status (Pending → Processing → Shipped → Delivered → Cancelled)
-  Order detail view with itemized products
---
 
## 🛠️ Tech Stack
 
| Layer | Technology |
| Backend | Python, Flask |
| Database | SQL Server (local) |
| ORM | SQLAlchemy + Flask-SQLAlchemy |
| Auth | Flask-Login, Werkzeug password hashing |
| Frontend | HTML, CSS, Jinja2 templates |
| File Upload | Flask file handling |

 
## 📁 Project Structure
 
```
E_Commerce/
│
├── app/
│   ├── blueprints/
│   │   ├── auth/          # Login, signup routes
│   │   ├── admin/         # Admin dashboard, product & order management
│   │   └── customer/      # Homepage, shop, cart, checkout
│   │
│   ├── models/
│   │   ├── user.py        # User model
│   │   ├── product.py     # Product model
│   │   ├── cart.py        # Cart model
│   │   ├── order.py       # Order model
│   │   └── order_item.py  # Order items model
│   │
│   ├── static/
│   │   ├── css/           # Stylesheets
│   │   └── uploads/       # Product images
│   │
│   ├── templates/
│   │   ├── admin/         # Admin HTML templates
│   │   └── customer/      # Customer HTML templates
│   │
│   └── extensions.py      # SQLAlchemy instance
│
├── config.py              # App configuration
├── run.py                 # App entry point
└── requirements.txt       # Python dependencies
```
 
---
 
 
### Run the app
bash
python run.py 
Open `http://127.0.0.1:5000` in your browser.
 

 
## 🔑 Default Admin Access
 
To create an admin user, register normally then update the role in your database:
 
sql
UPDATE Users SET role = 'admin' WHERE email = 'your@email.com'

 

 
## 📦 Requirements

Flask
Flask-Login
Flask-SQLAlchemy
PyMySQL


 
## 🗄️ Database Schema
 
| Table | Description |
|---|---|
| Users | Customer and admin accounts |
| Products | Product listings with images |
| Cart | Customer cart items |
| Orders | Customer orders with delivery info |
| Order_Items | Individual items within each order |
 
 
## Author
 
Ahsan Khan
