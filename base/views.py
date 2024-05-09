from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class Home(APIView):
    permission_classes = [IsAuthenticated]
    def initial(self, request, *args, **kwargs):
        return super().initial(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return Response({"message": "get response"},status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        return Response({"message": "post response"},status=status.HTTP_201_CREATED)
    

def exeption_view(request):
    # raise Exception("this is an exception")
    1000/0
