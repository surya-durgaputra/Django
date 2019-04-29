from django.db import models

class Pet(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    # since sex is either M or F, set max_length=1
    # since we might not be able sex some pets, set blank=True
    sex = models.CharField(choices=SEX_CHOICES, max_length=1, blank=True)
    # set the null=True because some pets might be rescued and age might not be knows
    # we dont set blank=True here because that will set this field to 0 and it will
    # not be distinguishable from the value 0 which is used to indicate that the pet is
    # less than one year old
    # storing null makes it clear that the age is unknown
    submission_date = models.DateTimeField(null=True)
    # a pet can have many vaccines
    # a vaccine can be given to many pets
    # set blank=True because a pet can have no vaccines
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)