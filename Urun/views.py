from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import UrunEkleForm
from .models import Urun
from django.contrib.auth.models import User
import os
from base64 import b64encode
from django.core.files import File
from marketle import settings


# Create your views here.


@require_http_methods(["GET", "POST"])
@login_required(login_url='/login/')
def urunEkle(req):
    if req.method == "GET":

        if req.user.groups.all() and req.user.groups.all().first().name == "Satıcılar":
            form = UrunEkleForm()
            prev_link = req.META.get('HTTP_REFERER')
            context = {'form': form,
                       'prev': prev_link}
            return render(req, 'marketle/urun_ekle.html', context=context)
        else:
            return HttpResponseRedirect(reverse('anasayfa'))

    else:  # POST
        form = UrunEkleForm(data=req.POST, instance=req.user, files=req.FILES)
        if form.is_valid():
            urun_adi = form.cleaned_data['urun_adi_f']
            urun_stok = form.cleaned_data['urun_stok_f']
            urun_fiyati = form.cleaned_data['urun_fiyati_f']
            urun_aciklama = form.cleaned_data['urun_aciklama_f']
            urun_resmi = form.cleaned_data['urun_resmi_f']
            s_user = User.objects.get(username=req.user.username)
            if urun_resmi is not None:
                pass
            else:
                f = open(os.path.join(settings.BASE_DIR, 'static/image/avatars/urun_yok.png'), 'rb')
                urun_resmi = File(f)
                urun_resmi.name = '{}.png'.format(b64encode("urunyok".encode()))

            Urun(user=s_user, urun_adi=urun_adi, urun_stok=urun_stok,
                 urun_fiyati=urun_fiyati, urun_aciklama=urun_aciklama,
                 urun_resmi=urun_resmi).save()
            return HttpResponseRedirect(reverse('anasayfa'))
        else:
            return HttpResponseRedirect(reverse('add_product'))


@require_http_methods(["GET", "POST"])
@login_required(login_url='/login/')
def urunDuzenle(req, id):
    if req.method == "GET":
        if req.user.groups.all().first().name == "Satıcılar":
            urun = Urun.objects.filter(id=id)
            if urun.exists():
                urun = urun.first()
                if urun.user.username != req.user.username:
                    return HttpResponseRedirect(reverse("anasayfa"))
                initial_data = {"urun_adi_f" :urun.urun_adi,
                                "urun_stok_f":urun.urun_stok,
                                "urun_fiyati_f":urun.urun_fiyati,
                                "urun_aciklama_f":urun.urun_aciklama}
                form = UrunEkleForm(initial=initial_data, instance=urun)
                prev_link = req.META.get('HTTP_REFERER')
                context = {'form': form,
                           'prev': prev_link,
                           'urun_resmi':urun.urun_resmi,
                           'urun_id':id}
                return render(req, 'marketle/urun_duzenle.html', context=context)
            else:
                # Böyle bir ürün yok
                return HttpResponse("<h1>Üzgünüz.. Hatalı ya da eksik bir sayfaya geldiniz.</h1>")
        else:
            return HttpResponseRedirect(reverse('anasayfa'))  # İzinsiz erişim yönlendirmesi
    else: # POST
        if req.user.groups.all().first().name == "Satıcılar":
            form = UrunEkleForm(data=req.POST, files=req.FILES)
            if form.is_valid():
                urun = Urun.objects.get(id=id)
                if urun.user.username != req.user.username:
                    return HttpResponseRedirect(reverse("anasayfa"))

                if form.cleaned_data['urun_resmi_f'] is None:
                    pass
                else:
                    urun.urun_resmi = form.cleaned_data['urun_resmi_f']
                urun.urun_adi = form.cleaned_data['urun_adi_f']
                urun.urun_stok = form.cleaned_data['urun_stok_f']
                urun.urun_fiyati = form.cleaned_data["urun_fiyati_f"]
                urun.urun_aciklama = form.cleaned_data["urun_aciklama_f"]
                urun.save()
                return HttpResponseRedirect(reverse('anasayfa'))
            pass
        else:
            return HttpResponseRedirect(reverse('anasayfa')) # İzinsiz erişim yönlendirmesi
        pass


@require_http_methods(["GET"])
@login_required(login_url='/login/')
def urunSil(req, id):
    if req.user.groups.all().first().name == "Satıcılar":
        urun = Urun.objects.get(id=id)
        if not urun:
            return HttpResponse("<h1>Üzgünüz.. Hatalı ya da eksik bir sayfaya geldiniz.</h1>")
        if urun.user.username != req.user.username:
            return HttpResponseRedirect(reverse("anasayfa"))
        urun.delete()
        return HttpResponseRedirect(reverse("anasayfa"))

    else:
        return HttpResponseRedirect(reverse("anasayfa"))




    pass

