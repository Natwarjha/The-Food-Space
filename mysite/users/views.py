from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users.forms import RegisterForm,ProfFormEditing, ProfFormCreating, CusOrdersUpd, CusRatFeedForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from users.forms import ProfFormEditing, ProfFormCreating
from users.models import Profile, CusOrders, CusRatingFeedback 
from django.http import JsonResponse
import json


# Create your views here.

def register(request):
    
    if request.method == 'POST':
     form = RegisterForm(request.POST)
     if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(
           request,
           'Welcome {}, Your account has been sussessfully created. Now you may login below'.format(username)
        )
        userobj = User.objects.get(username=username)
        userid = userobj.id
        return redirect('profformcreate', user_id =userid) 
    else:
        form = RegisterForm()  

    
    context = {
      'form':form
     }

    return render(request, 'users/register.html', context)

def login_view(request):
   
   if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']

      if (username == '') or (username is None):
         username = User.objects.get(email=email)
      user = authenticate(request, username=username, password=password)
   
      if user is None:
         messages.success(
           request,
           'Invaid user, try again'.format(user)
        )
         return redirect('login')

      elif user.is_superuser:
         login(request,user)
         messages.success(
           request,
           'Welcome {}, Your account superuser has been logged in  sussessfully'.format(user)
        )
         return redirect('profile')
      elif user is not None:
      
         login(request, user)

         messages.success(
           request,
           'Welcome {}, Your account has been logged in  sussessfully'.format(user)
        )
         
         return redirect('profile')
   
   return render(request, 'users/login.html')

def logout_view(request):

   if request.method == 'POST':
      user = request.user.username
      logout(request)
      messages.success(
         request,
         'Welcome {}, Your account has been logged out sussessfully.'.format(user)
      )


      return redirect('food:index')
   
   return render(request, 'users/logout.html')

# @login_required
# def ProfilePage(request):

#    context = {

#    }
#    return render(request, 'users/profile.html', context)



def ProfilePage(request):

   prof = Profile.objects.get(user= request.user.id)
   

   if not request.user.is_authenticated:

      return redirect('login')
   
   context = {
      'prof': prof
   }

   return render(request, 'users/profile.html', context)

# Editing the profile form 
# -------------------------------------------------
def ProfViewEditing(request, prof_id):

   prof = Profile.objects.get(id=prof_id)
   form = ProfFormEditing(request.POST or None, request.FILES or None, instance=prof)
   
   if request.method == 'POST':
      form.save()
      return redirect('profile')

   context = {
      'form':form

   }

   return render(request, 'users/profformedit.html', context)


# crreating  the profile form (prom from two) 
# -------------------------------------------------
def ProfViewCreating(request, user_id):
   prof = Profile.objects.get(user=user_id)
   profform = ProfFormCreating(request.POST or None, instance=prof)

   if request.method =='POST':
      if profform.is_valid():
         profform.save()
      return redirect('login')

   context = {
      'prof':prof,
      'profform':profform

   }
   return render(request, 'users/profformcreate.html', context)

def Orders(request, itemid, pdcd, user):

   if request.method == 'POST':

      quantity = request.POST['qty']

      cusordsobj = CusOrders(
         prod_code=pdcd,
         quantity= quantity,
         username=user,

      )
      cusordsobj.save()
      return redirect('food:detail', item_id=itemid)

   context = {
      'usernsme':user,
      'pdcd':pdcd
   }
   
   return render(request, 'users/orders.html', context)

def Updateorders(request, orderid, itemid):
   coo = CusOrders.objects.get(order_id=orderid)
   form = CusOrdersUpd(request.POST or None, instance=coo)

   if request.method == 'POST':
      if form.is_valid():
         form.save()
         return redirect('food:detail', item_id=itemid)

   context = {
      'form':form
   }
   return render(request, 'users/updorders.html', context)

def CusRatFeedView(request, itemid, pc):
   form = CusRatFeedForm(request.POST or None)

   if request.method == 'POST':
      form.instance.prod_code = pc
      form.instance.username = request.user.username
      if form.is_valid():
         form.save()
         return redirect('food:detail', item_id=itemid)
   context = {
      'form':form
   }
   return render(request, 'users/cusratfeed.html', context)


def UpdateCRF(request, detailid, crfid):

    crfo = CusRatingFeedback.objects.get(pk=crfid)
    form = CusRatFeedForm(request.POST or None, instance=crfo)

    context = {
        'form':form
    }
    if request.method == 'POST':
      if form.is_valid():
        form.save()
        return redirect('food:detail', item_id=detailid)

    return render(request, 'users/cusratfeed.html', context)

def DeleteCRF(request, detailid, crfid):

    crfo = CusRatingFeedback.objects.get(pk=crfid)

    context = {
        'crfo':crfo
    }

    if request.method == 'POST':
        crfo.delete()
        return redirect('food:detail', item_id=detailid)

    return render(request, 'users/delcrf.html', context)

def Payment(request, amt, qnt):

    context = {
        'amt':amt,
        'qnt':qnt,
        'tot':amt * qnt,
        'varid': 1
    }

    return render(request, 'users/payment.html', context)

def OnApprove(request):

    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)

        context = {

        }

        return JsonResponse(context)


def PaymentSuccess(request):

    return render(request, 'users/pymtsuccess.html')

def PaymentSuccessVar(request, var):
    
    print(var)

    return render(request, 'users/pymtsuccess.html')
