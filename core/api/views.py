from rest_framework.response import Response
from rest_framework.decorators import api_view
#local import
from .serializer import ItemSerializer
from core.models import Item

@api_view(['GET'])
def itemApi(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def itemDetailApi(request,pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item,many=False)
    return Response(serializer.data)

