#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from dotenv import load_dotenv

def main():
    """Run administrative tasks."""
    load_dotenv()
    
    PORT = os.getenv('DJANGO_PORT', '8000')  # Default to 8000 if DJANGO_PORT is not set
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if len(sys.argv) == 1:
        sys.argv.extend(['runserver', f'0.0.0.0:{PORT}'])
    elif len(sys.argv) > 1 and sys.argv[1] == 'runserver' and len(sys.argv) == 2:
        sys.argv.append(f'0.0.0.0:{PORT}')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
