from django.urls import path
from .views import SiteListView, SiteDetailView, ContactMailView


urlpatterns = [
    path('list/', SiteListView.as_view(), name='list'),
    path('detail/<int:site_id>/', SiteDetailView.as_view(), name='detail' ),
    path('contact/send_mail/', ContactMailView.as_view(), name='send_mail_view'),
    
]
