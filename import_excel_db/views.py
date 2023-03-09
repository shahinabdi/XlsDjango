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


def verify_pandas(request):
    pass


def Import_Excel_pandas(request):
    if request.method == 'POST' and request.FILES['file']:
        xlsfile = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(xlsfile.name, xlsfile)
        uploaded_file_url = fs.url(filename)
        xlsmetadata = pd.read_excel(filename, sheet_name='MetaData')
        xlsdata = pd.read_excel(filename, sheet_name='Data')
        updated_site = ""
        for dbframe in xlsmetadata.itertuples():
            NameGroup = dbframe[1]
            Project = dbframe[2]
            SiteName = dbframe[3]
            Country = dbframe[4]
            Town = dbframe[5]
            Code_INSEE = dbframe[6]
            GNIP_Code = dbframe[7]
            Latitude = dbframe[8]
            Longitude = dbframe[9]
            Altitude = dbframe[10]
            Unit_Altitude = dbframe[11]
            Type_of_Site = dbframe[12]
            Source_of_Information = dbframe[13]
            BV_INSPIRE = dbframe[14]
            FG_INSPIRE = dbframe[15]
            SNO_RENOIR = dbframe[16]
            Link_to_National = dbframe[17]
            Laboratory_Name = dbframe[18]
            First_Organism_Name = dbframe[19]
            Second_Organism_Name = dbframe[20]
            Third_Organism_Name = dbframe[21]
            Code = dbframe[22]
            Contact = dbframe[23]
            Home_Base_Affilate_OSU = dbframe[24]
            Associated_OSU = dbframe[25]
            try:
                metadataobj = MetaData.objects.get(SiteName=SiteName)
                # If object exists, update it
                metadataobj.NameGroup = NameGroup
                metadataobj.Project = Project
                metadataobj.Country = Country
                metadataobj.Town = Town
                metadataobj.Code_INSEE = Code_INSEE
                metadataobj.GNIP_Code = GNIP_Code
                metadataobj.Latitude = Latitude
                metadataobj.Longitude = Longitude
                metadataobj.Altitude = Altitude
                metadataobj.Unit_Altitude = Unit_Altitude
                metadataobj.Type_of_Site = Type_of_Site
                metadataobj.Source_of_Information = Source_of_Information
                metadataobj.BV_INSPIRE = BV_INSPIRE
                metadataobj.FG_INSPIRE = FG_INSPIRE
                metadataobj.SNO_RENOIR = SNO_RENOIR
                metadataobj.Link_to_National = Link_to_National
                metadataobj.Laboratory_Name = Laboratory_Name
                metadataobj.First_Organism_Name = First_Organism_Name
                metadataobj.Second_Organism_Name = Second_Organism_Name
                metadataobj.Third_Organism_Name = Third_Organism_Name
                metadataobj.Code = Code
                metadataobj.Contact = Contact
                metadataobj.Home_Base_Affilate_OSU = Home_Base_Affilate_OSU
                metadataobj.Associated_OSU = Associated_OSU

                metadataobj.save()
                updated_site = SiteName
            except MetaData.DoesNotExist:
                # If object doesn't exist, create it
                metadataobj = MetaData(NameGroup=NameGroup, Project=Project, SiteName=SiteName,
                                       Country=Country,
                                       Town=Town,
                                       Code_INSEE=Code_INSEE,
                                       GNIP_Code=GNIP_Code,
                                       Latitude=Latitude,
                                       Longitude=Longitude,
                                       Altitude=Altitude,
                                       Unit_Altitude=Unit_Altitude,
                                       Type_of_Site=Type_of_Site,
                                       Source_of_Information=Source_of_Information,
                                       BV_INSPIRE=BV_INSPIRE,
                                       FG_INSPIRE=FG_INSPIRE,
                                       SNO_RENOIR=SNO_RENOIR,
                                       Link_to_National=Link_to_National,
                                       Laboratory_Name=Laboratory_Name,
                                       First_Organism_Name=First_Organism_Name,
                                       Second_Organism_Name=Second_Organism_Name,
                                       Third_Organism_Name=Third_Organism_Name,
                                       Code=Code,
                                       Contact=Contact,
                                       Home_Base_Affilate_OSU=Home_Base_Affilate_OSU,
                                       Associated_OSU=Associated_OSU)
                metadataobj.save()
        # for dbframe in xlsdata.itertuples():
        #     dataobj = Data.objects.create(Sample_Name=dbframe[1],
        #                                   Media_Type=dbframe[2],
        #                                   Type_of_Rain_Collector=dbframe[3],
        #                                   Date=dbframe[4],
        #                                   Begin_of_Period=dbframe[5],
        #                                   End_of_Period=dbframe[6],
        #                                   O18=dbframe[7],
        #                                   O18_Unit=dbframe[8],
        #                                   O18_Error=dbframe[9],
        #                                   O18_Error_Unit=dbframe[10],
        #                                   O18_Provider=dbframe[11],
        #                                   O18_Measure_Equipement=dbframe[12],
        #                                   H2=dbframe[13],
        #                                   H2_Unit=dbframe[14],
        #                                   H2_Error=dbframe[15],
        #                                   H2_Error_Unit=dbframe[16],
        #                                   H2_Provider=dbframe[17],
        #                                   H2_Measure_Equipement=dbframe[18],
        #                                   H3=dbframe[19],
        #                                   H3_Unit=dbframe[20],
        #                                   H3_Error=dbframe[21],
        #                                   H3_Error_Unit=dbframe[22],
        #                                   H3_Provider=dbframe[23],
        #                                   H3_Measure_Equipement=dbframe[24],
        #                                   O17=dbframe[25],
        #                                   O17_Unit=dbframe[26],
        #                                   O17_Error=dbframe[27],
        #                                   O17_Error_Unit=dbframe[28],
        #                                   O17_Provider=dbframe[29],
        #                                   O17_Measure_Equipement=dbframe[30],
        #                                   Percipitation_Amount=dbframe[31],
        #                                   Percipitation_Amount_Unit=dbframe[32],
        #                                   Air_Temperature=dbframe[33],
        #                                   Air_Temperature_Unit=dbframe[34],
        #                                   Vapor_Pressure=dbframe[35],
        #                                   Vapor_Pressure_Unit=dbframe[36],
        #                                   Electric_Conductivity=dbframe[37],
        #                                   Electric_Conductivity_Unit=dbframe[38],
        #                                   pH=dbframe[39],
        #                                   pH_Comment=dbframe[40],
        #                                   SPM=dbframe[41],
        #                                   SPM_Unit=dbframe[42],
        #                                   SPM_Nature=dbframe[43],
        #                                   Ca=dbframe[44],
        #                                   Ca_Unit=dbframe[45],
        #                                   Mg=dbframe[46],
        #                                   Mg_Unit=dbframe[47],
        #                                   Na=dbframe[48],
        #                                   Na_Unit=dbframe[49],
        #                                   K=dbframe[50],
        #                                   K_Unit=dbframe[51],
        #                                   Cl=dbframe[52],
        #                                   Cl_Unit=dbframe[53],
        #                                   NO3=dbframe[54],
        #                                   NO3_Unit=dbframe[55],
        #                                   SO4=dbframe[56],
        #                                   SO4_Unit=dbframe[57],
        #                                   Br=dbframe[58],
        #                                   Br_Unit=dbframe[59],
        #                                   NH4=dbframe[60],
        #                                   NH4_Unit=dbframe[61],
        #                                   HCO=dbframe[62],
        #                                   HCO_Unit=dbframe[63])
        #     print(dataobj)
        #     dataobj.save()
        if len(updated_site) == "":
            message = f"The following site was updated: {updated_site}"
        else:
            message = f"The following site was inserted: {SiteName}"

        return render(request, 'upload_success.html', {'uploaded_file_url': uploaded_file_url, 'message': message})
    return render(request, 'index.html', {})

# def Import_Excel(request):
#     if request.method == 'POST':
#         MetaData = MetaDataResource()
#         Data = DataResource()
#         dataset = Dataset()
#         new_metadata = request.FILES['file']
#         data_import = dataset.load(new_metadata.read())
#         result_MetaData = MetaData.import_data(dataset=dataset, dry_run=True)
#         result_Data = Data.import_data(dataset=dataset, dry_run=True)

#         if not result_MetaData.has_errors():
#             MetaData.import_data(dataset=dataset, dry_run=False)

#     return render(request, 'index.html',{})
