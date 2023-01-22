from django.shortcuts import render
from .forms import customers
from .models import customer_reg
from .models import staff_reg
from .forms import station
from .models import stations
from .forms import train
from .models import trains
from .forms import route
from .models import routes
from .forms import offer
from .models import offers
from .forms import parking
from .models import parkings
from .forms import complaint
from .models import complaints
from .models import *
from django.shortcuts import redirect

from django.core.files.storage import FileSystemStorage

def first(request):
    return render(request,'index.html')


def customer(request):
    return render(request,'customer.html')

def dash(request):
    return render(request,'admin/index.html')
def customerdash(request):
    return render(request,'customer/index.html')
def staffdash(request):
    return render(request,'staff/index.html')    
'''def request(request):
    temp= request.session['uname'] 
    users=stations.objects.all()
    return render(request,'customer/request.html',{'result':temp,'res':users})'''
    
def request(request):
    users=routes.objects.all()

    return render(request,'customer/request.html',{'res':users})
    
def addcustomer(request):
    form =customer_reg()
    if request.method=='POST':
        form = customers(request.POST)
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['phonenumber']
        d = request.POST['password']
        e = request.POST['address']
        f = request.POST['gender']

        print(a)
        print(b)
        print(c)
        print(d)
        print(f)

        if form.is_valid():
            form.save()
        return render(request, 'customer.html')
    else:

        return render(request, 'customer.html')

def station(request):
    if request.method == 'POST':
        name = request.POST['name']
        user = stations(stationname=name)
        user.save()

        return render(request, 'admin/addstations.html')
                      
    else:

        return render(request, 'admin/addstations.html')

def offer(request):
    if request.method == 'POST':
        name = request.POST['evtname']
        offer = request.POST['eoffer']
        user = offers(eventname=name,offer=offer)

        user.save()


        return render(request, 'admin/addoffers.html' )


def parking(request):
    if request.method == 'POST':
        name = request.POST['stname']
        pslot = request.POST['sslot']
        rate = request.POST['rate']

        user = parkings(stationname=name,slot=pslot,rate=rate)

        user.save()


        return render(request, 'admin/parkingdetails.html' )
def train(request):
    context = {}
    if request.method == 'POST':
        number = request.POST['no']
        tname = request.POST['tname']
        time = request.POST['time']
        sname = request.POST['sname']
        uploaded_file = request.FILES['image']
        print(uploaded_file)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        user = trains(trainno=number,trainname=tname,traintime=time,stationname=sname,trainimage=uploaded_file)

        user.save()


        return render(request, 'admin/addtrains.html',context )

def viewrequest(request):
    users=userpayment.objects.all()
    return render(request,'staff/viewrequest.html',{'res':users}) 
    
def staff(request):
    if request.method == 'POST':
        address=request.POST['address']
        names=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        phonenumber=request.POST['phonenumber']
        designation=request.POST['designation']
        gender=request.POST['gender']
        uploaded_file = request.FILES['image']
        print(uploaded_file)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)

        data=staff_reg(name=names,address=address,email=email,password=password,phonenumber=phonenumber,gender=gender,designation=designation,image=uploaded_file)
        data.save()
    return render(request, 'admin/addstaff.html')

def route(request):
    if request.method == 'POST':
        name = request.POST['tname']
        sstation = request.POST['sstation']
        estation = request.POST['estation']
        distance = request.POST['dist']
        rate = request.POST['rate']
        user = routes(trainname=name,startstation=sstation,endstation=estation,distance=distance,rate=rate)

        user.save()


        return render(request, 'admin/addroutes.html' )

def ccomplaints(request):
    if request.method == 'POST':
        cid = request.POST['customerid']
        ccs = request.POST['complainsubject']
        desc = request.POST['description']
        user = complaints(customerid=cid,complainsubject=ccs,description=desc)

        user.save()


        return render(request, 'customer/addcomplaints.html' )
#select all


def viewstaff(request):
    sel=staff_reg.objects.all()
    return render(request,'admin/viewstaff.html',{'res':sel})
#//////

def viewcomplaint(request):
    sel=complaints.objects.all()
    return render(request,'admin/viewcomplaint.html',{'res':sel})


def viewcomplaints(request):
    sel=complaints.objects.all()
    return render(request,'staff/viewcomplaints.html',{'res':sel})

def viewstation(request):
    sel=stations.objects.all()
    return render(request,'admin/viewstation.html',{'res':sel})

def viewtrain(request):
    sel=trains.objects.all()
    return render(request,'admin/viewtrain.html',{'res':sel})


