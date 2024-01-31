from rest_framework.response import Response
from .serializers import registerserializers,UserLoginSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def Register(request):
    serializer=registerserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "user register sucessfully"},status=status.HTTP_200_OK)
    else:
        print(serializer.errors)
@api_view(['POST'])
def login(request):
    serializer = UserLoginSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access_token": str(refresh.access_token),
                "message": "User logged in successfully",
                "user_id": user.id,
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)