from http.client import responses
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.serializers import Serializer
from .models import registration
from .serializers import registrationserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

@csrf_exempt
def registration_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        reg = registration.objects.all()
        serializer = registrationserializer(reg, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = registrationserializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)






# @api_view(['GET', 'POST'])
# def registration_list(request):

#     if request.method == 'GET':
#         items = registration.objects.all()
#         serializer = registrationserializer(items, many = True)
#         return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = registrationserializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
# def registration_detail(request,pk):
#     try:
#         reg_list = registration.object.get(pk=pk)
#     except registration.DoesNotExist:
#         return HttpResponse(status=400)

#     if request.method == 'GET':
#         serializer = registrationserializer(registration)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data =JSONParser().parse(request)
#         serializer = registrationserializer(reg_list,data=data)
#         if serializer.is_valid():
#             serializer.save
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         reg_list.delete()
#         return HttpResponse(status=204
#         )



