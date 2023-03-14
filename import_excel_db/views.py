import pandas as pd
import numpy as np
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Data, MetaData

# Define the path to the reference file
REFERENCE_FILE_PATH = 'ReferenceFile.xlsx'

# Define the expected column names and data types for each sheet
# DATA_DTYPES = {'id': int, 'name': str, 'age': int, 'email': str}


def change_data_types(data):
    # Define a dictionary to map the column names to their data types
    data_types = {
        "Sample_Name":str,
        "Media_Type":str,
        "Type_of_Rain_Collector":str,
        "Date":{'date': 'datetime64[ns]'},
        "Begin_of_Period":{'date': 'datetime64[ns]'},
        "End_of_Period":{'date': 'datetime64[ns]'},
        "O18":float,
        "O18_Unit":str,
        "O18_Error":float,
        "O18_Error_Unit":str,
        "O18_Provider":str,
        "O18_Measure_Equipement":str,
        "H2":float,
        "H2_Unit":str,
        "H2_Error":float,
        "H2_Error_Unit":str,
        "H2_Provider":str,
        "H2_Measure_Equipement":str,
        "H3":float,
        "H3_Unit":str,
        "H3_Error":float,
        "H3_Error_Unit":str,
        "H3_Provider":str,
        "H3_Measure_Equipement":str,
        "O17":float,
        "O17_Unit":str,
        "O17_Error":float,
        "O17_Error_Unit":str,
        "O17_Provider":str,
        "O17_Measure_Equipement":str,
        "Percipitation_Amount":float,
        "Percipitation_Amount_Unit":str,
        "Air_Temperature":float,
        "Air_Temperature_Unit":str,
        "Vapor_Pressure":float,
        "Vapor_Pressure_Unit":str,
        "Electric_Conductivity":float,
        "Electric_Conductivity_Unit":str,
        "pH":float,
        "pH_Comment":str,
        "SPM":float,
        "SPM_Unit":str,
        "SPM_Nature":str,
        "Ca":float,
        "Ca_Unit":str,
        "Mg":float,
        "Mg_Unit":str,
        "Na":float,
        "Na_Unit":str,
        "K":float,
        "K_Unit":str,
        "Cl":float,
        "Cl_Unit":str,
        "NO3":float,
        "NO3_Unit":str,
        "SO4":float,
        "SO4_Unit":str,
        "Br":float,
        "Br_Unit":str,
        "NH4":float,
        "NH4_Unit":str,
        "HCO":float,
        "HCO_Unit":str
    }
    
    # Loop through the columns and change the data types as per the dictionary
    for col, data_type in data_types.items():
        try:
            if col in data.columns:
                data[col] = data[col].astype(data_type)
        except Exception as e:
            raise e
        else:
            return data

def verify_metadata_cols(metadata):
    """
    Verify the column names in the metadata sheet using the reference file
    """
    ref_data = pd.read_excel(REFERENCE_FILE_PATH, sheet_name='MetaData')
    if set(metadata.columns) != set(ref_data.columns):
        raise ValueError('Metadata columns do not match reference file')

def verify_data_cols(data):
    """
    Verify the column names in the data sheet using the reference file
    """
    ref_data = pd.read_excel(REFERENCE_FILE_PATH, sheet_name='Data')
    if set(data.columns) != set(ref_data.columns):
        raise ValueError('Data columns do not match reference file')

# def verify_data_types(data):
#     """
#     Verify the data types in the data sheet
#     """
#     for col, dtype in DATA_DTYPES.items():
#         if data[col].dtype != dtype:
#             print(f'{data[col]},Col DTYPE {data[col].dtype}, {dtype}')
#             raise ValueError(f'Invalid data type in column {col}')
        

def save_metadata_to_db(metadata):
    """
    Save the metadata to the database
    """
    updated_site = ""

    for dbframe in metadata.itertuples():
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
            # If object exists, update it
            else:
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
    return updated_site, SiteName

