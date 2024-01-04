from django.shortcuts import render
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
# Create your views here
from rest_framework.viewsets import ModelViewSet
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
class Movies(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [SessionAuthentication]
    filter_backends = [OrderingFilter]
    ordering_fields = ['name']
    pagination_class = PageNumberPagination

# class Movies(APIView):
    
#     def get(self,request,id = None,format = None):
#         if request.GET.get("year") is not None:
#             year = request.GET.get("year")
#             movies = Movie.objects.filter(year__gte = year)
#         else:
#             movies = Movie.objects.all()
#         serialized = MovieSerializer(movies,many=True)
#         return JsonResponse(serialized.data,safe=False)
    
#     def post(self,request):
#         data = request.data
#         serialized = MovieSerializer(data = data)
#         if serialized.is_valid():
#             serialized.save()
#             return JsonResponse({"message":"Movie saved Successfully"})
#         return JsonResponse(serialized.errors,status = 400)
    
#     def put(Self,request):
#         data = request.data
#         movie = Movie.objects.get(pk = data["id"])
#         serialized = MovieSerializer(movie,data = data,partial = True)
#         if serialized.is_valid():
#             serialized.save()
#             return JsonResponse({"message":"Movie saved Successfully"},status = 201)
#         return JsonResponse(serialized.errors)
