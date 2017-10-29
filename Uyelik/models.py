from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import user_logged_in
from django.utils import timezone

from stdimage.models import StdImageField
from Profil.storage import OverwriteStorage
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
                             blank=True,)

    # Add your own at will, but be mindful of collisions.
    dogum_tarihi = models.DateField(verbose_name="Doğum Tarihi",
                                    help_text='Doğum Tarihi',
                                    blank=True,
                                    null=True)
    profil_foto = StdImageField(variations={'thumbnail': {'width': 140, 'height': 140}}, blank=True,
                                null=True, storage=OverwriteStorage())

    class Meta:
        verbose_name_plural = "Kullanıcı Detayları"
    def __str__(self):
        return self.user.username

def son_oturum_acma(sender, user, request, **kwargs):
    user.last_login = timezone.now()
    user.save()

user_logged_in.connect(son_oturum_acma)