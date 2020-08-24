from django.urls import path

from .views import (
		json_example_view, 
		JsonCBV, 
		JsonCBV2, 
		SerializeListView,
		SerializeDetailView
	)

# app_name = update
urlpatterns = [
    path('demo/', json_example_view, name='demo'),
    path('update/jsoncbv/', JsonCBV.as_view(), name='jsoncbv'),
    path('update/jsoncbv2/', JsonCBV2.as_view(), name='jsoncbv2'),
    path('update/serialized/list/', SerializeListView.as_view(), name='serializedlist'),
    path('update/serialized/detail/', SerializeDetailView.as_view(), name='serializeddetail'),
]