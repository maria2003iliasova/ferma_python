from django.urls import path, include
from .views import *

urlpatterns = [
    path('editUser/<int:id>/', editUser),
    path('deleteUser/<int:id>/', deleteUser),
    
    path('editArticles/<int:id>/', editArticles),
    path('deleteArticles/<int:id>/', deleteArticles),
    
    path('editBron/<int:id>/', editBron),
    path('deleteBron/<int:id>/', deleteBron),
    path('', bron),
]
