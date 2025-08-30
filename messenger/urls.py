# messenger/urls.py
from django.urls import path
from .views import InboxView, ComposeView, MessageDetailView

urlpatterns = [
    path('', InboxView.as_view(), name='inbox'),
    path('compose/', ComposeView.as_view(), name='compose'),
    path('<int:pk>/', MessageDetailView.as_view(), name='message_detail'),
]
