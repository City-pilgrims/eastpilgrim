from django.urls import path

from preachapp.views import weekly_preaching_list, weekly_preaching_detail, intro_images

app_name = "preachapp"

urlpatterns = [
    path('intro/', intro_images, name='intro'),
    path('listing_preach/', weekly_preaching_list, name='weekly_preaching_list'),
    path('detail_preach/<int:pk>/', weekly_preaching_detail, name='weekly_preaching_detail'),
]