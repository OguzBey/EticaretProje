from django.db import models
from django.contrib.auth.models import User
from stdimage.models import StdImageField
from Profil.storage import OverwriteStorage
from django.shortcuts import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
import os
from base64 import b64encode
from django.core.files import File
from marketle import settings
# Create your models here.

class Urun(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="satici")
    urun_adi = models.CharField(max_length=30,
                                blank=False,
                                null=False)
    urun_slug = models.SlugField(unique=True, editable=False)
    urun_resmi = StdImageField(variations={'thumbnail': {'width': 140, 'height': 140}}, blank=True,
                                null=True, storage=OverwriteStorage())
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

    def show_user_url(self):
        # url döndürmek için yazılmış method
        username = "@{}".format(self.user)
        return reverse('show_user', kwargs={'username':username})

    def __str__(self):
        return self.urun_adi

def create_new_slug(instance, new_slug=None):
    urun_slug = slugify(instance.urun_adi)
    if new_slug is not None:
        urun_slug = new_slug
    query = Urun.objects.filter(urun_slug=urun_slug)
    if query.exists():
        new_slug = "{0}-{1}".format(urun_slug, query.first().id)
        return create_new_slug(instance, new_slug=new_slug) # recursive
    return urun_slug

def pre_save_method(sender, instance, *args, **kwargs):

    if not instance.urun_slug: # İlk defa oluştururken
        instance.urun_slug = create_new_slug(instance)
    else: # düzenlerken
        instance.urun_slug = create_new_slug(instance)
    if not instance.urun_resmi: #resim yok
        f = open(os.path.join(settings.BASE_DIR, 'static/image/avatars/urun_yok.png'), 'rb')
        urun_resmi = File(f)
        urun_resmi.name = '{}.png'.format(b64encode("urunyok".encode()))
        instance.urun_resmi = urun_resmi
    else: # ürün resmi var
        pass




pre_save.connect(pre_save_method, sender=Urun)