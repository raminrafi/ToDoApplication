from django.shortcuts import render

# Create your views here.
from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from .serializers import registrationserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@csrf_exempt
def task_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg = task.objects.all()
        serializer = taskserializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = taskserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)



