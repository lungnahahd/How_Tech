# viewsets : 자주 사용하는 공통적인 view 로직을 그룹화 한 것
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WonderSerializer
from .models import Wonder
from rest_framework.decorators import api_view

@api_view(['GET'])
def store_list(request):
    stores = Wonder.objects.all()




# class WonderViewSet(viewsets.ModelViewSet):
#     queryset = Wonder.objects.all()
#     serializer_class = WonderSerializer