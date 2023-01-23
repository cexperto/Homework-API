from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
import requests
from movies.permissions import UserOrReadOnly


@api_view(["POST", "GET"])
@permission_classes([UserOrReadOnly])
def random_number(request):
    if request.method == "POST":
        n1 = request.data["numberone"]
        n2 = request.data["numbertwo"]
        if n1 == 0:
            n1 = 1
        if n1 and n2 and n1 < n2:
            url = f"https://www.randomnumberapi.com/api/v1.0/random?min={n1}&max={n2}&count=1"
            r = requests.get(url)
            return Response({"number": r})
        return Response({"error": "numbertwo must be > numberone"})
    url = f"https://www.randomnumberapi.com/api/v1.0/random?min=1&max=100&count=1"
    r = requests.get(url)
    return Response({"number": r})



