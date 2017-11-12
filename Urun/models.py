from django.db import models
from django.contrib.auth.models import User
import time
# Create your models here.

class Urun(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="satici")
    urun_adi = models.CharField(max_length=30,
                                blank=False,
                                null=False)
    urun_stok = models.IntegerField(blank=False,
                                    null=False,
                                    default=0)
    urun_ktarihi = models.DateTimeField(auto_now=True,
                                        blank=False,
                                        null=False,
                                        editable=False)
    urun_fiyati = models.FloatField(null=False,
                                    blank=False,
                                    default=0.0)
    urun_aciklama = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Ürünler"


    def __str__(self):
        return self.urun_adi



