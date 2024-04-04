from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model
from django.contrib.auth import login , logout, authenticate
User = get_user_model()
def signup(request):
   if request.method == "POST":
    # le traitement du formulaire 
     username = request.POST.get("username") 
     password = request.POST.get("password")
     email = request.POST.get("email")
     first_name = request.POST.get ("first_name") 
     last_name = request.POST.get ("last_name")
     password_confirm = request.POST.get("password_confirm")

      # Vérifiez si les mots de passe correspondent
     if password != password_confirm:
            # Gérer l'erreur si les mots de passe ne correspondent pas
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})
     
     user = User.objects.create_user(username = username,
                                     email=email, 
                                     password=password,
                                     first_name=first_name,
                                     last_name=last_name)
     login(request, user)
     return redirect('index')
   

   return render(request, 'accounts/signup.html')

def login_user(request):
  if request.method == "POST":
    # Connester l'utilisateur 
    username = request.POST.get("username")
    password = request.POST.get("password")
    
    user = authenticate(username=username, password=password)
    if user:
       login(request, user)
       return redirect('index')
  
  return render (request, 'accounts/login.html', {'error_message': 'Identifiants incorrects'})
 

def logout_user (request):
  logout(request)
  return redirect('index') 