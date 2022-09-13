from django.urls import path
from .views import TodoViews

urlpatterns = [
    path('', TodoViews.as_view()),
    path('<int:id>', TodoViews.as_view())
]