from django.db import models

# Create your models here.


class MetaData(models.Model):
    # STATION INFO
    NameGroup = models.CharField(max_length=255, default='')
    Project = models.CharField(max_length=255, null=True)
    SiteName = models.CharField(max_length=255, unique=True)
    Country = models.CharField(max_length=255, null=True)
    Town = models.CharField(max_length=255, null=True)
    Code_INSEE = models.CharField(max_length=255, null=True)
    GNIP_Code = models.CharField(max_length=255, null=True)
    Latitude = models.CharField(max_length=255, null=True)
    Longitude = models.CharField(max_length=255, null=True)
    Altitude = models.CharField(max_length=255, null=True)
    Unit_Altitude = models.CharField(max_length=255, null=True)
    Type_of_Site = models.CharField(max_length=255, null=True)
    Source_of_Information = models.CharField(max_length=255, null=True)
    BV_INSPIRE = models.CharField(max_length=255, null=True)
    FG_INSPIRE = models.CharField(max_length=255, null=True)
    SNO_RENOIR = models.CharField(max_length=255, null=True)
    Link_to_National = models.CharField(max_length=255, null=True)
    # LAB INFO
    Laboratory_Name = models.CharField(max_length=255, null=True)
    First_Organism_Name = models.CharField(max_length=255, null=True)
    Second_Organism_Name = models.CharField(max_length=255, null=True)
    Third_Organism_Name = models.CharField(max_length=255, null=True)
    Code = models.CharField(max_length=255, null=True)
    Contact = models.CharField(max_length=255, null=True)
    # OSU INSU CNRS INFO
    Home_Base_Affilate_OSU = models.CharField(max_length=255, null=True)
    Associated_OSU = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.Site

    objects = models.Manager()


class Data(models.Model):
    Sample_Name = models.CharField(max_length=255, default='')
    Media_Type = models.CharField(max_length=255, default='')
    Type_of_Rain_Collector = models.CharField(max_length=255, default='')
    Date = models.DateTimeField()
    Begin_of_Period = models.DateTimeField()
    End_of_Period = models.DateTimeField()
    # O18
    O18 = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    O18_Unit = models.CharField(max_length=255, null=True)
    O18_Error = models.DecimalField(
        max_digits=18, decimal_places=10, null=True)
    O18_Error_Unit = models.CharField(max_length=255, null=True)
    O18_Provider = models.CharField(max_length=255, null=True)
    O18_Measure_Equipement = models.CharField(max_length=255, null=True)
    # H2
    H2 = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    H2_Unit = models.CharField(max_length=255, null=True)
    H2_Error = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    H2_Error_Unit = models.CharField(max_length=255, null=True)
    H2_Provider = models.CharField(max_length=255, null=True)
    H2_Measure_Equipement = models.CharField(max_length=255, null=True)
    # H3
    H3 = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    H3_Unit = models.CharField(max_length=255, null=True)
    H3_Error = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    H3_Error_Unit = models.CharField(max_length=255, null=True)
    H3_Provider = models.CharField(max_length=255, null=True)
    H3_Measure_Equipement = models.CharField(max_length=255, null=True)
    # O17
    O17 = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    O17_Unit = models.CharField(max_length=255, null=True)
    O17_Error = models.DecimalField(
        max_digits=18, decimal_places=10, null=True)
    O17_Error_Unit = models.CharField(max_length=255, null=True)
    O17_Provider = models.CharField(max_length=255, null=True)
    O17_Measure_Equipement = models.CharField(max_length=255, null=True)
    # Properties Physic
    Percipitation_Amount = models.DecimalField(
        max_digits=18, decimal_places=10, null=True)
    Percipitation_Amount_Unit = models.CharField(max_length=255, null=True)
    Air_Temperature = models.DecimalField(
        max_digits=18, decimal_places=10, null=True)
    Air_Temperature_Unit = models.CharField(max_length=255, null=True)
    Vapor_Pressure = models.DecimalField(
        max_digits=18, decimal_places=10, null=True)
    Vapor_Pressure_Unit = models.CharField(max_length=255, null=True)
    Electric_Conductivity = models.DecimalField(
        max_digits=18, decimal_places=10, null=True)
    Electric_Conductivity_Unit = models.CharField(max_length=255, null=True)
    pH = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    pH_Comment = models.CharField(max_length=255, null=True)
    SPM = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    SPM_Unit = models.CharField(max_length=255, null=True)
    SPM_Nature = models.CharField(max_length=255, null=True)
    # Chemistry
    Ca = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    Ca_Unit = models.CharField(max_length=255, null=True)
    Mg = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    Mg_Unit = models.CharField(max_length=255, null=True)
    Na = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    Na_Unit = models.CharField(max_length=255, null=True)
    K = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    K_Unit = models.CharField(max_length=255, null=True)
    Cl = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    Cl_Unit = models.CharField(max_length=255, null=True)
    NO3 = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    NO3_Unit = models.CharField(max_length=255, null=True)
    SO4 = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    SO4_Unit = models.CharField(max_length=255, null=True)
    Br = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    Br_Unit = models.CharField(max_length=255, null=True)
    NH4 = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    NH4_Unit = models.CharField(max_length=255, null=True)
    HCO = models.DecimalField(max_digits=18, decimal_places=10, null=True)
    HCO_Unit = models.CharField(max_length=255, null=True)

    def __str__(self) -> str:
        return self.Sample_Name

    objects = models.Manager()
