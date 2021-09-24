from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.CharField(max_length=50)
    name = models.CharField(max_length= 100)
    phone_no = models.CharField(max_length=11)
    email_id = models.CharField(max_length=100)
    area = models.CharField(max_length=100,null=True)
    family_mem = models.IntegerField(default=0)
    mem_name = models.CharField(max_length= 100,null=True)
    visit_for_Queries = models.CharField(max_length=500, null=True, default='Not done')
    surgical_or_consultation = models.CharField(max_length=500, null=True, default='Not done')
    medicine_sold = models.CharField(max_length=500, null=True,default='Not done')
    diagnostic = models.CharField(max_length=500, null=True, default='Not done')

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_id(customer_id):
        try:
            return Customer.objects.get(customer_id = customer_id)
        except:
            return False

