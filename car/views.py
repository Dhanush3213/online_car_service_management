from django.shortcuts import render
from car.models import Service
from userapp.models import Order, User, Login

# Create your views here.
def adminhome(request):
    return render(request,'admin/adminhome.html')

def addService(request):
    if request.method=='POST':
        service= Service()
        service.sname=request.POST.get('title')
        service.stype=request.POST.get('type')
        service.price=request.POST.get('price')
        service.description=request.POST.get('desc')
        service.no_services = request.POST.get('copy')
        if len(request.FILES)!=0:
            service.image = request.FILES['image']
        service.save()
    return render(request,"admin/addService.html")



def updateService(request):
        service = Service.objects.all()
       
        return render(request,"admin/geteditService.html",{'service': service})

def deleteservice(request,id):
  Service.objects.get(id = id).delete()
  service = Service.objects.all() 
  return render(request,"admin/geteditService.html",{'service': service})
   
def latestorders(request):
    orders = Order.objects.all()
    return render(request,"admin/latestorders.html",{'orders':orders})


def enableusers(request):
    users = Login.objects.all().filter(role=1)
    return render(request,"admin/enableusers.html",{'users':users})
    
def enableUser(request,id):
    user = Login.objects.get(id=id)
    user.role=2
    user.save()
    users = Login.objects.all().filter(role=1)
    return render(request, "admin/enableusers.html", {'users': users})

def viewusers(request):
    users = User.objects.all()
    

    return render(request,"admin/allusers.html",{'users':users})

