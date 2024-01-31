
from rest_framework import serializers
from .models import SavePassword
class PasswordGeneratorSerializer(serializers.Serializer):
    length = serializers.IntegerField(min_value=1, max_value=50, required=True)
    include_uppercase = serializers.BooleanField(default=True)
    include_lowercase = serializers.BooleanField(default=True)
    include_special_chars = serializers.BooleanField(default=False)
    include_numbers = serializers.BooleanField(default=True)
class SavedPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavePassword
        fields = "__all__"