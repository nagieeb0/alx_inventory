from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, CategoryViewSet, InventoryChangeLogViewSet

router = DefaultRouter()
router.register(r'inventory_management', InventoryItemViewSet, basename='inventory')
router.register(r'categories', CategoryViewSet)
router.register(r'logs', InventoryChangeLogViewSet)

urlpatterns = router.urls
