from django.db import models
#from model_utils import TimeStampedModel

# Create your models here.
class Inst(models.Model):
    inst_id = models.CharField(max_length=200)
    fulldomainname = models.CharField(max_length=400)
    pub_ip = models.CharField(max_length=200)
    pri_ip = models.CharField(max_length=200)

class Usr(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
