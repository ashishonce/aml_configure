
import os
import sys
import subprocess


azure_credentials = { "clientId": "ab96606e-49a7-45d3-a575-5172e11fdb7f", "clientSecret": "^s:e6b4uCMXxN168t+i?[f](`E~8YeAP", "subscriptionId": "4847477c-3812-4667-ad10-174e0eab74d4", "tenantId": "2d1aba9c-5938-402b-90b9-72a284a4bced"}

tenant_id=azure_credentials.get("tenantId", "")
service_principal_id=azure_credentials.get("clientId", "")
service_principal_password=azure_credentials.get("clientSecret", "")
command = ("az login --service-principal --username {APP_ID} --password \"{PASSWORD}\" --tenant {TENANT_ID}").format(
        APP_ID=service_principal_id, PASSWORD=service_principal_password, TENANT_ID=tenant_id)

try:
    app_create = subprocess.check_output(command, shell=True)
    print(app_create)
except Exception as ex:
    print(ex)