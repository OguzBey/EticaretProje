from django.shortcuts import render,HttpResponseRedirect,reverse, render_to_response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from Urun.models import Urun
from django.contrib.auth.models import User
from django.views import defaults
from django.template import exceptions
# Create your views here.

def anasayfa(req):

    if req.method == "GET":
        if len(req.user.groups.all()) == 0:
            group_name = "yok"
        else:
            group_name = req.user.groups.all().first().name


        urunler = Urun.objects.all().order_by('urun_ktarihi').reverse() # Yeni ürünler başta
        # req.user.myuser.dogum_tarihi # one to one
        # req.user.satici.all()[0].urun_stok # many to one

        context = {'urunler': urunler}

        return render(req, 'marketle/anasayfa.html', context=context)


@login_required(login_url='/login/')
def logout_user(req):
    logout(req)
    return HttpResponseRedirect(reverse('anasayfa'))

def sayfa_yok(req):

    response = render(req, '404.html', {})
    response.status_code = 404
    return response
