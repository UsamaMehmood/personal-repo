from django.conf.urls import url
from store import views

urlpatterns = [
    url(r'^items/$', views.ItemsList.as_view(), name='items'),
    url(r'^fans/$', views.FansList.as_view(), name='fans'),
    url(r'^add_item/$', views.AddItem.as_view(), name='add_item'),
    url(r'^add_fan/$', views.AddFan.as_view(), name='add_fan'),
    url(r'^update_item/(?P<pk>\d+)/$', views.UpdateItem.as_view(), name='update_item'),
    url(r'^update_fan/(?P<pk>\d+)/$', views.UpdateFan.as_view(), name='update_fan'),
    url(r'^delete/(?P<pk>\d+)/$', views.ItemDelete.as_view(), name='delete_item'),
    url(r'^delete_fan/(?P<pk>\d+)/$', views.FanDelete.as_view(), name='delete_fan')
]