from django.urls import path, include
from .views import *

urlpatterns = [
    path('createUser/', createUser),
    path('editUser/<int:id>/', editUser),
    path('deleteUser/<int:id>/', deleteUser),
    
    path('createArticles/', createArticles),
    path('editArticles/<int:id>/', editArticles),
    path('deleteArticles/<int:id>/', deleteArticles),
    
    path('createComments/', createComments),
    path('editComments/<int:id>/', editComments),
    path('deleteComments/<int:id>/', deleteComments),
    
    path('editBron/<int:id>/', editBron),
    path('deleteBron/<int:id>/', deleteBron),
    path('createBron/', createBron),
    
    path('', account),
]
