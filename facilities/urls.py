from django.urls import path
from .views import facility_list, facility_booking, create_facility, update_facility, delete_facility


urlpatterns = [

    path('', facility_list, name='facility_list'),
    path('create/', create_facility, name='create_facility'),
    path('<int:facility_id>/booking/', facility_booking, name='facility_booking'),
    path('<int:facility_id>/update/', update_facility, name='update_facility'),  # URL for updating facility
    path('<int:facility_id>/delete/', delete_facility, name='delete_facility'),  # URL for deleting facility
]



# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.facility_list, name='facility_list'),
#     # path('<int:facility_id>/', views.facility_detail, name='facility_detail'),
#    path('book/<int:facility_id>/', views.book_facility, name='book_facility'),
#     path('create/', views.create_facility, name='create_facility'),
#     path('facilities/<int:facility_id>/booking/', views.facility_booking, name='facility_booking'),
# ]