import pandas as pd
from django.shortcuts import render
from .views_resources import *

# Define the path to the reference file
REFERENCE_FILE_PATH = 'ReferenceFile.xlsx'

# Define the expected column names and data types for each sheet
# DATA_DTYPES = {'id': int, 'name': str, 'age': int, 'email': str}
DATA_DTYPES = {
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

def change_data_types(data):
    # Define a dictionary to map the column names to their data types
    
    # Loop through the columns and change the data types as per the dictionary
    for col, data_type in DATA_DTYPES.items():
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

def verify_metadata_rows(metadata):
    """
    Verify the rows in the metadata sheet using
    """
    if len(metadata) < 1:
        raise ValueError('Metadata has not enough data')
    if len(metadata) > 1:
            raise ValueError('Metadata has more than one data')

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
        
def validate_excel_file(file):
    # Check if file is an Excel file
    if not file.name.endswith('.xlsx') and not file.name.endswith('.xls'):
        raise ValueError("Uploaded file is not an Excel file.")

def upload_file(request):  # sourcery skip: extract-method
    if request.method == 'POST':
        # Get the uploaded file from the request
        file = request.FILES['file']
        try:
            validate_excel_file(file)
        except ValueError as e:
            return render(request, 'upload.html', {'error': str(e)})
        else:
            data = pd.read_excel(file, sheet_name='Data')
            metadata = pd.read_excel(file, sheet_name='MetaData')
            
            try:
                data = change_data_types(data)
            except ValueError as e:
                return render(request, 'upload.html', {'error': str(e)})
                
            try:
                # Verify the column and row names in the metadata sheet
                verify_metadata_cols(metadata)
                verify_metadata_rows(metadata)    
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

