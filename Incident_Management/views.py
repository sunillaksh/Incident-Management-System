from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login,logout
from Incident_Management.models import Incident_Data
from django.contrib import messages


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('signup')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('signup')
        
        if len(username)>20:
            messages.error(request, "Username must be under 20 charcters!!")
            return redirect('signup')
        
        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('signup')
        
        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('home')
    else:
        return render(request,"signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Sucessfully!!")
            return redirect('Incidents')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('signin')    
    return render(request, "signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('signin')

# provision to search the incident using the Incident ID. 
def Incidents(request):
    Incident_Datadata = Incident_Data.objects.filter(user=request.user)
    Incident_IDnum = ''
    if request.method=="POST":
        Incident_IDnum = request.POST.get('incident_tl') 
        if Incident_IDnum != None:
            Incident_Datadata = Incident_Data.objects.filter(user=request.user, Incident_ID__icontains=Incident_IDnum)
    data = {
        'Incident_Datadata':Incident_Datadata,
        'Incident_IDnum':Incident_IDnum
    }    
    return render(request, "Incidents.html", data)

def IncidentView(request, id):
    Incident_Datadata = Incident_Data.objects.get(id=id)
    data = {
        'Incident_Datadata':Incident_Datadata,
    }     
    return render(request, "IncidentView.html", data)

def Incidentdelet(request, id):
    Incident_Datadata = Incident_Data.objects.get(id=id)
    Incident_Datadata.delete()
    return HttpResponseRedirect(reverse(Incidents))

def Incidentcreate(request):
    if request.method=="POST":
        Incident_Detail = request.POST.get('Incident_dl')
        Incident_Priority = request.POST.get('Ipr')
        Incident_Status = request.POST.get('Iss')
        sn = Incident_Data(Incident_Status=Incident_Status,Incident_Detail=Incident_Detail,Incident_Priority=Incident_Priority,user=request.user)
        sn.save()
    return HttpResponseRedirect(reverse(Incidents))

def Incidentedit(request, id):
    Incident_Datadata = Incident_Data.objects.get(id=id)
    data = {
        'Incident_Datadata':Incident_Datadata,
    }     
    return render(request, "Incidentedit.html", data)

def saveIncidentedit(request, id):   
    if request.method=="POST":
        Incident_Detail = request.POST.get('Incident_dl')
        Incident_Priority = request.POST.get('Ipr')
        Incident_Status = request.POST.get('Iss')
        Incident_Datadata = Incident_Data.objects.get(id=id)        
        Incident_Datadata.Incident_Detail=Incident_Detail
        Incident_Datadata.Incident_Priority=Incident_Priority
        Incident_Datadata.Incident_Status=Incident_Status
        Incident_Datadata.save()
    return HttpResponseRedirect(reverse(Incidents))