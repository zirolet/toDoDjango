from django.urls import path
from .views import *

urlpatterns = [
    #path('', myList.as_view(), name='index'),
    path('',  myList, name='index'),
    path('<int:entry_id>/', detail, name='detail'),
    path('create/', creation, name='creation'),
    path('accountCreation/', accountCreation, name='accountCreation'),
    path('logout/', logoutView, name='logout'),
    path('delete/<int:entry_id>/', deleteEntryView, name='delete')
]