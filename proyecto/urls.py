from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("pages/", views.PageListView.as_view(), name="pages_list"),
    path("pages/create/", views.PageCreateView.as_view(), name="page_create"),
    path("pages/<int:pk>/", views.PageDetailView.as_view(), name="page_detail"),
    path("pages/<int:pk>/edit/", views.PageUpdateView.as_view(), name="page_update"),
    path("pages/<int:pk>/delete/", views.PageDeleteView.as_view(), name="page_delete"),
]
