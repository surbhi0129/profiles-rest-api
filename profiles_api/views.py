from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """Test api view"""
    def get(self, request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methods as function(get, post, patch,delete)'
        'Is similar to traditonal django view'
        'Gives you most control over the application logic'
        'Is mapped manually to urls',

        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
