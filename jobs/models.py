from django.db import models

class Cost(models.Model):
    costModel = models.DecimalField(max_digits=8, decimal_places=0)
    dateModel = models.DateField()
    incomeModel = models.DecimalField(max_digits=8, decimal_places=0, default=0)

    def profitModel(self):
        return self.incomeModel - self.costModel
