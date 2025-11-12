from django.db import models


class Material(models.Model):
    id=models.BigAutoField(primary_key=True)
    item = models.CharField( max_length=199)
    quant = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:

        db_table = 'material'



# Create your models here.
