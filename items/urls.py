from django.urls import path
from . import views
from .views import itemCreateView, itemUpdateView, itemDeleteView

urlpatterns = [
    path('show', views.show),
	path('create', itemCreateView.as_view()),
	path('<pk>/update', itemUpdateView.as_view()),
	path('<pk>/delete/', itemDeleteView.as_view()), 
]