from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("detail/<int:id>/",views.detail,name="detail"),
    path("add/",views.create_item,name="create_name"),
    path("update/<int:id>/",views.update_item,name="update_item"),
    path("delete/<int:id>/",views.delete_item,name="delete_item"),
]