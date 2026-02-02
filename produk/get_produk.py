import requests
import hashlib
from datetime import datetime
from produk.models import Produk, Kategori, Status
from django.db import transaction

def get_data():
    username = "tesprogrammer020226C02"
    today = datetime.today()
    raw_password = f"bisacoding-{today.day:02d}-{today.month:02d}-{str(today.year)[-2:]}"
    md5_password = hashlib.md5(raw_password.encode()).hexdigest()

    data = {"username": username, "password": md5_password}
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
    response = requests.post(url, data=data)

    if response.status_code != 200:
        print("API error", response.status_code)
        return

    api_data = response.json()
    if response.status_code != 200:
        print("Error connecting to API:", response.status_code)
        print(response.text)
        return

    data = response.json()
    if data.get("error") != 0:
        print("API Error:", data.get("ket"))
        return

    # --- Save to database ---
    for item in data.get("data", []):
        # --- Get or create category ---
        kategori_obj, _ = Kategori.objects.get_or_create(nama_kategori=item["kategori"])

        # --- Get or create status ---
        status_obj, _ = Status.objects.get_or_create(nama_status=item["status"])

        # --- Save product ---
        Produk.objects.update_or_create(
            nama_produk=item["nama_produk"],
            defaults={
                "harga": int(item["harga"]),
                "kategori": kategori_obj,
                "status": status_obj
            }
        )

    print("Data berhasil disimpan!")

    return


# from django.core.management.base import BaseCommand
# from produk.models import Produk

# import requests
# import hashlib
# from datetime import datetime

# class Command(BaseCommand):
#     help = "Print all Produk in database"

#     def handle(self, *args, **kwargs):
#         username = "tesprogrammer020226C01"

#         today = datetime.today()
#         raw_password = f"bisacoding-{today.day:02d}-{today.month:02d}-{str(today.year)[-2:]}"
#         md5_password = hashlib.md5(raw_password.encode()).hexdigest()

#         url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
#         data = {"username": username, "password": md5_password}
#         response = requests.post(url, data=data)

#         print("Status code:", response.status_code)
#         print("Response:", response.json())