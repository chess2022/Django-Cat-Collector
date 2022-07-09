from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
      # route for cats index
    path('cats/', views.cats_index, name='index'),
    # path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    # # new route used to show a form a create a cat
    # path('cats/create/', views.CatCreate.as_view(), name='cats_create')
]
