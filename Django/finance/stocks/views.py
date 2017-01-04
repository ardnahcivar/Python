from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Stocks
from .serializer import StocksSerializer
# Create your views here.

class StockList(APIView):
    def get(self,request):
        stock = Stocks.objects.all()
        serializer = StocksSerializer(stock,many=True)
        return Response(serializer.data)

    def post(self):
        pass
