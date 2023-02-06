from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
def get_id():
    pass

class User(models.Model):
    customer_id = models.CharField(max_length=20,null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length = 10, validators=[MinLengthValidator(10)])
    #phone_no = models.BigIntegerField()
    password = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=20, null=True,blank=True)
    address = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.customer_id = '12345'
        super(User, self).save(*args, **kwargs)
    class Meta:
        db_table = "account_user"

