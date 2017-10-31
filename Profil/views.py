from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from Uyelik.models import MyUser
from .forms import UserEditForm, MyUserEditForm
# Create your views here.

@login_required(login_url='/login/')
def kullanici_profili(req):
    context = {}
    return render(req, 'marketle/profil.html', context=context)

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