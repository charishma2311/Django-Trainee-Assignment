# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import connection

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal triggered")
    print("Inside transaction block:", connection.in_atomic_block)
