from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import MetaData, Data
from django.utils.datastructures import MultiValueDictKeyError
import openpyxl
from tablib import Dataset
from .resource import DataResource, MetaDataResource
# Create your views here.


def Import_Excel_pandas(request):
    if request.method == 'POST' and request.FILES['file']:
        xlsfile  = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(xlsfile.name, xlsfile)
        uploaded_file_url = fs.url(filename)
        empexceldata = pd.read_excel(filename, sheet_name='MetaData')
        
        for dbframe in empexceldata.itertuples():
            print(dbframe)
            obj = MetaData.objects.create(NameGroup=dbframe.NameGroup,
                                            Project = dbframe.Project,
                                            SiteName = dbframe.Site,
                                            Country = dbframe.Country,
                                            Town = dbframe.Town,
                                            Code_INSEE = dbframe.Code_INSEE,
                                            GNIP_Code = dbframe.GNIP_Code,
                                            Latitude = dbframe.Latitude,
                                            Longitude = dbframe.Longitude,
                                            Altitude = dbframe.Altitude, 
                                            Unit_Altitude = dbframe.Unit_Altitude,
                                            Type_of_Site = dbframe.Type_of_Site,
                                            Source_of_Information = dbframe.Source_of_Information,
                                            BV_INSPIRE = dbframe.BV_INSPIRE,
                                            FG_INSPIRE = "",
                                            SNO_RENOIR = dbframe.SNO_RENOIR,
                                            Link_to_National = dbframe.Link_to_National,
                                            Laboratory_Name = dbframe.Laboratory_Name,
                                            First_Organism_Name = dbframe.First_Organism_Name,
                                            Second_Organism_Name = dbframe.Second_Organism_Name,
                                            Third_Organism_Name = dbframe.Third_Organism_Name,
                                            Code = dbframe.Code,
                                            Contact = dbframe.Contact,
                                            Home_Base_Affilate_OSU = dbframe.Home_base_Affiliate_OSU,
                                            Associated_OSU = dbframe.Associated_OSU)
            obj.save()
        return render(request, 'index.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'index.html', {})

def Import_Excel(request):
    if request.method == 'POST':
        MetaData = MetaDataResource()
        Data = DataResource()
        dataset = Dataset()
        new_metadata = request.FILES['file']
        data_import = dataset.load(new_metadata.read())
        result_MetaData = MetaData.import_data(dataset=dataset, dry_run=True)
        result_Data = Data.import_data(dataset=dataset, dry_run=True)

        if not result_MetaData.has_errors():
            MetaData.import_data(dataset=dataset, dry_run=False)

    return render(request, 'index.html',{})

