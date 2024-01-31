from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from user.models import  CustomUser
from rest_framework.permissions import IsAuthenticated
from .serializers import SavedPasswordSerializer
  # Import the serializer for your User model
from .models import SavePassword
@api_view(['POST'])
def save_password(request):
    print("here",request.data)
    user = request.data.get("userid")
    print("here%%%%%%%%%%%%%%%%%%",user)
    password=request.data.get("password")
    platform=request.data.get("field")
    users=CustomUser.objects.get(username=user)
    print(type(users.id))
    saves=SavePassword.objects.create(user=users,
                                     password=password,platform=platform)
    saves.save()
    return Response({"msg": "Saved successfully"})
    

@api_view(['POST'])
def saved_passwords(request):
    try:
        token = request.data.get('token')
        saved_password_object = SavePassword.objects.filter(user=token)
        print(saved_password_object)
        for i in saved_password_object:
            print(i.password)
    
        serializer = SavedPasswordSerializer(saved_password_object,many=True)
        print(serializer.data)
        
        
        return Response(serializer.data)
    
    except SavePassword.DoesNotExist:

        return Response({"msg": "SavePassword object not found"}, status=404)
    
    except Exception as e:
    
        return Response({"msg": str(e)}, status=500)
@api_view(['DELETE'])

def delete_password(request, id):
    pass
