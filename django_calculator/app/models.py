from django.db import models

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
    access_level = models.CharField(max_length=1, null=True, blank=True, default='a', choices=ACCESS_LEVEL)

    @property
    def is_owner(self):
        return self.access_level == 'o'
