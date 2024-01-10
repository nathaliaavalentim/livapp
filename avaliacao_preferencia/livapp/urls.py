from django.contrib import admin
from django.urls import path, include
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static



from .views import *

from . import views

app_name = 'livapp'
urlpatterns = [
    #path('', views.post_list, name='post_list'),
    #path('<slug:slug>', views.post_detail, name='post_detail'),
    #path('criar/', views.post_create, name='post_create'),
    #path('sobre-nos/', views.about, name='about'),
    #path('contato/', views.contact, name='contact'),
    path('logar_usuario/', views.logar_usuario, name='logar_usuario'),
    path('cadastrar_usuario/', views.cadastrar_usuario, name='cadastrar_usuario'),
    #path('index', views.index, name="index"),
    path('', views.IndexView.as_view(), name='index'),
    #path('avatar/', views.post_create, name='avatar'),
    path('avatar/', views.avatar, name='avatar'),
    path('picture/', views.picture, name='picture'),
    path('pictureex/', views.pictureex, name='pictureex'),
    path('picturereforco/', views.picturereforco, name='picturereforco'),
    path('picturedica/', views.picturedica, name='picturedica'),
    path('pictureex2/', views.pictureex2, name='pictureex2'),
    path('picturereforco2/', views.picturereforco2, name='picturereforco2'),
    path('picturedica2/', views.picturedica2, name='picturedica2'),
    path('pictureex3/', views.pictureex3, name='pictureex3'),
    path('picturereforco3/', views.picturereforco3, name='picturereforco3'),
    path('picturedica3/', views.picturedica3, name='picturedica3'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('accounts/', include('django.contrib.auth.urls')),
    
    path('pictureexant3/', views.pictureexant3, name='pictureexant3'),
    path('final/', views.final, name='final'),
    
    re_path(r'^$', views.home, name="home"),
    re_path(r'^upload/', views.upload, name="upload"),
    
    path(r'pictureex/upload/', views.upload, name="upload"),
        
    re_path(r'^$', views.home2, name="home2"),
    path(r'picturereforco/upload/', views.upload, name="upload"),
    
    re_path(r'^$', views.home3, name="home3"),
    path(r'picturedica/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home4, name="home4"),
    path(r'pictureex2/upload/', views.upload, name="upload"), 
    
    path('pictureexrep1/', views.pictureexrep1, name='pictureexrep1'),
    path('pictureexrep2/', views.pictureexrep2, name='pictureexrep2'),
    #path('pictureexrep3/', views.pictureexrep3, name='pictureexrep3'),
    
    re_path(r'^$', views.home5, name="home5"),
    path(r'pictureexrep1/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home6, name="home7"),
    path(r'picturereforco2/upload/', views.upload, name="upload"),
    
    re_path(r'^$', views.home7, name="home7"),
    path(r'picturedica2/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home8, name="home8"),
    path(r'pictureexrep2/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home9, name="home9"),
    path(r'pictureex3/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home10, name="home10"),
    re_path(r'picturereforco3/upload/', views.upload, name="upload"),
    
    re_path(r'^$', views.home11, name="home11"),
    path(r'picturedica3/upload/', views.upload, name="upload"), 
    
    #re_path(r'^$', views.home12, name="home12"),
    #path(r'pictureexrep3/upload/', views.upload, name="upload"), 
    
    re_path(r'^$', views.home13, name="home13"),
    path(r'pictureexant3/upload/', views.upload, name="upload"), 
    
    re_path(r'^salvaavatar/', views.salvaavatar, name="salvaavatar"),
    path(r'avatar/salvaavatar/', views.salvaavatar, name="salvaavatar"),
    
    re_path(r'^salvaavatarbd/', views.salvaavatarbd, name="salvaavatarbd"),
    path(r'picturereforco3/salvaavatarbd/', views.salvaavatarbd, name="salvaavatarbd"),

    re_path(r'^recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'picture/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureex/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureexrep1/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureex2/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureexrep2/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    path(r'pictureex3/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),
    #path(r'pictureexrep3/recuperaavatar/', views.recuperaavatar, name="recuperaavatar"),

    
    
    


]




