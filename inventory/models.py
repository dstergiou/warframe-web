from django.db import models


class Item(models.Model):
    CHOICES = (
        ('S', 'Standard Item'),
        ('P', 'Prime Item'),
        ('M', 'Mod'),
    )
    name = models.CharField(max_length=100, blank=False, null=False)
    url_name = models.CharField(max_length=100, blank=False, null=False)
    item_id = models.CharField(max_length=100, blank=True, null=False, default='__REPLACE__')
    type = models.CharField(max_length=1, choices=CHOICES, blank=False, null=False)
    quantity = models.PositiveIntegerField(default=0, blank=False, null=False)
    ducats = models.PositiveIntegerField(blank=True, null=True, default=0)
    rank = models.PositiveIntegerField(blank=True, null=True, default=0)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
