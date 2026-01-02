from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def home(request):
    return render(request, 'login.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        #Checks of a user with the provided username exits
        if not User.objects.filter(username=username).exists():
        #Display an error message if the username does not exit
         messages.error(request,'Invalid Username')
         return redirect('/login/') #might needed changing
    
        user =  authenticate(user-username, password=password)

        if user is None:
        #Display and error message if authentication fails (invalid password)
          messages.error(request, "Invalid Password")
          return redirect('login')
        else:
            login(request, user)
            return redirect('/home/')
        
    return render(request, 'login.html')

#View function for registration page
def register_page(request):
   if request.method == 'Post' :
      first_name =  request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      username = request.POST.get('username')
      password = request.POST.get('password')

      #check if a user with the provided username already exits
      user = User.objects.filter(username=username)

      if user.exists():
         messages.info(request, "Username already taken")
         return('/register/')
      
      user = User.objects.create_user(
         first_name = first_name,
         last_name=last_name,
         username=username       
    )
      user.set_password(password)
      user.save()

      messages.info(request, "Account created Sucessfully")
      return redirect('/register/')
   
   return render(request, 'register.html')

             
