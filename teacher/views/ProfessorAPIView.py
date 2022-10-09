from teacher.views import *
from teacher.models import Professor
from teacher.serializers import ProfessorSerializer

class ProfessorAPIView(APIView):
    def get(self, request, format=None):
        professores = Professor.objects.all()
        serializer = ProfessorSerializer(professores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)