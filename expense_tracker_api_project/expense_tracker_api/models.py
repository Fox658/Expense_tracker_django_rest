import uuid
from django.db import models

class Category(models.Model):
    category_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    category_name = models.CharField(max_length=255, null=True)
    date_modified = models.DateField(null=True)
    date_created = models.DateField(null=True)
    #created_by

class Expense(models.Model):
    expense_id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    amount = models.FloatField(null=True)
    description = models.CharField(max_length=255, null=True)
    date_modified = models.DateField(null=True)
    date_created = models.DateField(null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="expenses"
    )
    #created_by
