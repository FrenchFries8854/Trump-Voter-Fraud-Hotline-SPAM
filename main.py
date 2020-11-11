import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
random.seed = (os.urandom(1024))

url = "https://defendyourballot.formstack.com/forms/index.php"

names = json.loads(open("names.json").read())
states = json.loads(open("states.json").read())

counter = -1
for name in names:
    counter += 1
    middle_name = random.choice(names)
    last_name = random.choice(names)
    name_extra = "".join(random.choice(string.digits))

    email = name.lower() + name_extra + "@gmail.com"
    zipcode = random.randint(0, 9) + random.randint(0, 9) + random.randint(0, 9) + random.randint(0, 9) + random.randint(0, 9)

    password = "".join(random.choice(chars) for i in range(8))

    requests.post(url, allow_redirects=False, data={
        "form": "4124516",
        "viewkey": "17N8F1Ijju",
        "password": "",
        "hidden_fields": "",
        "incomplete": "",
        "incomplete_email": "",
        "incomplete_password": "",
        "referrer": "https: // www.google.com/",
        "referrer_type": "link",
        "_submit": "1",
        "style_version": "3",
        "latitude": "",
        "longitude": "",
        "viewparam": "933809",
        "field101315259-first": name,
        "field101315259-middle": middle_name,
        "field101315259-last": last_name,
        "field101315260": "Phone Number",
        "field101316245-address": "Address 1",
        "field101316245-address2": "Address 2",
        "field101316245-city": "City",
        "field101316245-state": random.choice(states),
        "field101316245-zip": str(zipcode),
        "field101315261": email,
        "field101315261_confirm": email,
        "field101315264": "State of Incident",
        "field101315265": "County of the Incident",
        "field101315266": "Name of the Polling Place or Early Voting Site",
        "field101315267": "describe the incident",
        "field101315268": "(binary)",
        "field101319448": "",
        "field101319451": "",
        "field101319453": "",
        "field101319455": "",
        "field101319456": "",
        "field101319457": "",
        "g-recaptcha-response": "",
        "nonce": "fpXUo6x3cXPNBSJs"
    })