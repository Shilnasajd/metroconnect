"""metroconnect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.first,name='first'),
    path('customer', views.customer, name='customer'),
    path('addcustomer', views.addcustomer, name='addcustomer'),
    path('login', views.login, name='login'),
    path('logins', views.logins, name='logins'),
    path('logout', views.logout, name='logout'),
    path('addstaff', views.addstaff, name='addstaff'),
    path('staff',views.staff,name='staff'),
    path('addstations',views.addstations,name='addstations'),
    path('station',views.station,name='station'),
    path('addtrains',views.addtrains,name='addtrains'),
    path('train',views.train,name='train'),
    path('addroutes',views.addroutes,name='addroutes'),
    path('route', views.route, name='route'),
    path('addoffers',views.addoffers,name='addoffers'),
    path('offer', views.offer, name='offer'),
    path('parkingdetails', views.parkingdetails, name='parkingdetails'),
    path('parking', views.parking, name='parking'),
    path('viewstaff',views.viewstaff,name='viewstaff'),
    path('viewstation',views.viewstation,name='viewstation'),
    path('viewtrain', views.viewtrain, name='viewtrain'),
    path('viewoffer', views.viewoffer, name='viewoffer'),
    path('viewroute', views.viewroute, name='viewroute'),
    path('viewparking', views.viewparking, name='viewparking'),
    path('dash', views.dash, name='dash'),
    path('staffupdate/<int:id>', views.staffupdate, name='staffupdate'),
    path('staffupdate/editstaff/<int:id>', views.editstaff, name='editstaff'),
    path('staffdelete/<int:id>', views.staffdelete, name='staffdelete'),
    path('customerdash', views.customerdash, name='customerdash'),
    path('cprofile', views.cprofile, name='cprofile'),
    path('staffdash', views.staffdash, name='staffdash'),
    path('sprofile', views.sprofile, name='sprofile'),
    path('stationupdate/<int:id>', views.stationupdate, name='stationupdate'),
    path('stationupdate/editstation/<int:id>', views.editstation, name='editstation'),
    path('stationdelete/<int:id>', views.stationdelete, name='stationdelete'),
    path('trainupdate/<int:id>', views.trainupdate, name='trainupdate'),
    path('trainupdate/edittrain/<int:id>', views.edittrain, name='edittrain'),
    path('traindelete/<int:id>', views.traindelete, name='traindelete'),
    path('stationdelete/<int:id>', views.stationdelete, name='stationdelete'),
    path('routeupdate/<int:id>', views.routeupdate, name='routeupdate'),
    path('routeupdate/editroute/<int:id>', views.editroute, name='editroute'),
    path('routedelete/<int:id>', views.routedelete, name='routedelete'),
    path('offerupdate/<int:id>', views.offerupdate, name='offerupdate'),
    path('offerupdate/editoffer/<int:id>', views.editoffer, name='editoffer'),
    path('offerdelete/<int:id>', views.offerdelete, name='offerdelete'),
    path('addcomplaints',views.addcomplaints,name='addcomplaints'),
    path('ccomplaints',views.ccomplaints,name='ccomplaints'),
    path('viewcomplaint', views.viewcomplaint, name='viewcomplaint'),
    path('viewcomplaints', views.viewcomplaints, name='viewcomplaints'),
    path('request', views.request, name='request'),
    path('addrequest', views.addrequest, name='addrequest'),
    path('viewrequest', views.viewrequest, name='viewrequest'),
    path('userticket/<int:id>', views.userticket, name='userticket'),
    path('userticket/addticket', views.addticket, name='addticket'),
    path('payment/<int:id>', views.payment, name='payment'),
    path('payment/addpayment', views.addpayment, name='addpayment'),
    path('viewuserticket', views.viewuserticket, name='viewuserticket'),
    path('download/<int:id>', views.download, name='download'),
    path('viewslot', views.viewslot, name='viewslot'),
    path('slotpayment/<int:id>', views.slotpayment, name='slotpayment'),
    path('slotpayment/addslotpayment', views.addslotpayment, name='addslotpayment'),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

