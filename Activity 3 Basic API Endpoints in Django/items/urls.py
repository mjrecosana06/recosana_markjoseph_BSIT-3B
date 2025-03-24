from django.urls import path
from .views import get_items, add_item, get_item, update_item, delete_item

urlpatterns = [
    path('items/', get_items, name='get_items'),
    path('items/add/', add_item, name='add_item'),
    path('items/<int:item_id>/', get_item, name='get_item'),
    path('items/<int:item_id>/update/', update_item, name='update_item'),
    path('items/<int:item_id>/delete/', delete_item, name='delete_item'),
]