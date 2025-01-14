# Django Medical System

A Django-based medical management system deployed on Render.com with PostgreSQL database integration.

## Technology Stack

- Python 3.10.0
- Django (Latest stable version)
- PostgreSQL (via Render.com managed database)
- Gunicorn (Web server)
- Static files served from `staticfiles` directory

## Deployment Configuration

This project is configured for deployment on Render.com with the following specifications:

### Web Service
- Build Command: `pip install -r requirements.txt && python manage.py collectstatic --no-input`
- Start Command: `cd medical_system && gunicorn medical_system.wsgi:application`
- Auto Deploy: Enabled
- Health Check Path: `/health/`
- Web Concurrency: 4 workers

### Database
- Type: PostgreSQL
- Plan: Starter
- Database Name: django_medical_db
- User: django_medical_user

## Local Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd medical_system
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create .env file with the following variables
DJANGO_SETTINGS_MODULE=medical_system.settings
DJANGO_DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgres://localhost/django_medical_db
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create superuser:
```bash
python manage.py createsuperuser
```

7. Run development server:
```bash
python manage.py runserver
```

## Project Structure
```
medical_system/
├── medical_system/          # Main project directory
│   ├── __init__.py
│   ├── settings.py         # Project settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── staticfiles/           # Collected static files
├── requirements.txt       # Project dependencies
└── render.yaml           # Render deployment configuration
```

## Deployment Instructions

### Prerequisites
- A Render.com account
- Git repository with your project
- PostgreSQL database (automatically provisioned by Render)

### Deployment Steps

1. Push your code to your Git repository

2. On Render.com:
   - Create a new Web Service
   - Connect your repository
   - The `render.yaml` configuration will automatically set up:
     - Build and start commands
     - Environment variables
     - Database connection
     - Static file serving

3. Verify the deployment:
   - Check the build logs
   - Visit the health check endpoint
   - Verify database migrations

## Environment Variables

The following environment variables are configured in `render.yaml`:

- `PYTHON_VERSION`: 3.9.0
- `DATABASE_URL`: Automatically set from the linked database
- `SECRET_KEY`: Automatically generated
- `DJANGO_SETTINGS_MODULE`: medical_system.settings
- `WEB_CONCURRENCY`: 4
- `DJANGO_DEBUG`: false

## Database Management

The database is automatically provisioned and managed by Render.com:
- Plan: Starter
- Automatic backups: Included
- Connection string: Automatically injected into environment variables

## Static Files

Static files are served from the `staticfiles` directory:
- Collected during build using `python manage.py collectstatic`
- Served directly by Render.com

## Health Checks

The application includes a health check endpoint at `/health/` which is used by Render.com to monitor the application's status.

## Scaling

The application is configured with 4 Gunicorn workers by default. This can be adjusted by modifying the `WEB_CONCURRENCY` environment variable in `render.yaml`.

## Troubleshooting

Common issues and solutions:

1. Static files not loading:
   - Verify `STATIC_ROOT` in settings.py
   - Check if collectstatic command completed successfully

2. Database connection issues:
   - Verify DATABASE_URL environment variable
   - Check database status in Render dashboard

3. Application errors:
   - Check application logs in Render dashboard
   - Verify environment variables are set correctly

## Support

For deployment-related issues:
- Check Render.com documentation
- Contact Render.com support
- Review application logs in Render dashboard

## Security Notes

- Debug mode is disabled in production
- Secret key is automatically generated
- Database credentials are managed securely by Render
- HTTPS is enabled by default

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

This project is licensed under the MIT License.
