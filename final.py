from tabulate import tabulate
from truecallerpy import search_phonenumber
import json 
import subprocess
from apify_client import ApifyClient

phone = input("Enter Phone in the format '+CountryCode Number': ")
email = input("Enter email: ")

print()
print("FETCHING....")
print()

# ------WHATSAPP-----------------
client = ApifyClient("apify_api_ED41KNhxvnawcml2cW7hxxyYJUHKDz1yXKgY")
cnt = 0
run_input = {
    "numbers": [phone]
}
run = client.actor("inutil_labs/wscrp-free").call(run_input=run_input)
l = []
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    l.append(item)
if l:
    cnt += 1
    phone = l[0]['phone']
    picture = l[0]['picture']
    isbiz = l[0]['isbiz']
    about = l[0]['about']

    # Prepare WhatsApp data
    whatsapp_data = [
        ['Registered', 'Yes'],
        ['Phone', phone],
        ['Profile picture', picture],
        ['Is business', isbiz],
        ['About', about]
    ]

    # Generate WhatsApp table
    whatsapp_table = tabulate(whatsapp_data, tablefmt='grid')

    # Print WhatsApp table
    # print('------------------------')
    print(cnt, "WhatsApp")
    # print('------------------------')
    print(whatsapp_table)
    print()

# -----------TRUECALLER------------
command = ['truecallerpy', '-s', phone]
output = subprocess.check_output(command, universal_newlines=True)
result = json.loads(output)

data = result['data']
if data:
    cnt += 1

    # Prepare Truecaller data
    truecaller_data = [
        ['Registered', 'Yes'],
        ['Name', data[0]['name']],
        ['Location', data[0]['addresses'][0]['city']]
    ]

    # Generate Truecaller table
    truecaller_table = tabulate(truecaller_data, tablefmt='grid')

    # Print Truecaller table
    # print('------------------------')
    print(cnt, "Truecaller:")
    # print('------------------------')
    print(truecaller_table)
    print()
