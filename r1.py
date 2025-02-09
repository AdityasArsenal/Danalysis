from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)


def insertion_company(company_name):
    company_response = supabase.table("companies").insert({"name":f"{company_name}"}).execute()
    inserted_company_id = company_response.data[0]['id']
    
    return inserted_company_id



def insertion_kpi_definition(kpi_type_id, kpi_names, units, decimals, reference_units, inserted_kpi_names, inserted_kpi_definitions_ids):
    
    for kpi_name,unit, reference_unit, decimal in zip(kpi_names,units, reference_units, decimals):
        if kpi_name not in inserted_kpi_names:

            kpi_definitions_response = supabase.table("kpi_definitions").insert({"kpi_type_id":f"{kpi_type_id}","name":f"{kpi_name}","unit":f"{unit}","decimal_places":f"{decimal}","reference_unit":f"{reference_unit}"}).execute()
            kpi_definitions_id = kpi_definitions_response.data[0]['id']
            inserted_kpi_definitions_ids.append(kpi_definitions_id)
            inserted_kpi_names.append(kpi_name)

    return inserted_kpi_names, inserted_kpi_definitions_ids



def insertion_company_kpi_data(inserted_company_id, kpi_names, inserted_kpi_names, inserted_kpi_definitions_ids, values, periods,):

    index_map = {name: idx for idx, name in enumerate(inserted_kpi_names)}
    for kpi_name, value, period in zip(kpi_names,values,periods):
        if kpi_name in index_map:
            inserted_kpi_definition_id = inserted_kpi_definitions_ids[index_map[kpi_name]]
            response = supabase.table("company_kpi_data").insert({"company_id":f"{inserted_company_id}","kpi_definition_id":f"{inserted_kpi_definition_id}","value":f"{value}","period":f"{period}"}).execute()
            inserted_company_kpi_data_id = response.data[0]['id']

            return inserted_company_kpi_data_id

            