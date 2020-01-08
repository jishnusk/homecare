from django.shortcuts import render
from .models import Login
from .models import Prosignup
from .models import Customersignup
from django.http import HttpResponse
def prosignup(request):
    return render(request,'signup.html')    
def cussignup(request):
    return render(request,'customersignup.html')    
def homepage(request):
    return render(request, 'frontpage.html') 
def loginn(request):
    obj_email     = request.POST['uname']
    obj_password = request.POST['pass']
    obj_login = Login.objects.get(email = obj_email)
    if obj_login.email == obj_email:
        if obj_login.password == obj_password:
            request.session['userid']= obj_login.id
            return render(request,'new.html')
        else:
            return HttpResponse('password is wrong')
    else:
        return HttpResponse('invalid user details')
def profsignup(request):
    name=request.POST['fullname']
    gender=request.POST['gender']
    email=request.POST['em']
    mobile=request.POST['mb']
    pincode=request.POST['pn']
    experience=request.POST['ex']
    website=request.POST['pw']
    expertin=request.POST['expt']
    password=request.POST['pswd']
    obj_login=Login(email=email,password=password)
    obj_login.save()
    obj_prosignup=Prosignup(name=name,gender=gender,mobile=mobile,pincode=pincode,experience=experience,website=website,expertin=expertin,Fk_Login=obj_login)
    obj_prosignup.save()
    return HttpResponse("user Registered successfully")
def custsignup(request):
    cname=request.POST['cfullname']
    cemail=request.POST['cem']
    cmobile=request.POST['cmb']
    cpincode=request.POST['cpn']
    cpassword=request.POST['cpswd']            
    obj_login=Login(email=cemail,password=cpassword)
    obj_login.save()
    obj_custsignup=Customersignup(name=cname,mobile=cmobile,pincode=cpincode,Fk_Login=obj_login)
    obj_custsignup.save()
    return HttpResponse("user Registered successfully")
def search(request):
     return render(request, 'searchdata.html')   