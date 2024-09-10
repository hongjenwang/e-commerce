# Django E-commerce Site

This is a simple e-commerce site built with Django. It allows users to browse products, add them to their cart, and make purchases.

## Features
- User authentication and authorization
- Product browsing and searching
- Shopping cart functionality
- Order processing

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name

**2. Create and activate a virtual environment:**
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

**3. Install dependencies:**
   pip install -r requirements.txt

**4. Set up the database:**
   python manage.py migrate

**5. Create a superuser:**
   python manage.py createsuperuser

**6. Run the development server:**
   python manage.py runserver

**7. Access the application:**
   Open your browser and navigate to http://127.0.0.1:8000/

## Environment Variables

Create a .env file in the root directory and add the following:

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost, 127.0.0.1
DATABASE_URL=postgres://user:password@localhost:5432/dbname


