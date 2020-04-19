from django.contrib import admin

# Register your models here.
from .models import Produto, Cliente, Mini

admin.site.register(Produto)
admin.site.register(Cliente)
admin.site.register(Mini)

