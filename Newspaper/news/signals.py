from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver # импортируем нужный декоратор
from django.core.mail import mail_user
from .models import PostCategory
import threading

from news.tasks import new_post_subscription

@receiver(m2m_changed, sender = PostCategory)
# функция обработчик с параметрами под регистрацию сигнала
def new_post_notify(sender, instance, created, **kwargs):
    
    if kwargs['action'] == 'post_add':
        new_post_subscription(instance)
    
 
# коннектим наш сигнал к функции обработчику и указываем, к какой именно модели после сохранения привязать функцию
post_save.connect(new_post_notify, sender=PostCategory)

def notify_subscribers_next_week():
  timer = threading.Timer(604800, new_post_notify) #таймер на 1 неделю