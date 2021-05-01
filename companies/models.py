from django.db import models


class Companies(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    company_id = models.CharField(max_length=50, blank=True, null=True)
    bank_number = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Payment(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, blank=True, null=True)
    bank_paper_id = models.IntegerField(null=True, blank=True)
    payment_date = models.CharField(max_length=100, null=True, blank=True)
    paid = models.FloatField(default=0, null=True, blank=True)
    need_to_pay = models.FloatField(default=0, null=True, blank=True)
    notes = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        ordering = ['bank_paper_id']
