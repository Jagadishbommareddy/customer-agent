from django.core.urlresolvers import reverse
from django.db import models
from .validators import *


class ContactInfo(models.Model):
    mobile_number = models.CharField(max_length=20, validators=[validate_mobile_number])
    phone_number = models.CharField(max_length=20, validators=[validate_phone_number])
    email_id = models.EmailField(max_length=50)

class Customer(ContactInfo):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, validators=[validate_first_name])
    last_name = models.CharField(max_length=20, validators=[validate_last_name])

    def get_absolute_url(self):
        return reverse('customer-update', kwargs={'pk': self.pk})

class PropertyType(models.Model):
    propert_type_id= models.AutoField(primary_key=True)
    description= models.CharField(max_length=50)
class Agent(ContactInfo):
    agent_id= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=20,validators=[validate_first_name])
    last_name= models.CharField(max_length=20,validators=[validate_last_name])
    age=models.IntegerField()
    education= models.CharField(max_length=50,validators=[validate_education])
    company_name=models.CharField(max_length=50)
    specialization= models.CharField(max_length=100,validators=[validate_specialization])
    experience=models.IntegerField()
    agent_notes=models.TextField()
    property_type= models.ManyToManyField("PropertyType")
    def get_absolute_url(self):
        return reverse('agent-update', kwargs={'pk': self.pk})

class Location(models.Model):
    agent = models.ForeignKey(Agent)
    location_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=20, blank=True, null=True, validators=[validate_city])
    state = models.CharField(max_length=20, blank=True, null=True,validators=[validate_state])

class AgentReferal(models.Model):
    agent= models.ForeignKey(Agent)
    referal_id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=30,validators=[validate_name])
    verified= models.BooleanField(default=True)


class Address(models.Model):
        customer_id = models.ForeignKey(Customer, blank=True, null=True)
        agent_id = models.ForeignKey(Agent)
        address_id = models.AutoField(primary_key=True)
        address1 = models.CharField(max_length=100, blank=True, null=True)
        address2 = models.CharField(max_length=100, blank=True, null=True)
        city = models.CharField(max_length=20, blank=True, null=True, validators=[validate_city])
        state = models.CharField(max_length=20, blank=True, null=True, validators=[validate_state])
        landmark = models.CharField(max_length=20, blank=True, null=True, validators=[validate_landmark])
        pincode = models.IntegerField(blank=True, null=True)


