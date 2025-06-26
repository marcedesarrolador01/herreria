"""""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'herrero.settings')  # si tu settings está en herrero/settings.py
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("alejandroperez", "admin@example.com", "herreria2025perez270625")
    print("✅ Superusuario creado")
else:
    print("⚠️ El superusuario ya existe")"""