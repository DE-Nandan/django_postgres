from django.db import models

class Organization(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    TYPE_CHOICES = [
        ('perishable', 'Perishable'),
        ('non_perishable', 'Non-Perishable'),
    ]

    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Zone(models.Model):
    zone = models.CharField(max_length=100)
    fix_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.zone

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    base_distance_in_km = models.PositiveIntegerField()
    km_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.organization} - {self.item} - {self.zone}"
