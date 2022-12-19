from django.db import models
from django.urls import reverse_lazy


class Province(models.Model):
    province = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.province

class Opportunity(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    province = models.ForeignKey("Province", on_delete=models.PROTECT, blank=True, null=True)
    postal_code = models.CharField(max_length=8, blank=True, null=True)
    phone_number1 = models.CharField(max_length=20, blank=True, null=True)
    phone_number2 = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=30)
    sin = models.CharField(max_length=30, blank=True, null=True)
    dob = models.DateField()
    agent = models.CharField(max_length=30, blank=True, null=True)
    collection_amount = models.FloatField(blank=True, null=True)
    collection_date = models.DateField(blank=True, null=True)
    last_agent = models.CharField(max_length=30, blank=True, null=True)
    last_crawl = models.DateTimeField(blank=True, null=True)
    last_result = models.CharField(max_length=30, blank=True, null=True)
    prioritize_local = models.BooleanField(blank=True, null=True)
    prioritize_global = models.BooleanField(blank=True, null=True)
    file_upload = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name

    def get_absolute_url(self):
        return reverse_lazy("main:opportunity_update", kwargs={"pk": self.id})
