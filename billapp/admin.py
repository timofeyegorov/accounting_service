from django.contrib import admin
from .models import People, OperationType, OperationTag, Operation

# Register your models here.
admin.site.register(People)
admin.site.register(OperationType)
admin.site.register(OperationTag)
admin.site.register(Operation)