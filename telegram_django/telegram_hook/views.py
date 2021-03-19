from django.shortcuts import render
from django.http import HttpResponse, Http404

from rest_framework import status, viewsets
from rest_framework.decorators import api_view

from telegram_hook.serializers import PersonSerializer
from telegram_hook.models import Person

from rest_framework.views import APIView
from rest_framework.response import Response


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer


# class PersonDetail(APIView):
#     """
#     Retrieve, update or delete a Person instance.
#     """
#     def get_object(self, name):
#         try:
#             return Person.objects.get(name=name)
#         except Person.DoesNotExist:
#             raise Http404

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def get(self, request, name, format=None):
#         person = self.get_object(name)
#         serializer = PersonSerializer(person)
#         return Response(serializer.data)

@api_view(['POST'])
def set_staged_name(request):
    person_to_stage_serializer = PersonSerializer(data=request.data)
    if not person_to_stage_serializer.is_valid():
        return Response(person_to_stage_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    person_to_stage_serializer.save()
    return Response(person_to_stage_serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_staged_name(request):
    staged_person = Person.objects.latest('id')
    serializer = PersonSerializer(staged_person)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def set_name(request, name: str):

#     return HttpResponse(f"Hello {name}")

# def get_name(request, name: str):
    
#     return HttpResponse(f"Hello {name}")