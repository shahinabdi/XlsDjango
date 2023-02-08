from import_export import resources
from .models import MetaData, Data


class MetaDataResource(resources.ModelResource):
    class Meta:
        model = MetaData

class DataResource(resources.ModelResource):
    class Meta:
        model = Data