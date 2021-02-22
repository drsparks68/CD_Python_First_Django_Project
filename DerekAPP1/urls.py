from django.urls import path
from . import views	# the . indicates that the views file can be found in the same directory as this file
                    
urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<int:num>', views.show),
    path('<int:num>/edit', views.edit),
    path('<int:num>/delete', views.destroy),
]