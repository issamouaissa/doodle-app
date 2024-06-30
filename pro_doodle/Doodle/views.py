from django.shortcuts import render, redirect ,get_object_or_404
from .models import Sondage, DateSondage , Vote 
from .forms import SondageForm, DateSondageForm, VoteForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate , login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')



def sondage(request):
    if request.method == 'POST':
        form = SondageForm(request.POST)
        if form.is_valid():
            sondage = form.save()
            return redirect('dates_sondage', sondage_id=sondage.id)
    else:
        form = SondageForm()
    return render(request, 'sondage.html', {'form': form})

def dates_sondage(request, sondage_id):
    sondage = get_object_or_404(Sondage, id=sondage_id)
    if request.method == 'POST':
        form = DateSondageForm(request.POST)
        if form.is_valid():
            # Extraire les trois dates du formulaire
            date_1 = form.cleaned_data['date_1']
            date_2 = form.cleaned_data['date_2']
            date_3 = form.cleaned_data['date_3']
            
            # Créer et sauvegarder les instances DateSondage
            DateSondage.objects.create(sondage=sondage, date=date_1)
            DateSondage.objects.create(sondage=sondage, date=date_2)
            DateSondage.objects.create(sondage=sondage, date=date_3)
            
            # Rediriger vers la vue de confirmation
            return redirect('confirmation', sondage_id=sondage_id)
    else:
        form = DateSondageForm()
    return render(request, 'dates_sondage.html', {'form': form, 'sondage': sondage})


def confirmation(request, sondage_id):
    sondage = get_object_or_404(Sondage, id=sondage_id)
    dates_sondage = DateSondage.objects.filter(sondage=sondage)
    
    if request.method == 'POST':
        form = VoteForm(sondage, request.POST)
        if form.is_valid():
            for date_sondage in dates_sondage:
                checked = form.cleaned_data.get(f"date_{date_sondage.id}", False)
                if checked:
                    percentage = form.cleaned_data.get(f"percentage_{date_sondage.id}", 0)
                    percentage += 1
                    form.cleaned_data[f"percentage_{date_sondage.id}"] = percentage
                    # Mettez à jour le pourcentage dans la base de données si nécessaire
            return redirect('confirmation', sondage_id=sondage_id)
    else:
        form = VoteForm(sondage)

    context = {
        'sondage': sondage,
        'dates_sondage': dates_sondage,
        'form': form,
    }
    return render(request, 'confirmation.html', context)



def vote(request, sondage_id):
    sondage = get_object_or_404(Sondage, id=sondage_id)
    dates_sondage = DateSondage.objects.filter(sondage=sondage)

    if request.method == 'POST':
        selected_dates = request.POST.getlist('selected_dates')
        
        for date_id in selected_dates:
            date_sondage = get_object_or_404(DateSondage, id=date_id)
            # Incrémenter le nombre de votes pour cette date
            date_sondage.votes += 1
            date_sondage.save()
            # Enregistrer le vote dans la table Vote
            Vote.objects.create( date_sondage=date_sondage)

        return redirect('validation', sondage_id=sondage_id)

    return render(request, 'vote.html', {'sondage': sondage, 'dates_sondage': dates_sondage})

def validation(request, sondage_id):
    sondage = get_object_or_404(Sondage, id=sondage_id)
    return render(request, 'validation.html', {'sondage': sondage})

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')  
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def signin(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request , username=username , password=password)
        if user is not None:
            login (request, user)
            return redirect('/sondage')
        else:
            msg = 'Sorry, Error Login'
            form = AuthenticationForm(request.POST)
            return render(request,'login.html' , { 'form' : form , 'msg' : msg} )
    else:
        form = AuthenticationForm()
    return render(request,'login.html' , { 'form' : form} )

    

def index(request):
    return render(request, 'index.html')

def signout(request):
    logout(request)
    return redirect('/')

    
def aide(request):
    return render(request, 'aide.html')

def trafication(request):
    return render(request, 'trafication.html')

def contact(request):
    return render(request, 'contact.html')

def accueil(request):
    return render(request, 'accueil.html')