def save_data_to_db(data, SiteName):
    """
    Save the data to the database
    """
    metadata = MetaData.objects.get(SiteName=SiteName)

    for dbframe in data.itertuples():
        Sample_Name=dbframe[1]
        Media_Type=dbframe[2]
        Type_of_Rain_Collector=dbframe[3]
        Date=dbframe[4]
        Begin_of_Period=dbframe[5]
        End_of_Period=dbframe[6]
        Comment=dbframe[7]
        O18=dbframe[8]
        O18_Unit=dbframe[9]
        O18_Error=dbframe[10]
        O18_Error_Unit=dbframe[11]
        O18_Provider=dbframe[12]
        O18_Measure_Equipement=dbframe[13]
        H2=dbframe[14]
        H2_Unit=dbframe[15]
        H2_Error=dbframe[16]
        H2_Error_Unit=dbframe[17]
        H2_Provider=dbframe[18]
        H2_Measure_Equipement=dbframe[19]
        H3=dbframe[20]
        H3_Unit=dbframe[21]
        H3_Error=dbframe[22]
        H3_Error_Unit=dbframe[23]
        H3_Provider=dbframe[24]
        H3_Measure_Equipement=dbframe[25]
        O17=dbframe[26]
        O17_Unit=dbframe[27]
        O17_Error=dbframe[28]
        O17_Error_Unit=dbframe[29]
        O17_Provider=dbframe[30]
        O17_Measure_Equipement=dbframe[31]
        Percipitation_Amount=dbframe[32]
        Percipitation_Amount_Unit=dbframe[33]
        Air_Temperature=dbframe[34]
        Air_Temperature_Unit=dbframe[35]
        Vapor_Pressure=dbframe[36]
        Vapor_Pressure_Unit=dbframe[37]
        Electric_Conductivity=dbframe[38]
        Electric_Conductivity_Unit=dbframe[39]
        pH=dbframe[40]
        pH_Comment=dbframe[41]
        SPM=dbframe[42]
        SPM_Unit=dbframe[43]
        SPM_Nature=dbframe[44]
        Ca=dbframe[45]
        Ca_Unit=dbframe[46]
        Mg=dbframe[47]
        Mg_Unit=dbframe[48]
        Na=dbframe[49]
        Na_Unit=dbframe[50]
        K=dbframe[51]
        K_Unit=dbframe[52]
        Cl=dbframe[53]
        Cl_Unit=dbframe[54]
        NO3=dbframe[55]
        NO3_Unit=dbframe[56]
        SO4=dbframe[57]
        SO4_Unit=dbframe[58]
        Br=dbframe[59]
        Br_Unit=dbframe[60]
        NH4=dbframe[61]
        NH4_Unit=dbframe[62]
        HCO3=dbframe[63]
        HCO3_Unit=dbframe[64]
        Site = metadata #F_KEY

        dataobj = Data.objects.create(Sample_Name=Sample_Name,
                                        Media_Type=Media_Type,
                                        Type_of_Rain_Collector=Type_of_Rain_Collector,
                                        Date=Date,
                                        Begin_of_Period=Begin_of_Period,
                                        End_of_Period=End_of_Period,
                                        O18=O18,
                                        O18_Unit=O18_Unit,
                                        O18_Error=O18_Error,
                                        O18_Error_Unit=O18_Error_Unit,
                                        O18_Provider=O18_Provider,
                                        O18_Measure_Equipement=O18_Measure_Equipement,
                                        H2=H2,
                                        H2_Unit=H2_Unit,
                                        H2_Error=H2_Error,
                                        H2_Error_Unit=H2_Error_Unit,
                                        H2_Provider=H2_Provider,
                                        H2_Measure_Equipement=H2_Measure_Equipement,
                                        H3=H3,
                                        H3_Unit=H3_Unit,
                                        H3_Error=H3_Error,
                                        H3_Error_Unit=H3_Error_Unit,
                                        H3_Provider=H3_Provider,
                                        H3_Measure_Equipement=H3_Measure_Equipement,
                                        O17=O17,
                                        O17_Unit=O17_Unit,
                                        O17_Error=O17_Error,
                                        O17_Error_Unit=O17_Error_Unit,
                                        O17_Provider=O17_Provider,
                                        O17_Measure_Equipement=O17_Measure_Equipement,
                                        Percipitation_Amount=Percipitation_Amount,
                                        Percipitation_Amount_Unit=Percipitation_Amount_Unit,
                                        Air_Temperature=Air_Temperature,
                                        Air_Temperature_Unit=Air_Temperature_Unit,
                                        Vapor_Pressure=Vapor_Pressure,
                                        Vapor_Pressure_Unit=Vapor_Pressure_Unit,
                                        Electric_Conductivity=Electric_Conductivity,
                                        Electric_Conductivity_Unit=Electric_Conductivity_Unit,
                                        pH=pH,
                                        pH_Comment=pH_Comment,
                                        SPM=SPM,
                                        SPM_Unit=SPM_Unit,
                                        SPM_Nature=SPM_Nature,
                                        Ca=Ca,
                                        Ca_Unit=Ca_Unit,
                                        Mg=Mg,
                                        Mg_Unit=Mg_Unit,
                                        Na=Na,
                                        Na_Unit=Na_Unit,
                                        K=K,
                                        K_Unit=K_Unit,
                                        Cl=Cl,
                                        Cl_Unit=Cl_Unit,
                                        NO3=NO3,
                                        NO3_Unit=NO3_Unit,
                                        SO4=SO4,
                                        SO4_Unit=SO4_Unit,
                                        Br=Br,
                                        Br_Unit=Br_Unit,
                                        NH4=NH4,
                                        NH4_Unit=NH4_Unit,
                                        HCO3=HCO3,
                                        HCO3_Unit=HCO3_Unit,
                                        Site=Site)
        dataobj.save()



def upload_file(request):
    if request.method == 'POST':
        # Get the uploaded file from the request
        file = request.FILES['file']

        # Read the file into a pandas dataframe
        data = pd.read_excel(file, sheet_name='Data')
        metadata = pd.read_excel(file, sheet_name='MetaData')
        
        try:
            data = change_data_types(data)
        except ValueError as e:
            return render(request, 'upload.html', {'error': str(e)})
            
        try:
            # Verify the column names in the metadata sheet
            verify_metadata_cols(metadata)

            # Verify the column names in the data sheet
            verify_data_cols(data)

            # Save the data and metadata to the database
            updated_site, sitename = save_metadata_to_db(metadata)
            save_data_to_db(data, sitename)

            # Redirect to a success page
            return render(request, 'upload_success.html')

        except ValueError as e:
            # If there's an error, render the upload page with the error message
            return render(request, 'upload.html', {'error': str(e)})

    # Render the upload page
    return render(request, 'upload.html')

