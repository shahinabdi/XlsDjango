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
        return self.SiteName

    objects = models.Manager()
    
    class Meta:
        verbose_name = 'Metadata'
        verbose_name_plural = 'Metadata'

class Data(models.Model):
    Sample_Name = models.CharField(max_length=255, default='', unique=True)
    Media_Type = models.CharField(max_length=255, default='', blank=True)
    Type_of_Rain_Collector = models.CharField(max_length=255, default='', blank=True)
    Date = models.DateTimeField()
    Begin_of_Period = models.DateTimeField()
    End_of_Period = models.DateTimeField()
    Comment = models.CharField(max_length=255, default='', blank=True)
    # O18
    O18 = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    O18_Unit = models.CharField(max_length=255, null=True, blank=True)
    O18_Error = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    O18_Error_Unit = models.CharField(max_length=255, null=True, blank=True)
    O18_Provider = models.CharField(max_length=255, null=True, blank=True)
    O18_Measure_Equipement = models.CharField(max_length=255, null=True, blank=True)
    # H2
    H2 = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    H2_Unit = models.CharField(max_length=255, null=True, blank=True)
    H2_Error = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    H2_Error_Unit = models.CharField(max_length=255, null=True, blank=True)
    H2_Provider = models.CharField(max_length=255, null=True, blank=True)
    H2_Measure_Equipement = models.CharField(max_length=255, null=True, blank=True)
    # H3
    H3 = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    H3_Unit = models.CharField(max_length=255, null=True, blank=True)
    H3_Error = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    H3_Error_Unit = models.CharField(max_length=255, null=True, blank=True)
    H3_Provider = models.CharField(max_length=255, null=True, blank=True)
    H3_Measure_Equipement = models.CharField(max_length=255, null=True, blank=True)
    # O17
    O17 = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    O17_Unit = models.CharField(max_length=255, null=True, blank=True)
    O17_Error = models.DecimalField(
        max_digits=18, decimal_places=10, null=True, blank=True)
    O17_Error_Unit = models.CharField(max_length=255, null=True, blank=True)
    O17_Provider = models.CharField(max_length=255, null=True, blank=True)
    O17_Measure_Equipement = models.CharField(max_length=255, null=True, blank=True)
    # Properties Physic
    Percipitation_Amount = models.DecimalField(
        max_digits=18, decimal_places=10, null=True, blank=True)
    Percipitation_Amount_Unit = models.CharField(max_length=255, null=True, blank=True)
    Air_Temperature = models.DecimalField(
        max_digits=18, decimal_places=10, null=True, blank=True)
    Air_Temperature_Unit = models.CharField(max_length=255, null=True, blank=True)
    Vapor_Pressure = models.DecimalField(
        max_digits=18, decimal_places=10, null=True, blank=True)
    Vapor_Pressure_Unit = models.CharField(max_length=255, null=True, blank=True)
    Electric_Conductivity = models.DecimalField(
        max_digits=18, decimal_places=10, null=True, blank=True)
    Electric_Conductivity_Unit = models.CharField(max_length=255, null=True, blank=True)
    pH = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    pH_Comment = models.CharField(max_length=255, null=True, blank=True)
    SPM = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    SPM_Unit = models.CharField(max_length=255, null=True, blank=True)
    SPM_Nature = models.CharField(max_length=255, null=True, blank=True)
    # Chemistry
    Ca = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    Ca_Unit = models.CharField(max_length=255, null=True, blank=True)
    Mg = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    Mg_Unit = models.CharField(max_length=255, null=True, blank=True)
    Na = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    Na_Unit = models.CharField(max_length=255, null=True, blank=True)
    K = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    K_Unit = models.CharField(max_length=255, null=True, blank=True)
    Cl = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    Cl_Unit = models.CharField(max_length=255, null=True, blank=True)
    NO3 = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    NO3_Unit = models.CharField(max_length=255, null=True, blank=True)
    SO4 = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    SO4_Unit = models.CharField(max_length=255, null=True, blank=True)
    Br = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    Br_Unit = models.CharField(max_length=255, null=True, blank=True)
    NH4 = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    NH4_Unit = models.CharField(max_length=255, null=True, blank=True)
    HCO3 = models.DecimalField(max_digits=18, decimal_places=10, null=True, blank=True)
    HCO3_Unit = models.CharField(max_length=255, null=True, blank=True)
    Site = models.ForeignKey(MetaData, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.Sample_Name

    objects = models.Manager()
    class Meta:
        verbose_name = 'Data'
        verbose_name_plural = 'Data'