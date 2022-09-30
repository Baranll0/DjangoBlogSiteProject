from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name="post"

urlpatterns=[
    path("dashboard/",views.dashboard,name="dashboard"),
    path("",views.index,name="index"),
    path("addpost/",views.addpost,name="addpost"),
    path("post/<int:id>",views.detail,name="detail"),
    path("update/<int:id>", views.updatePost, name="update"),
    path("delete/<int:id>", views.deletePost, name="delete"),
    path('comment/<int:id>',views.addComment,name="comment"),


]
