from rest_framework import viewsets, permissions
from .models import InventoryItem, Category, InventoryChangeLog
from .serializers import InventoryItemSerializer, CategorySerializer, InventoryChangeLogSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User

class InventoryItemViewSet(viewsets.ModelViewSet):
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InventoryItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        old_item = self.get_object()
        old_quantity = old_item.quantity
        new_item = serializer.save()
        if old_quantity != new_item.quantity:
            InventoryChangeLog.objects.create(
                item=new_item,
                changed_by=self.request.user,
                old_quantity=old_quantity,
                new_quantity=new_item.quantity
            )

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class InventoryChangeLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventoryChangeLog.objects.all()
    serializer_class = InventoryChangeLogSerializer
