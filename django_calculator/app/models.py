from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
OPERATOR = [
    ('+', '+'),
    ('-', '-'),
    ('*', '*'),
    ('/', '/')
]

class Operation(models.Model):
    num1 = models.FloatField()
    operator = models.CharField(max_length=1, choices=OPERATOR)
    num2 = models.FloatField()
    answer = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User')
    created = models.DateTimeField(auto_now=True)


ACCESS_LEVEL = [
    ('o', 'Owner'),
    ('a', 'Account_User')
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, null=True, blank=True, choices=ACCESS_LEVEL, default='a')

    @property
    def is_owner(self):
        return self.access_level == 'o'

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance)
