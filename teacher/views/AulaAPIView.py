from teacher.views import *
from teacher.models import Aula, Professor
from teacher.serializers import CadastrarAulaSerializer, AulaSerializer
from django.shortcuts import get_object_or_404

class CadastrarAulaAPIView(APIView):
    def post(self, request, id_professor, format=None):
        professor = get_object_or_404(Professor, id=id_professor)
        serializer = CadastrarAulaSerializer(data=request.data)
        if serializer.is_valid():
            aula = Aula(
                nome=serializer.validated_data.get('nome'),
                email=serializer.validated_data.get('email'),
                professor=professor
            )
            aula.save()
            aula_serializer = AulaSerializer(aula, many=False)
            return Response(aula_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                {
                    "message": "Houveram erros de validação",
                    "erros": serializer.errors
                }, 
                status=status.HTTP_400_BAD_REQUEST
            )