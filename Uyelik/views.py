from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib import messages
from django.forms.models import inlineformset_factory
from .models import MyUser
from django.contrib.auth.models import User
# Create your views here.

def uyelik_formu(req):
    user_form = UserForm()
    if req.method == "POST":
        user_form = UserForm(req.POST)
        if user_form.is_valid():
            user = user_form.save()
            grup = user_form.cleaned_data['kullanici_tipi']
            if grup == "MS":
                g = Group.objects.get(name='Müşteriler')
                g.user_set.add(user)
            else:
                g = Group.objects.get(name='Satıcılar')
                g.user_set.add(user)
        # else:
        #     return render(req, 'marketle/uyelik.html', context={'userform': user_form})

            return HttpResponseRedirect(reverse('login'))

    context = {'form': user_form, }
    return render(req, 'marketle/uyelik.html', context=context)

