from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Hero(models.Model):
    date = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(31)],default=0,blank=False,null=False)
    month = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(12)],default=0,blank=False,null=False)
    year = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(2021)],default=0,blank=False,null=False)
    age = models.IntegerField(validators=[MinValueValidator(1)
                                       ],default=0,blank=False,null=False)
                                    
    
