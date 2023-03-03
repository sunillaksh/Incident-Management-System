from django.db import models
from django.contrib.auth.models import User
import random
import datetime

# for genrate random ID
def incident_char():
    current_year = datetime.datetime.now().year
    random_number = random.randint(10000, 99999)
    return f'RMG{random_number}{current_year}'


# Create your models here.
class Incident_Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Incident_ID = models.CharField(max_length=12, default=incident_char)
    Incident_Detail = models.TextField(max_length=500)
    Incident_DT = models.DateTimeField(auto_now=True)
    Incident_Priority = models.CharField(max_length=50, choices=[('High','High'),('Medium','Medium'),('Low','Low')], null=True)
    Incident_Status = models.CharField(max_length=50, choices=[('Open','Open'),('In progress','In progress'),('Closed','Closed')], null=True)