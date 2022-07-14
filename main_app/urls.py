from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # route for cats index
    path('cats/', views.cats_index, name='index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'), 
    # Class-based view: new route used to show a form a create a cat
    path('cats/create/', views.CatCreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),
    path('cats/<int:cat_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    # pk stands for 'primary key'
    # associate a toy with a cat (M:M)
    path('cats/<int:cat_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    # # remove associate a toy with a cat
    path('cats/<int:cat_id>/delete_toy/<int:toy_id>/', views.delete_toy, name='delete_toy'),
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
]
