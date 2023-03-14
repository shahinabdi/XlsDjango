from import_export import resources
from .models import MetaData, Data
from django.utils.translation import ugettext_lazy as _


class MetaDataResource(resources.ModelResource):
    class Meta:
        model = MetaData

class DataResource(resources.ModelResource):
    class Meta:
        model = Data