from django.urls import path

from boardapp.views import BoardList, BoardDetail
from preachapp.views import weekly_preaching_list, weekly_preaching_detail, intro_images

app_name = "boardapp"

urlpatterns = [
    path('intro/', intro_images, name='intro'),
    path('listing_board/', BoardList, name='board_list'),
    path('detail_board/<int:pk>/', BoardDetail, name='board_detail'),
]