def viewoffer(request):
    sel=offers.objects.all()
    return render(request,'admin/viewoffer.html',{'res':sel})

def viewroute(request):
    sel=routes.objects.all()
    return render(request,'admin/viewroute.html',{'res':sel})

def viewparking(request):
    sel=parkings.objects.all()
    return render(request,'admin/viewparking.html',{'res':sel})


def logout(request):
    return render(request,'index.html')


def viewslot(request):
    sel=parkings.objects.all()
    return render(request,'customer/viewslot.html',{'res':sel})


def login(request):
    return render(request,'login.html')



def logins(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password == 'admin':
        request.session['userdetail'] = email
        request.session['user'] = 'admin'
        return render(request, 'admin/index.html')

    elif customer_reg.objects.filter (email=request.POST['email'],password=password).exists():
        userdetail=customer_reg.objects.get(email=request.POST['email'], password=password)
        if userdetail.password == request.POST['password']:
            request.session['uid'] = userdetail.id
            request.session['uname'] = userdetail.name

            request.session['uemail'] = email

            request.session['user'] = 'user'
            return render(request, 'customer/index.html')
            
    elif staff_reg.objects.filter (email=request.POST['email'],password=password).exists():
        userdetail=staff_reg.objects.get(email=request.POST['email'], password=password)
        if userdetail.password == request.POST['password']:
            request.session['sid'] = userdetail.id
            request.session['sname'] = userdetail.name

            request.session['semail'] = email

            request.session['staff'] = 'staff'
            return render(request, 'staff/index.html')

    else:

     return render(request,'index.html', {'status': 'failed'})


def addstaff(request):
    return render(request,'admin/addstaff.html')

def addstations(request):
    return render(request,'admin/addstations.html')

def addtrains(request):
    return render(request,'admin/addtrains.html')

def addroutes(request):
    return render(request,'admin/addroutes.html')

def addoffers(request):
    return render(request,'admin/addoffers.html')

def parkingdetails(request):
    return render(request,'admin/parkingdetails.html')

def addcomplaints(request):
    return render(request,'customer/addcomplaints.html')
    
    
def staffupdate(request,id):
    sel=staff_reg.objects.get(id=id)
    return render(request,'admin/editstaff.html',{'res':sel})

def staffdelete(request,id):

	sel=staff_reg.objects.get(pk=id)
	sel.delete()
	return redirect(viewstaff)

    
def userticket(request,id):
    temp=request.session['sname']
    sel=userrequest.objects.get(id=id)
    user=routes.objects.all()
    return render(request,'staff/ticket.html',{'res':sel,'res2':user,'result':temp})

    
'''def viewticket(request):
    temp=request.session['uname']
    user=ticket.objects.filter(customerid=temp,status='pending')
    return render(request,'customer/viewticket.html',{'res2':user})'''

    
def stationupdate(request,id):
    sel=stations.objects.get(id=id)
    return render(request,'admin/editstation.html',{'res':sel})
    
    
def payment(request,id):
    sel=routes.objects.get(id=id)
  
    return render(request,'customer/payment.html',{'res':sel})



def slotpayment(request,id):
    sel=parkings.objects.get(id=id)
    temp=request.session['uname']
    a=sel.stationname
    b=sel.slot
    c=sel.rate
    x = int('1')
    y=int(b)
    d=y-x
    print(d)
    data=parkings(stationname=a,slot=d,rate=c,id=id)
    data.save()
    return render(request,'customer/slotpayment.html',{'res':sel,'result':temp})








def offerupdate(request,id):
    sel=offers.objects.get(id=id)
    return render(request,'admin/editoffer.html',{'res':sel})

def offerdelete(request,id):

	sel=offers.objects.get(pk=id)
	sel.delete()
	return redirect(viewoffer)



def trainupdate(request,id):
    sel=trains.objects.get(id=id)
    return render(request,'admin/edittrain.html',{'res':sel})



def traindelete(request,id):

	sel=trains.objects.get(pk=id)
	sel.delete()
	return redirect(viewtrain)

def routeupdate(request,id):
    sel=routes.objects.get(id=id)
    return render(request,'admin/editroute.html',{'res':sel})
    
def viewuserticket(request):
    temp=request.session['uname'] 
    sel=userpayment.objects.filter(customerid=temp)
    return render(request,'customer/viewuserticket.html',{'res':sel})


def routedelete(request,id):

	sel=routes.objects.get(pk=id)
	sel.delete()
	return redirect(viewroute)

####delete
def stationdelete(request,id):

	sel=stations.objects.get(pk=id)
	sel.delete()		
	return redirect(viewstation)



def editstation(request,id):
    context = {}
    if request.method == 'POST':
        p=request.POST['name']

        data = stations(stationname=p,id=id)

        data.save()

        return redirect(viewstation)

def editoffer(request,id):
    context = {}
    if request.method == 'POST':
        p=request.POST['evtnme']
        q=request.POST['off']

        data = offers(eventname=p,offer=q,id=id)

        data.save()

        return redirect(viewstation)



def editstaff(request,id):
    context = {}
    if request.method == 'POST':
        p=request.POST['name']
        i=request.POST['address']
        rt=request.POST['email']
        d=request.POST['phonenumber']
        dt=request.POST['gender']
        s=request.POST['designation']
        st=request.POST['password']

        myfile = request.FILES['image']
        print(myfile)
        fs = FileSystemStorage()
        name = fs.save(myfile.name, myfile)
        data = staff_reg(name=p,address=i,email=rt,phonenumber=d,gender=dt,designation=s,password=st,image=myfile,id=id)

        data.save()

        return redirect(viewstaff)

def edittrain(request,id):
    context = {}
    if request.method == 'POST':
        p=request.POST['no']
        i=request.POST['tname']
        d=request.POST['sname']
        dt=request.POST['time']

        myfile = request.FILES['image']
        print(myfile)
        fs = FileSystemStorage()
        name = fs.save(myfile.name, myfile)
        data = trains(trainno=p,trainname=i,stationname=d,traintime=dt,trainimage=myfile,id=id)

        data.save()

        return redirect(viewtrain)

def editroute(request,id):
    context={}
    if request.method=='POST':
        p=request.POST['tname']
        q=request.POST['sname']
        r=request.POST['ename']
        s= request.POST['distance']
        t= request.POST['rate']
        data=routes(trainname=p,startstation=q,endstation=r,distance=s,rate=t)
        data.save()
        return redirect(viewroute)



def cprofile(request):
    if request.session.has_key('uid'):
        temp=request.session['uid']
        users = customer_reg.objects.get(id=request.session['uid'])
        # us=[]
        # us['id']=user.id
        # email= user.email

        return render(request, 'customer/profile.html',{'res': users})
        
   

def sprofile(request):
    if request.session.has_key('sid'):
        temp=request.session['sid']
        users = staff_reg.objects.get(id=request.session['sid'])
        # us=[]
        # us['id']=user.id
        # email= user.email

        return render(request, 'staff/profile.html',{'res': users})
        
           
def addrequest(request):
    if request.method == 'POST':
        customerid = request.POST['customerid']
        sstation = request.POST['startstation']
        estation = request.POST['endstation']
        date = request.POST['date']
        
        user = userrequest(customerid=customerid,startstation=sstation,endstation=estation,date=date)

        user.save()


        return render(request, 'customer/request.html' )
        
        


def addticket(request):
    if request.method == 'POST':
        p=request.POST['customerid']
        i=request.POST['startstation']
        rt=request.POST['endstation']
        d=request.POST['date']
        dt=request.POST['distance']
        s=request.POST['rate']
        st=request.POST['trainno']
        u=request.POST['sid']
        v=request.POST['status']

       
        data = ticket(customerid=p,startstation=i,endstation=rt,date=d,distance=dt,rate=s,trainno=st,sid=u,status=v)

        data.save()

        return redirect(viewrequest)
        
        


def addslotpayment(request):
    if request.method == 'POST':
        p=request.POST['customerid']
        i=request.POST['startstation']
        rt=request.POST['endstation']
        d=request.POST['date']
        dt=request.POST['cardname']
        s=request.POST['rate']
        u=request.POST['cardnumber']
        w=request.POST['cardtype']

        data = userslotpayment(customerid=p,startstation=i,endstation=rt,date=d,cardname=dt,rate=s,cardnumber=u,cardtype=w)
        
        data.save()

        return redirect(viewslot)




















def addpayment(request):
    if request.method == 'POST':
        p=request.session['uname']
        i=request.POST['startstation']
        rt=request.POST['endstation']
        d=request.POST['date']
        dt=request.POST['cardname']
        s=request.POST['rate']
        st=request.POST['trainno']
        u=request.POST['cardnumber']
        w=request.POST['cardtype']
        sid=request.POST['sid']

       
        data = userpayment(customerid=p,startstation=i,endstation=rt,date=d,cardname=dt,rate=s,trainno=st,cardnumber=u,cardtype=w,sid=sid)

        data.save()

        return render(request,'customer/request.html')
        
        
def download(request,id):
    sel=userpayment.objects.get(id=id)
    return render(request,'customer/download.html',{'res':sel})
    