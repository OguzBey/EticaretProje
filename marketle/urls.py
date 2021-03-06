"""marketle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import handler404
from django.contrib import admin
from Anasayfa.views import *
from django.contrib.auth import views as auth_views
from Uyelik.views import uyelik_formu
from Profil.views import *
from django.conf.urls.static import static
from Urun.views import *
from django.shortcuts import render_to_response
from django.template import RequestContext
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', anasayfa, name="anasayfa"),
    url(r'^logout/$', logout_user, name="logout"),
    url(r'login/$', auth_views.login, {'template_name': 'marketle/girisyap.html'}, name="login",
        ),
    url(r'^register/$', uyelik_formu, name="register"),
    url(r'^profil/$', kullanici_profili, name="profil"),
    url(r'^profil/edit$', kullanici_profili_duzenle, name="edit_profil"),
    url(r'^user/(?P<username>@\w+)$', kullanici_goruntule, name="show_user"),
    url(r'^account/edit$', hesap_ayarlari_duzenle, name="edit_account"),
    #product
    url(r'^product/add/$', urunEkle, name="add_product"),
    url(r'^product/edit/(?P<id>\d+)$', urunDuzenle , name="edit_product"),
    url(r'^product/delete/(?P<id>\d+)$', urunSil, name="delete_product"),
    url(r'^product/(?P<slug>[a-z0-9]+(\-[a-z0-9]+)*)/$', urunGoster, name="show_product"),
    url(r'^product/(?P<slug>[a-z0-9]+(\-[a-z0-9]+)*)/comment/(?P<id>\d+)$', yorumDuzenle, name="edit_comment")


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# handler404 = 'Anasayfa.views.sayfa_yok'


