from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="items")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InventoryChangeLog(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='change_logs')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    old_quantity = models.IntegerField()
    new_quantity = models.IntegerField()
    change_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.item.name} changed from {self.old_quantity} to {self.new_quantity}"
