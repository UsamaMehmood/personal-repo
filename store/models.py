from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    seller = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    amount_paid = models.PositiveIntegerField()
    balance = models.PositiveIntegerField(editable=False)
    date_purchased = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return "{}, {}".format(self.name, self.quantity)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.balance = self.total_amount - self.amount_paid
        super().save(False, False, None, None)


class Fan(models.Model):
    name = models.CharField(max_length=50)
    design = models.CharField(max_length=100)
    seller = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    total_amount = models.PositiveIntegerField()
    amount_paid = models.PositiveIntegerField()
    balance = models.PositiveIntegerField(editable=False)
    date_purchased = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fans'

    def __str__(self):
        return "{}, {}".format(self.name, self.design)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.balance = self.total_amount - self.amount_paid
        super().save(False, False, None, None)
