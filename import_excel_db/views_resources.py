from .models import Data, MetaData

def save_metadata_to_db(metadata):
    """
    Save the metadata to the database
    """
    site_status = []

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
            site_status.append(SiteName)
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
                site_status.append('updated')
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
                site_status.append('inserted')

    return site_status

def save_data_to_db(data, SiteName):
    """
    Save the data to the database
    """
    metadata = MetaData.objects.get(SiteName=SiteName)
    message = ""
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



        try:
            dataobj = Data.objects.get(Sample_Name=Sample_Name)
        except Data.DoesNotExist:
            dataobj = Data.objects.create(Sample_Name=Sample_Name,
                                            Media_Type=Media_Type,
                                            Type_of_Rain_Collector=Type_of_Rain_Collector,
                                            Date=Date,
                                            Begin_of_Period=Begin_of_Period,
                                            End_of_Period=End_of_Period,
                                            Comment=Comment,
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
            message = 'Some Sample name was found in the database and updated.'
        else:
            dataobj.Media_Type=Media_Type
            dataobj.Type_of_Rain_Collector=Type_of_Rain_Collector
            dataobj.Date=Date
            dataobj.Begin_of_Period=Begin_of_Period
            dataobj.End_of_Period=End_of_Period
            dataobj.Comment=Comment
            dataobj.O18=O18
            dataobj.O18_Unit=O18_Unit
            dataobj.O18_Error=O18_Error
            dataobj.O18_Error_Unit=O18_Error_Unit
            dataobj.O18_Provider=O18_Provider
            dataobj.O18_Measure_Equipement=O18_Measure_Equipement
            dataobj.H2=H2
            dataobj.H2_Unit=H2_Unit
            dataobj.H2_Error=H2_Error
            dataobj.H2_Error_Unit=H2_Error_Unit
            dataobj.H2_Provider=H2_Provider
            dataobj.H2_Measure_Equipement=H2_Measure_Equipement
            dataobj.H3=H3
            dataobj.H3_Unit=H3_Unit
            dataobj.H3_Error=H3_Error
            dataobj.H3_Error_Unit=H3_Error_Unit
            dataobj.H3_Provider=H3_Provider
            dataobj.H3_Measure_Equipement=H3_Measure_Equipement
            dataobj.O17=O17
            dataobj.O17_Unit=O17_Unit
            dataobj.O17_Error=O17_Error
            dataobj.O17_Error_Unit=O17_Error_Unit
            dataobj.O17_Provider=O17_Provider
            dataobj.O17_Measure_Equipement=O17_Measure_Equipement
            dataobj.Percipitation_Amount=Percipitation_Amount
            dataobj.Percipitation_Amount_Unit=Percipitation_Amount_Unit
            dataobj.Air_Temperature=Air_Temperature
            dataobj.Air_Temperature_Unit=Air_Temperature_Unit
            dataobj.Vapor_Pressure=Vapor_Pressure
            dataobj.Vapor_Pressure_Unit=Vapor_Pressure_Unit
            dataobj.Electric_Conductivity=Electric_Conductivity
            dataobj.Electric_Conductivity_Unit=Electric_Conductivity_Unit
            dataobj.pH=pH
            dataobj.pH_Comment=pH_Comment
            dataobj.SPM=SPM
            dataobj.SPM_Unit=SPM_Unit
            dataobj.SPM_Nature=SPM_Nature
            dataobj.Ca=Ca
            dataobj.Ca_Unit=Ca_Unit
            dataobj.Mg=Mg
            dataobj.Mg_Unit=Mg_Unit
            dataobj.Na=Na
            dataobj.Na_Unit=Na_Unit
            dataobj.K=K
            dataobj.K_Unit=K_Unit
            dataobj.Cl=Cl
            dataobj.Cl_Unit=Cl_Unit
            dataobj.NO3=NO3
            dataobj.NO3_Unit=NO3_Unit
            dataobj.SO4=SO4
            dataobj.SO4_Unit=SO4_Unit
            dataobj.Br=Br
            dataobj.Br_Unit=Br_Unit
            dataobj.NH4=NH4
            dataobj.NH4_Unit=NH4_Unit
            dataobj.HCO3=HCO3
            dataobj.HCO3_Unit=HCO3_Unit
            dataobj.Site=Site
            dataobj.save()

