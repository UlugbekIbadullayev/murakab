from django.db import models

class BaseModel (models.Model):
    created_at = models.DateField( auto_now_add=True)
    updated_at = models.DateField( auto_now=True)


    class Meta:
        managed = True