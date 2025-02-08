from dotenv import load_dotenv
load_dotenv()
import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

supabase = create_client(url, key)

#insert
supabase.table("company_kpi_data").insert({"name":"ram","mail":"ram@gmail.com"}).execute()


#delete 
supabase.table("company_kpi_data").delete().eq("id", 2).execute()


#select
data = supabase.table("company_kpi_data").select("*").execute()

#update
supabase.table("company_kpi_data").update({"name": "rammm"}).eq("id", 2).execute()



print(data)
