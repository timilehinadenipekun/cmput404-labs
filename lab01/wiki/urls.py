from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("save/", views.savePage, name="save"),
    path("add/", views.editor, name="add"),
    path("page/<int:id>/", views.view_page, name="view"),
    path("page/<int:id>/like/", views.like_page, name="like")

]
