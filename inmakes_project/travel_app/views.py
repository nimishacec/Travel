from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from travel_app.models import Place


def login(request):
     if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']
         user=auth.authenticate(username=username,password=password)

         if user is not None:
             auth.login(request,user)
             return redirect('/')
         else:
             messages.info(request,"invalid login")
     return render(request,"login.html")

# Create your views here.
def  register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)

                user.save();
                messages.info(request, "user created")
                return redirect('login')
                #print("user created")
        else:
            messages.info(request, "password mismatch")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def  index(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'obj':obj})
# def  register1(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         email=request.POST['email']
#         password = request.POST['password']
#         password1 = request.POST['password1']
#         if password==password1:
#             if User.objects.filter(username=username).exists():
#                  print("Username exists")
#             elif User.objects.filter(email=email).exists():
#                  print("email exists")
#             else:
#                 user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name,email=email)
#
#                 user.save();
#                 print("user created")
#         else:
#             print("password mismatch")
#         #     #return redirect('register')
#         # #return redirect('/')
#     return render(request,"register1.html")