#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Generate synthetic HubSpot Contacts"""

import random

# Initialize data sources
with open("etternavn.txt", "r") as surname_file:
    surnames = surname_file.readlines()

with open("fornavn.txt", "r") as firstname_file:
    firstnames = firstname_file.readlines()

with open("byer.txt", "r") as cities_file:
    cities = cities_file.readlines()

with open("fylker.txt", "r") as fylker_file:
    fylker = fylker_file.readlines()

with open("jobbtittler.txt", "r") as jobbtittler_file:
    job_titles = jobbtittler_file.readlines()

with open("company-ids.txt", "r") as company_ids_file:
    company_ids = company_ids_file.readlines()

# Generate synthetic data
contacts = []

def gen_data(filename, num_of_contacts=100):

    for x in range(0, num_of_contacts):

        first_name = firstnames[random.randint(0, len(firstnames)-1)].strip()
        last_name = surnames[random.randint(0, len(surnames)-1)].strip()
        city = cities[random.randint(0, len(cities)-1)].strip()
        region = fylker[random.randint(0, len(fylker)-1)].strip()
        website = "http://www.HubSpot.com"
        job_title = job_titles[random.randint(0, len(job_titles)-1)].strip()
        twitter_user = f"{first_name[0]}{last_name}".lower()
        email = f"{first_name}.{last_name}@hubspot.com"
        company_name = "HubSpot"
        company_id = company_ids[random.randint(0, len(company_ids)-1)].strip()

        contact = f"{first_name},{last_name},{city},{region},{website},{job_title},{twitter_user},{email},{company_name},{company_id}\n"
        contacts.append(contact)

    # dump generated data to file
    file_header = "First Name,Last Name,City,State/Region,Website URL,Job Title,Twitter Username,Email,Company Name,Company ID\n"

    with open(filename, 'w') as outfile:
        outfile.write(file_header)
        for o in contacts:
            outfile.write(o)


if __name__ == "__main__":
    gen_data("contacts.csv")
