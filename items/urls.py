from django.urls import path
from . import views
from .views import itemUpdateView

urlpatterns = [
    path('show', views.show),
    path('item', views.item),
#    path('edit/<int:id>', views.edit),
#    path('update/<int:id>', views.update),
#    path('delete/<int:id>', views.destroy),
	path('<pk>/update', itemUpdateView.as_view())
]