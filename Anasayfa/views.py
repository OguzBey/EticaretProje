from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from Urun.models import Urun
from django.contrib.auth.models import User

# Create your views here.

def anasayfa(req):

    if req.method == "GET":
        if len(req.user.groups.all()) == 0:
            group_name = "yok"
        else:
            group_name = req.user.groups.all().first().name


        # satici = req.user.satici
        # satici = User.objects.get(username=req.user.username)
        # urunler = Urun.objects.filter(user=satici)
        # print(urunler.all()[0].user.myuser.dogum_tarihi)
        # diger = req.user.myuser

        context = {}

        return render(req, 'marketle/anasayfa.html', context=context)


@login_required(login_url='/login/')
def logout_user(req):
    logout(req)
    return HttpResponseRedirect(reverse('anasayfa'))

# def login_user(req):
#     form1 = LoginwCapthca()
#     context = {'form':form1}
#     return  render(req, 'marketle/girisyap.html', context=context)
