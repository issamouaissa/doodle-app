from django.urls import path
from . import views  # Importation de views
from .views import home, sondage, login, dates_sondage, confirmation, validation,vote

urlpatterns = [
    path('', views.home, name='home'),
    path('sondage/', views.sondage, name='sondage'),
    path('dates_sondage/<int:sondage_id>/', views.dates_sondage, name='dates_sondage'),
    path('confirmation/<int:sondage_id>/', confirmation, name='confirmation'),
    path('signup/', views.signup, name='signup'),
    path('index/', views.index, name='index'),
    path('signout/', views.signout, name='signout'),
    path('signin/', views.signin, name='signin'),
    path('index/signin/', views.signin, name='login'),
    path('index/signup/', views.signup, name='signup'),
    path('base/', views.base, name='base'),
    path('vote/<int:sondage_id>/', vote, name='vote'),
    path('validation/<int:sondage_id>/', validation, name='validation'),
    path('aide/', views.aide, name='aide'),
    path('trafication/', views.trafication, name='trafication'),
    path('contact/', views.contact, name='contact'),
    path('accueil/', views.accueil, name='accueil'),

]



