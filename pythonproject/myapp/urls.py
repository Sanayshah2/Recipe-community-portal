from django.urls import path
from . import views

urlpatterns = [
    
    
    path("recipes/<cname>/<int:myid>/<recipename>/", views.foodview, name="foodview"),
    #path("addcategory/<profilename>/", views.addcategory, name="addcategory"),
    path("recipes/", views.recipes, name="recipes"),
    path("<profilename>/foodentrykaro/", views.foodform, name="foodform"),
    path("recipes/<int:cid>/<cname>/", views.categoryview, name="categoryview"),  
    path("", views.home, name="home"),  
    path("signup/",views.signup,name="signup"),  
    path("comment/<cname>/<int:myid>/<recipename>/",views.addComment,name = "comment"),
    path('recipes/<cname>/<int:myid>/<recipename>/edit/', views.updaterecipe, name='updaterecipe'),
    path('recipes/<cname>/<recipename>/delete/<int:myid>/<int:profileid>/<profilename>/', views.deleterecipe, name='deleterecipe'),
    
    
]