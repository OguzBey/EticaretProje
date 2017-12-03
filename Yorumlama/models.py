from django.db import models
from Urun.models import Urun
from django.contrib.auth.models import User
from django.shortcuts import reverse
# Create your models here.

class UrunYorumlama(models.Model):
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE, related_name="urunyorum")
    yorum_yapan = models.ForeignKey(User, on_delete=models.CASCADE)
    yorum_baslik = models.CharField(null=False, blank=False, max_length=30)
    yorum_icerik =models.TextField(null=False, blank=False)
    yorum_tarihi = models.DateTimeField(auto_now_add=True)

    def yorum_yapan_url(self):
        username =  "@{}".format(self.yorum_yapan.username)
        return reverse('show_user', kwargs={'username': username})

