from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StockSerializer
from  .models import Stock

class StockList(APIView):
    def get(self,request):
        stock = Stock.objects.all()
        serializer = StockSerializer(stock,many=True)
        return Response(serializer.data)

    def post(self):
        pass
