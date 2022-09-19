from django.urls import path
import car.views

urlpatterns = [
  path('adminhome/',car.views.adminhome,name='adminhome'),
  path('addService/',car.views.addService,name='addService'),
  path('updateService/',car.views.updateService,name='updateService'),
  path('latestorders',car.views.latestorders,name='latestorders'),
  path('enableusers',car.views.enableusers,name='enableusers'),
  path('enableUser/<int:id>',car.views.enableUser,name='enableUser'),
  path('viewusers',car.views.viewusers,name='viewusers'),
  path('deleteservice/<id>', car.views.deleteservice, name='deleteservice'),

]
