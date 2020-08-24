import json
from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from .models import Update

from .mixin import JsonResponseMixin

def json_example_view(request):
	"""
	Json - JS Object Notation
	"""

	data = {
		"counter": 100,
		"content": "This is information for Json"
	}
	# return JsonResponse(data)
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type='application/json')


class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data = {
		"counter": 100,
		"content": "This is information for Json"
		}
		return JsonResponse(data)


class JsonCBV2(JsonResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data = {
		"counter": 100,
		"content": "This is information for Json"
		}
		return JsonResponse(data)


class SerializeDetailView(View):
	# def get(self, request, *args, **kwargs):
	# 	obj = Update.objects.get(id=1)
	# 	data = serialize("json", [obj,], fields=('user', 'content'))
	# 	# data = {
	# 	# "user": obj.user.username,
	# 	# "content": obj.content
	# 	# }
	# 	json_data = data
	# 	return HttpResponse(json_data, content_type='application/json')

	def get(self, request, *args, **kwargs):
		obj = Update.objects.get(id=1)
		json_data = obj.serialize()
		return HttpResponse(json_data, content_type='application/json')

class SerializeListView(View):
	def get(self, request, *args, **kwargs):
		QS = Update.objects.all()
		json_data = QS.serialize()
		return HttpResponse(json_data, content_type='application/json')