from import_export import resources
from .models import Data, MetaData


class MetaDataResource(resources.ModelResource):
    class Meta:
        model = MetaData

class DataResource(resources.ModelResource):
    class Meta:
        model = Data