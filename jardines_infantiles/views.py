from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import JardinesInfantilesSerializer
from .models import JardinesInfantiles
from django.db import transaction

class JardinesInfantilesListCreateView(APIView):
    def get(self, request):
        queryset = JardinesInfantiles.objects.all()
        serializer = JardinesInfantilesSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:

            with transaction.atomic():
                serializer = JardinesInfantilesSerializer(data=request.data)
                
                if serializer.is_valid():
                    instance = serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error al crear el jardín: {e}")
            return Response({"error": "Error interno del servidor"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
