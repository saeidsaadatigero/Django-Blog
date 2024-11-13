# Django Blog Project

This is a simple blog application built with Django. It allows users to create, read, update, and delete blog posts, as well as comment on them. The application uses Bootstrap for styling and crispy forms for better form handling.

## Features

- User authentication (login, logout, signup)
- Create, update, delete, and view blog posts
- Comment on blog posts
- Pagination for blog posts
- Search functionality for posts
- Caching for improved performance

## Requirements

- Python 3.x
- Django 5.0.1
- Other dependencies listed in `requirements.txt`

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saeidsaadatigero/django-blog.git
   cd django-blog
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

- Navigate to the home page to view the list of blog posts.
- Click on a post title to view its details and comments.
- Use the "Add new post" link to create a new blog post (requires login).
- Users can log in, log out, and sign up for an account.

## Directory Structure

```
django-blog/
│
├── config/               # Django project settings
├── blog/                 # Blog app containing models, views, and templates
├── accounts/             # User authentication app
├── media/                # Uploaded media files
├── static/               # Static files (CSS, JS, images)
├── templates/            # HTML templates
├── manage.py             # Django management script
└── requirements.txt      # Python dependencies
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
```

Feel free to modify any sections to better fit your project's specifics!