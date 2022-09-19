from django.shortcuts import render
from userapp.models import User, Login,Order
from car.models import Service
from datetime import date
# Create your views here.

def index(request):
    service=Service.objects.all()[:10]
    return render(request,"user/index.html",context={'service':service})

def index2(request):
    
    service=Service.objects.all()[:10]
   
    return render(request,"user/index2.html",context={'service':service})


def register(request):
    if request.method=='POST':
        loginobj = Login()
        loginobj.username = request.POST.get('username')
        loginobj.password = request.POST.get('password')
        loginobj.save()
        if Login.objects.filter(username=request.POST.get('username')).exists():
            user = User()
            user.firstname = request.POST.get('firstname')
            user.email = request.POST.get('email')
            user.loginid=loginobj
            user.save()
            if User.objects.filter(loginid = loginobj).exists():
                return render(request,"user/login.html")
        return render(request,"user/register.html",context={'error':'Registration failed'})
   
    return render(request, "user/register.html")

def login(request):
    if request.method=='POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')
        if Login.objects.filter(username=uname,password=pwd).exists():
            loginobj = Login.objects.get(username=uname,password=pwd)
            request.session['userid']=loginobj.id
            role=loginobj.role
            if role==0:
                return render(request,"admin/adminhome.html")
            if role==1:
                user = Login.objects.get(id=request.session['userid'])
                if uname=='admin' and pwd=='abc':
                      user.role=0
                      user.save()
                return render(request,"user/index2.html",{ 'user':user})
            elif role == 2:
                user = Login.objects.get(id=request.session['userid'])
                client = User.objects.get(loginid_id=request.session['userid'])
                return render(request, "user/profile.html",{'user':user,'client':client})
            else:
                return render(request, "user/index.html")

        return render(request, "user/login.html", context={'error': 'Login failed'})
   
    return render(request, "user/login.html" )

def logout(request):
    del request.session['userid']
    return render(request, "user/login.html")

def viewservice(request):
    service = Service.objects.all()
    return render(request,"user/viewservice.html",{'service':service})

def viewservice2(request):
    service = Service.objects.all()
    return render(request,"user/viewservice2.html",{'service2':service})

def vieworders(request):
    if 'userid' not in request.session:
       return render(request, "user/login.html")
    userid = request.session['userid']
    if Order.objects.filter(user_id=userid).exists():
        orders = Order.objects.order_by('-order_date','-id').filter(user_id=userid)
        return render(request,"user/vieworders.html",{'orders':orders})
    else:
        return render(request, "user/vieworders.html", {'ordermess':'No order history'})

def cancelorder(request,id):
    if 'userid' not in request.session:
        return render(request, "user/login.html")
    order = Order.objects.get(id = id)
    order.status=2
    order.save()
    service = Service.objects.get(id = order.Service.id)
    service.save()
    userid = request.session['userid']
    if Order.objects.filter(user_id=userid).exists():
        orders = Order.objects.order_by('-order_date').filter(user_id=userid)
        return render(request, "user/vieworders.html", {'orders': orders})
    else:
        return render(request, "user/vieworders.html", {'ordermess': 'No order history'})


def profile(request):
    service = Service.objects.all()[:10]
    user = Login.objects.get(id=request.session['userid'])
    client = User.objects.get(loginid_id=request.session['userid'])
    return render(request, "user/profile.html",context={'service': service, 'user':user,'client':client})

def editprofile(request):
    service = Service.objects.all()[:10]
    user = Login.objects.get(id=request.session['userid'])
    client = User.objects.get(loginid_id=request.session['userid'])
    if request.method=='POST':
        uname = request.POST.get('uname')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        user.uname = uname
        user.password=password
        client.firstname = name
        client.email = email
        client.save()
        user.save()
        return render(request, "user/editprofile.html",context={'service': service, 'user': user,'client': client})
    return render(request, "user/editprofile.html",context={'service': service,'user': user,'client': client})

def payment(request,id):
    if 'userid' not in request.session:
        return render(request, "user/login.html")
    if request.method=='POST':
        service = Service.objects.get(id=id)
        user = Login.objects.get(id = request.session['userid'])
        cardnum = request.POST.get("cardnumber")
        cvv=request.POST.get('cvv')
        exp = request.POST.get('exp')
        c_date = date.today()
        amount = request.POST.get('amount')
        booking_date=request.POST.get('booking_date')
       
        order = Order()
        order.Service=service
        order.user=user
        order.card_num=cardnum
        order.cvv=cvv
        order.expiry=exp
        order.order_date=c_date
        order.amount=amount
        order.booking_date=booking_date
        order.status=1
        order.save()

        if Order.objects.filter(Service_id=id).exists():
            return render(request, "user/index2.html",{'message':'Payment Successful'})
        else:
            service = service.objects.get(id=id)
            return render(request, "user/payment.html", {'service': service,'message':'payment failed'})
    else:
        service = Service.objects.get(id=id)
        return render(request, "user/payment.html",{'service':service})
