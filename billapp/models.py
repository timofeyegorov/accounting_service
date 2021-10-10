from django.db import models

# Create your models here.
class People(models.Model):
    # Id создается автоматически
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class OperationType(models.Model):
    name = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name

class OperationTag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Operation(models.Model):
    operation_sum = models.FloatField()
    people_name = models.ForeignKey(People, on_delete=models.CASCADE)
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE, default=1)
    operation_tag = models.ForeignKey(OperationTag, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)