from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def get_items(request):
    """Return all items or filter items based on query parameter."""
    search_query = request.GET.get('search', None)
    items = Item.objects.all()
    
    if search_query:
        items = items.filter(name__icontains=search_query)

    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_item(request):
    """Add a new item."""
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_item(request, item_id):
    """Return a single item."""
    item = get_object_or_404(Item, id=item_id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

@api_view(['PUT'])
def update_item(request, item_id):
    """Update an item."""
    item = get_object_or_404(Item, id=item_id)
    serializer = ItemSerializer(item, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_item(request, item_id):
    """Delete an item."""
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
