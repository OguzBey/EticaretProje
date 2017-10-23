from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'myuser')
    MUSTERI = "MS"
    SATICI = "ST"
    SECENEKLER = (
        (MUSTERI, "Müşteri"),
        (SATICI, "Satıcı"),
    )
    kullanici_tipi = models.CharField(choices=SECENEKLER,
                                      max_length=2,
                                      help_text='Lütfen üye tipinizi seçiniz.',
                                      default='MS',
                                      verbose_name='Üye Tipi')
    adres = models.TextField(max_length=100, help_text='Lütfen bir adres yazın.',
                             verbose_name='Adres',
                             blank=True)

    # Add your own at will, but be mindful of collisions.
    dogum_tarihi = models.DateField(verbose_name="Doğum Tarihiniz.",
                                    help_text='Doğum Tarihi',
                                    blank=True,
                                    null=True)
