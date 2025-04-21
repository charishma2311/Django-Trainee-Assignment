# signals.py
#Yes, they run in the same thread.
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal thread:", threading.current_thread().name)

# test.py
import threading
from django.contrib.auth.models import User

print("Main thread:", threading.current_thread().name)
User.objects.create(username='thread_check')
