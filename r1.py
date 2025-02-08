from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)


# data = supabase.table("company_kpi_data").select("*").execute()

# dataa = supabase.table("kpi_definitions").select("*").eq("name", "TotalWasteGenerated").execute()
supabase.table("company_kpi_data").insert({"value":"ram","period":"ram@gmail.com","company_id":"1","kpi_definition_id":"1"}).execute()


# print(data)
# print(dataa)

