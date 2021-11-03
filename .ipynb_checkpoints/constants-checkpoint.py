from parse_utils import parse_date
#Files
fname_personal = 'data/personal_info.csv'
fname_employment = 'data/employment.csv'
fname_vehicles = 'data/vehicles.csv'
fname_update_status = 'data/update_status.csv'
fnames = fname_personal, fname_employment, fname_vehicles, fname_update_status

#Parser
parser_personal = (str,str,str,str,str)
parser_employment = (str,str,str,str)
parser_vehicles = (str,str,str,int)
parser_update_status = (str,parse_date, parse_date)
parsers = parser_personal, parser_employment, parser_vehicles, parser_update_status

# named tuple names
class_name_personal = 'Personal'
class_name_employment = 'Employment'
class_name_vehicles = 'Vehicles'
class_name_updatestatus = 'UpdateStatus'
class_names = class_name_personal, class_name_employment,\
                class_name_vehicles, class_name_updatestatus

# Field Inclusion/Exclusion
personal_fields_compress = [True, True, True, True, True]
employment_fields_compress = [True, True, True, False]
vehicle_fields_compress = [False, True, True, True]
update_status_fields_compress = [False, True, True]
compress_fields = (personal_fields_compress, employment_fields_compress,
                   vehicle_fields_compress, update_status_fields_compress)
