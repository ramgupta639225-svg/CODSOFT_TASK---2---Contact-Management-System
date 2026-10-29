from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, filters
from .models import Contact
from .serializers import ContactSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import ContactPagination




class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter,
                       filters.OrderingFilter)

    search_fields = ('name','email', 'phone')
    ordering_fields = ('name','email', 'phone', 'company')
    filterset_fields = ('name','email', 'phone', 'company')
    pagination_class = ContactPagination

