from unicodedata import name
from django.urls import path
from miapp.views import FamiliaListView

urlpatterns = [
    path('', FamiliaListView.as_view()),
]