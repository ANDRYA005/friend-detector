from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from telegram_hook.serializers import PersonSerializer
from telegram_hook.models import Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    @action(methods=['get'], detail=False)
    def get_staged(self, request):
        staged_person = self.queryset.order_by("-id")[0]
        serializer = self.get_serializer(staged_person)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
