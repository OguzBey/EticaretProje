from django.shortcuts import render, HttpResponseRedirect, reverse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from Uyelik.models import MyUser
from .forms import UserEditForm, MyUserEditForm
from django.contrib.auth.models import User
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
    # user_edit_formset = inlineformset_factory(User, MyUser,
    #                                        fields=('adres','dogum_tarihi','profil_foto'))
    user_edit_form2 = MyUserEditForm(instance=req.user.myuser)

    myuser = MyUser.objects.get(user=req.user)


    if req.method == "POST":
        user_edit_form = UserEditForm(data=req.POST, instance=req.user)
        user_edit_form2 = MyUserEditForm(data=req.POST, files=req.FILES)
        if user_edit_form.is_valid() and user_edit_form2.is_valid():
            user = user_edit_form.save()
            m = MyUser.objects.get(user=user)
            if user_edit_form2.cleaned_data['profil_fotosu'] is None:
                pass
            else:
                m.profil_foto = user_edit_form2.cleaned_data['profil_fotosu']
            m.adres = user_edit_form2.cleaned_data['adres']
            m.dogum_tarihi = user_edit_form2.cleaned_data['dogum_tarihi']
            # m.profil_foto = user_edit_form2.cleaned_data['profil_fotosu']
            m.save()
            return HttpResponseRedirect(reverse('profil'))

    context = {'form1': user_edit_form,
               'form2': user_edit_form2,
               'myuser':myuser}
    return render(req, 'marketle/profil_duzenle.html', context=context)


@require_http_methods(["GET", "POST"])
def kullanici_goruntule(req, username):
    if req.method == "GET":
        uname = username.lstrip("@")
        # user = get_object_or_404(User, username=uname)
        try:
            user = User.objects.get(username=uname)
        except:
            user = None

        if user:
            context = {'users':user,
                       'check':True,
                       'r_username':username}
        else:
            context = {'check':False}
        return render(req, 'marketle/show_user.html', context=context)
    else:
        if req.user.is_superuser:

            uname = username.lstrip("@")
            do = req.POST['doit']

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

            #success
            return HttpResponseRedirect(reverse('show_user', kwargs={'username':username}))

        else:
            # İstek yapan kullanıcı admin değil csrf tahmin etmiş olabilir zor ama why not
            return HttpResponseRedirect(reverse('show_user', kwargs={'username':username}))

