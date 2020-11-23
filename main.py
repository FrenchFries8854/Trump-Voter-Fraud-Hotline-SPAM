import requests
import os
import random
import string
import json
import time

chars = string.ascii_letters + string.digits + "!@#$%^&*()"
random.seed = (os.urandom(1024))

url = "https://defendyourballot.formstack.com/forms/index.php"

names = json.loads(open("names.json").read())
states = json.loads(open("states.json").read())
cities = json.loads(open("cities.json").read())
directions = json.loads(open("directions.json").read())
street_types = json.loads(open("street_types.json").read())

counter = -1
while True:
    counter += 1
    first_name = random.choice(names)
    middle_name = random.choice(names)
    last_name = random.choice(names)
    phone_number = f"({random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}) {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}-{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    house_number_rand = random.randint(3, 5)
    house_number = ""
    for x in range(house_number_rand):
        house_number = house_number + str(random.randint(1, 9))
    street = ""
    street_num_rand = random.randint(2, 3)
    for x in range(street_num_rand):
        street = street + str(random.randint(1, 9))
    if street[-1] == "1":
        street = f"{street}st"
    elif street[-1] == "2":
        street = f"{street}nd"
    elif street[-1] == "3":
        street = f"{street}rd"
    else:
        street = f"{street}th"
    address_one = f"{house_number} {street} {random.choice(street_types)} {random.choice(directions)}"
    state = random.choice(states)
    city = random.choice(cities[state])
    incident_state = random.choice(states)
    incident_city = random.choice(cities[incident_state])
    polling_place = f"{random.choice(names)} {random.choice(names)} Vote Center"
    name_extra = "".join(random.choice(string.digits))

    email = first_name.lower() + name_extra + "@gmail.com"
    zipcode = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"

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
        "field101315259-first": first_name,
        "field101315259-middle": middle_name,
        "field101315259-last": last_name,
        "field101315260": phone_number,
        "field101316245-address": address_one,
        "field101316245-address2": "",
        "field101316245-city": city,
        "field101316245-state": state,
        "field101316245-zip": str(zipcode),
        "field101315261": email,
        "field101315261_confirm": email,
        "field101315264": incident_state,
        "field101315265": incident_city,
        "field101315266": polling_place,
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
    print(f"x{counter + 1} sent: {first_name} {middle_name} {last_name} {phone_number} {address_one} {city} {state} {zipcode} {email}")
    print(f"Occurred in: {incident_city} {incident_state} {polling_place}")
    sleep_time = random.randint(1, 75)
    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)
