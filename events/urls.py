from django.urls import path
from .views import event_list, event_detail, event_register, create_event, update_event, delete_event

urlpatterns = [
    path('', event_list, name='event_list'),
    path('<int:event_id>/', event_detail, name='event_detail'),
    path('<int:event_id>/register/', event_register, name='event_register'),
    path('create/', create_event, name='create_event'),
     path('event/update/<int:event_id>/', update_event, name='update_event'),
    path('event/delete/<int:event_id>/', delete_event, name='delete_event'),
    
]