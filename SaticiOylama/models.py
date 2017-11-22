from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class SaticiOylama(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="oylama")
    oy_veren = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    oy_puani = models.IntegerField(default=1,
                                   blank=False,
                                   null=False,
                                   validators=[
                                       MaxValueValidator(10),
                                       MinValueValidator(1)])
    oy_verilis_tarihi = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.user.username # Oy alan kullanıcı adı

