from django.shortcuts import render,HttpResponseRedirect,reverse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def anasayfa(req):

    if req.method == "GET":

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
