from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from Uyelik.models import MyUser
from .forms import UserEditForm, MyUserEditForm, HesapAyarlariForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from SaticiOylama.forms import SaticiOylamaForm
from SaticiOylama.models import SaticiOylama
# Create your views here.


@require_http_methods(["GET", "POST"])
@login_required(login_url='/login/')
def kullanici_profili(req):
    context = {}
    return render(req, 'marketle/profil.html', context=context)


@require_http_methods(["GET", "POST"])
@login_required(login_url='/login/')
def kullanici_profili_duzenle(req):

    user_edit_form = UserEditForm(instance=req.user)
    user_edit_form2 = MyUserEditForm(instance=req.user.myuser)

    myuser = MyUser.objects.get(user=req.user)


    if req.method == "POST":
        user_edit_form = UserEditForm(data=req.POST, instance=req.user)
        user_edit_form2 = MyUserEditForm(data=req.POST, files=req.FILES)
        if user_edit_form.is_valid() and user_edit_form2.is_valid():
            username = req.user.username
            email = req.user.email
            user = user_edit_form.save(commit=False)
            user.username = username
            user.email = email
            user.save()
            m = MyUser.objects.get(user=user)
            if user_edit_form2.cleaned_data['profil_fotosu'] is None:
                pass
            else:
                m.profil_foto = user_edit_form2.cleaned_data['profil_fotosu']
            m.adres = user_edit_form2.cleaned_data['adres']
            m.dogum_tarihi = user_edit_form2.cleaned_data['dogum_tarihi']
            m.save()
            return HttpResponseRedirect(reverse('profil'))

    context = {'form1': user_edit_form,
               'form2': user_edit_form2,
               'myuser': myuser}
    return render(req, 'marketle/profil_duzenle.html', context=context)


def isVoted(satici_username, oyveren_username):
    satici = User.objects.get(username=satici_username)
    oyveren = User.objects.get(username=oyveren_username)
    if satici.oylama.filter(oy_veren=oyveren).exists():
        return True # Oy vermiş
    else:
        return False # Oy vermemiş


def basariHesapla(user):

    oy_sayisi = len(user.oylama.all())
    if oy_sayisi == 0:
        return 0
    pay = 0
    payda = oy_sayisi*10
    for i in user.oylama.all():
        pay += i.oy_puani
    return "{:.2f}".format((pay/payda)*100)


@require_http_methods(["GET", "POST"])
def kullanici_goruntule(req, username):
    if req.method == "GET":
        satici_oylama_form = SaticiOylamaForm()
        uname = username.lstrip("@")
        # user = get_object_or_404(User, username=uname)
        try:
            user = User.objects.get(username=uname)
        except:
            user = None

        if user:
            if not user.is_superuser and user.groups.all().first().name == "Satıcılar": # Satıcı
                yuzde_basari = basariHesapla(user)
                if req.user.is_authenticated: # oturum açmış
                    if isVoted(uname, req.user.username): # oy vermişse ?
                        context = {'users': user,
                                   'check': True,
                                   'r_username': username,
                                   'basari': yuzde_basari,
                                   'oylama_formu_check': False,
                                   'isVoted': True}
                    else: # Oy vermemişse
                        context = {'users':user,
                                   'check':True,
                                   'r_username':username,
                                   'basari': yuzde_basari,
                                   'oylama_formu_check': True,
                                   'oylama_formu':satici_oylama_form,
                                   'isVoted': False}
                else: # oturum açmamış
                    context = {'users': user,
                               'check': True,
                               'r_username': username,
                               'basari': yuzde_basari,
                               'oylama_formu_check': False,
                               'isVoted': False}
            else: # Satıcı ve admin değil
                context = {'users': user,
                           'check': True,
                           'r_username': username,
                           'oylama_form_check': False}

        else: # Böyle bir kullanıcı yok
            context = {'check':False}
        return render(req, 'marketle/show_user.html', context=context)
    else: # POST
        do = req.POST['doit']
        uname = username.lstrip("@")
        user = User.objects.get(username=uname)  # satici
        oy_veren = User.objects.get(username=req.user.username)  # oy vermeye çalışan user
        if req.user.is_superuser:

            if do == "ban":

                try:
                    user = User.objects.get(username=uname)
                except:
                    #yanlış kullanıcı adı gönderildi
                    return HttpResponseRedirect(reverse('show_user', kwargs={'username':username}))

                user.is_active = False
                user.save()

            elif do == "unban":

                try:
                    user = User.objects.get(username=uname)
                except:
                    #yanlış kullanıcı adı gönderildi
                    return HttpResponseRedirect(reverse('show_user', kwargs={'username':username})) # hata sayfaya g

                user.is_active = True
                user.save()
            elif do == "oyver": # Oylama by admin

                form = SaticiOylamaForm(data=req.POST)
                if form.is_valid():
                    if not SaticiOylama.objects.filter(oy_veren=oy_veren).exists():
                        oy_puani = form.cleaned_data['oy_puani_f']
                        SaticiOylama(user=user, oy_veren=oy_veren, oy_puani=oy_puani).save()
                    else:
                        pass

            else:
                pass

            return HttpResponseRedirect(reverse('show_user', kwargs={'username':username}))

        else:
            # İstek yapan kullanıcı admin değil

            if do == "oyver":
                form = SaticiOylamaForm(data=req.POST)
                if form.is_valid():
                    if not SaticiOylama.objects.filter(oy_veren=oy_veren).exists():
                        oy_puani = form.cleaned_data['oy_puani_f']
                        SaticiOylama(user=user, oy_veren=oy_veren, oy_puani=oy_puani).save()
                    else:
                        pass
            else:
                pass
            return HttpResponseRedirect(reverse('show_user', kwargs={'username':username}))


@login_required(login_url='/login/')
@require_http_methods(["GET", "POST"])
def hesap_ayarlari_duzenle(req):
    back_url = req.META.get('HTTP_REFERER')
    if req.method == "GET":
        form = HesapAyarlariForm(instance=req.user, request=req)
        context = {"form": form ,
                   "back_url": back_url}
        return render(req, "marketle/hesap_ayarları.html", context=context)
    else: # POST
        form = HesapAyarlariForm(instance=req.user, data=req.POST, request=req)
        context = {
            "form" : form,
            "back_url": back_url
        }
        if form.is_valid():
            user = User.objects.filter(id=req.user.id).first()
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            user.username = username
            user.email = email
            user.save()
            return HttpResponseRedirect(reverse('profil'))
        return render(req, "marketle/hesap_ayarları.html", context=context)


