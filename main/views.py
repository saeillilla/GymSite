from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse,HttpResponseBadRequest
from django.forms import inlineformset_factory
from .forms import CreateUserform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BMIData,Trainer,personToTrainer,Subscription,personToSubsc
from django.contrib.auth import authenticate, login,logout

import json

# views.py

from django.http import JsonResponse

from .test import send_email

def showSubscriptions(request,id):
    data =Subscription.objects.filter(id=id)
    print(data)
    try:
        single_object = personToSubsc.objects.get(user=request.user.id,subscription = id)
        print(single_object)
        
        single_object.delete()
        
    except personToSubsc.DoesNotExist:
        insc = personToSubsc(user=request.user,subscription = data[0])
        insc.save()
        print("No Value Found")
        
    # print(id)
    return redirect("/userpanel/")

def subscribeTrainer(request,id):
    data =Trainer.objects.filter(id=id)
    print(data)
    try:
        single_object = personToTrainer.objects.get(user=request.user.id,trainer = data[0])
        single_object.delete()
        # print(single_object)
        
    except personToTrainer.DoesNotExist:
        insc = personToTrainer(user=request.user,trainer = data[0])
        insc.save()
        # print("saved")
    return redirect('/userpanel/')
    return HttpResponse(True)

    # return JsonResponse({'error': 'Object does not exist'}, status=404)

def getBMI(request):
    
    try:
        single_object = BMIData.objects.get(userID=request.user.id)
        data = {
                'age': single_object.age,
                'height': single_object.height,
                'weight': single_object.weight,
                'BMI': single_object.BMI,
            }

        return JsonResponse(data)
    except BMIData.DoesNotExist:
        data = {
                'age': "",
                'height': "",
                'weight': "",
                'BMI': "",
            }

        return JsonResponse(data)
        # return JsonResponse({'error': 'Object does not exist'}, status=404)



def change_bmi(request):

    if request.method == 'POST':
        decoded_string = request.body.decode("utf-8")

        json_object = json.loads(decoded_string)
        # Get the data from the POST request
        age = json_object['age']
        height = json_object['height']
        weight = json_object['weight']
        # bmi = json_object['BMI']

        # Perform the BMI calculation and update the model here
        bmi = weight / (height ** 2)
        # print(bmi)
        # print(type(request.user.id))
        try:
            single_object = BMIData.objects.get(userID=request.user.id)
        except BMIData.DoesNotExist:
            single_object = False
        if single_object:
            print("Object Exists")
            BMIData.objects.filter(userID=request.user.id).update(userID=request.user.id,age=age,height=height,weight=weight,BMI=bmi)
        else:
            insc = BMIData(userID=request.user.id,age=age,height=height,weight=weight,BMI=bmi)
            insc.save()

        print(bmi,height,weight)
        # Update your model with the calculated BMI
        # YourModel.objects.filter(your_conditions).update(bmi_field=bmi)

        # Respond with a success message or updated data
        return JsonResponse({'message': 'BMI updated successfully', 'bmi': bmi})
    else:
        return JsonResponse({'message': 'Invalid request'})




@login_required(login_url="/login")
def userpanel(request):
    isSubscribed = False
    
    trainers = Subscription.objects.all()
    trainers_subs = personToSubsc.objects.filter(user=request.user.id)
    print(trainers)
    # for j in trainers:
    #     print(j.id)
    data = {}
    for i in trainers:
        print("Subscription name")
        print(i.name)
        services = i.services.split(',')
        # print(services)
        for j in trainers_subs:
            print(j.subscription.id)
            if j.subscription.id ==i.id:
                isSubscribed = True
            else:
                isSubscribed = False
                
        data[i.id] = {"name":i.name,"pricing":i.pricing,"services":services,"subscribed":isSubscribed}
    context = {}
    print(data)
    trainers = Trainer.objects.all()
    
    
    for i in trainers:
        subscribed = personToTrainer.objects.filter(user=request.user.id,trainer = i.id)
        print(subscribed.count())
        
        # if i.id in subscribed:
        #     subs= True
        # else:
        #     subs= False
        # print(subs)
        if subscribed.count() == 1:
            trainer = {"id":i.id,"name":i.name,"field":i.field,"comments":i.comments,"image":i.profile_pic.url,"subscribed":True }
        else:
            trainer = {"id":i.id,"name":i.name,"field":i.field,"comments":i.comments,"image":i.profile_pic.url,"subscribed":False }
            
        context[i.id] = trainer
    print(context)
    return render(request,'userpanel.html',{'my_context': context,"subs":data})

# Create your views here.
def home(request):
    print(request.user.id)
    trainer = []
    trainers = Trainer.objects.all()
    for i in trainers:
        
        trainer.append( {"id":i.id,"name":i.name,"field":i.field,"comments":i.comments,"image":i.profile_pic.url,"subscribed":True })
        
    return render(request,'home.html',{"trainer":trainer})

def contactUs(request):
    trainer = []
    trainers = Trainer.objects.all()
    for i in trainers:
        
        trainer.append( {"id":i.id,"name":i.name,"field":i.field,"comments":i.comments,"image":i.profile_pic.url,"subscribed":True })
       
    if request.method =="POST":
        print(request.POST)
        print(request.POST["email"])
        print(request.POST["subject"])
        print(request.POST["message"])
        send_email("Gym Site Contact | "+request.POST["subject"],request.POST["message"],["saeil.moorsingal@gmail.com",request.POST["email"]])
    return render(request,'contact.html',{"trainer":trainer})

def loginPage(request):

    context = {}
    
    if request.method =='POST':
        context = {"name":request.POST["email"]}
        print(type(request.POST))
        print(request.POST["email"])
        print(request.POST["password"])
        user = authenticate(request, username =request.POST["email"],password =request.POST["password"]  )
        print(user)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.success(request,"Login Failed. Username or password is incorect")

        
    return render(request,'login.html',context)


def logoutPage(request):
    logout(request)
    return redirect('/login')


def signUp(request):
    form = CreateUserform()
    context = {'form': form}
    if request.method == 'POST':
        form = CreateUserform(request.POST)
        print("Post Methord")
        print("Checking If valid or not")
        print(form.is_valid())
        if form.is_valid():
            print("Saving Form")
            
            form.save()
            username = form.cleaned_data.get('username')
            print(username)
            messages.success(request,"Account created for username "+username)
            return redirect("/login")
    return render(request,'signup.html',context)