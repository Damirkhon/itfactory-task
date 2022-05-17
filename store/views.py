from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Store, Employee
from .serializers import StoreSerializer, VisitSerializer


@api_view(["GET"])
def store_list(request):
    phone_num = request.GET["phone"]
    print(phone_num)
    stores = Store.objects.filter(employee__phone=phone_num)
    serializer = StoreSerializer(stores, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_visit(request):
    user = get_object_or_404(Employee, phone=request.data["phone"])
    store = get_object_or_404(Store, pk=request.data["store"])
    if user == store.employee:
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"VisitID": serializer.data["id"], "Time": serializer.data["time"]}
            )
        else:
            return Response(serializer.errors)
    else:
        return Response(
            {"error": "Store and user not matching"}, status=status.HTTP_400_BAD_REQUEST
        )
