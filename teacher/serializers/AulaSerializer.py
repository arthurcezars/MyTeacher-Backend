from teacher.serializers import *
from teacher.models import Aula
from django.forms import ValidationError

class CadastrarAulaSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    nome = serializers.CharField(max_length=100)

    def validate_nome(self, value):
        if len(value) < 3:
            raise ValidationError("deve ter pelo menos três caracteres")
        return value

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = '__all__'