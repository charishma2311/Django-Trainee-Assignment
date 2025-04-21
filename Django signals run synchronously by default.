# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import time

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal started")
    time.sleep(3)  # Delay to show it's blocking
    print("Signal finished")

# test.py (or run in shell)
from django.contrib.auth.models import User

print("Creating user...")
User.objects.create(username='fresh_user')
print("User created")
