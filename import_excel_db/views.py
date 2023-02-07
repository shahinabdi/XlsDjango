from django.shortcuts import render
from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import MetaData, Data

from tablib import Dataset
from .resource import EmployeeResource
# Create your views here.


def Import_Excel_pandas(request):
    if request.method == 'POST' and request.FILES['file']:
        xlsfile  = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(xlsfile.name, xlsfile)
        uploaded_file_url = fs.url(filename)
        empexceldata = pd.read_excel(filename)
        for dbframe in empexceldata.itertuples():
            obj = MetaData.objects.create(Empcode=dbframe.Empcode,
                                            firstName = dbframe.firstName,
                                            middleName = dbframe.middleName,
                                            lastName = dbframe.lastName,
                                            email = dbframe.email,
                                            phoneNo = dbframe.phoneNo,
                                            address = dbframe.address,
                                            birthdate = dbframe.birthdate, gender = dbframe.gender)
            obj.save()
        return render(request, 'index.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'index.html', {})

def Import_Excel(request):
    if request.method == 'POST':
        Employee = EmployeeResource()
        dataset = Dataset()
        new_employee = request.FILES['myfile']
        data_import = dataset.load(new_employee.read())
        result = Employee.import_data(dataset=dataset, dry_run=True)
        if not result.has_errors():
            Employee.import_data(dataset=dataset, dry_run=False)
    return render(request, 'index.html',{})
