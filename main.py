# Sample fields:
# 1. UUID: 0000-8675-76543-0023
# 2. Gender: M
# 3. Age: 50
# 4. Profession: Bank
# 5. Locality/Pincode: Refer to the pdf: 560037
# 6. Rate of infection in that zone: Follow the trend dataset [R-naught: 0.8 - 1.2] - 1.1
# 7. Pre-existing medical conditions: None
# 8. Travel history in the last 1 month: Y
# 9. Coming in contact with someone who has been diagnosed with Covid 19: N
# 10. Do you have any kind of Covid 19 symptoms: N

import random, requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup


# Set population, initialize dataset
population = 100
data = np.empty((0,10), str)

genders = ["M", "F"]
ages = np.arange(1, 71, 1).tolist()
professions = ["Health Care", "Security", "Police", "Blue Collar worker", "Work from Home", "Public Policy", "Bank"]
conditions = ["None", "Diabetes", "Cancer", "Kidney Ailments", "Pulmonary", "Heart"]
yes_no_questions = ["Y", "N"]

# Scrape site for KARNATAKA pincodes
def generate_pincodes():
    def is_int(s):
        try: 
            int(s)
            return True
        except ValueError:
            return False
    pincodes = []
    url = requests.get("https://chennaiiq.com/india/pincode/index.asp?id=16&state_name=Karnataka&page=B").text
    soup = BeautifulSoup(url, 'lxml')
    trs = soup.find_all('tr', class_="tab")
    for tr in trs:
        for td in tr.find_all('td'):
            value = str(td).replace("<td>", "").replace("</td>", "")
            if is_int(value):
                if int(value) > 100000:
                    pincodes.append(int(value))
    return pincodes

# Generate random values for each of the features for a given person
def generate_random_features():
    uuid = str(np.random.randint(1000, 9999)) + "-" + str(np.random.randint(1000, 9999)) + "-" + str(np.random.randint(1000, 9999)) + "-" + str(np.random.randint(1000, 9999))
    gender = random.choice(genders)
    age = random.choice(ages)
    profession = random.choice(professions)
    pincode = random.choice(generate_pincodes())
    infection_rate = round(random.uniform(0.8, 1.2), 1)
    condition = random.choice(conditions)
    travel = random.choice(yes_no_questions)
    contact = random.choice(yes_no_questions)
    symptoms = random.choice(yes_no_questions)
    return (uuid, gender, age, profession, pincode, infection_rate, condition, travel, contact, symptoms)

def create_person(uuid, gender, age, profession, pincode, infection_rate, condition, travel, contact, symptoms):
    person = np.array([])
    # Add features to person array
    person = np.append(person, uuid)
    person = np.append(person, gender)
    person = np.append(person, age)
    person = np.append(person, profession)
    person = np.append(person, pincode)
    person = np.append(person, infection_rate)
    person = np.append(person, condition)
    person = np.append(person, travel)
    person = np.append(person, contact)
    person = np.append(person, symptoms)
    return person

# Build dataset
def build_dataset():
    for _ in range(population):
        # Will be manipulating global dataset
        global data
        # Generate random features for each person
        features = generate_random_features()
        uuid, gender, age, profession, pincode, infection_rate, condition, travel, contact, symptoms = features[0], features[1], features[2], features[3], features[4], features[5], features[6], features[7], features[8], features[9] 
        # Add features to person array, add person to data array
        person = create_person(uuid, gender, age, profession, pincode, infection_rate, condition, travel, contact, symptoms)
        data = np.append(data, [person], axis=0)

if __name__ == '__main__':

    # initialize dataset and define columns
    features_list = ['UUID', 'Gender', 'Age', 'Profession', 'Locality/Pin Code', 'Rate of infection in that zone', 'Pre-existing medical conditions', 'Travel history in the last 1 month', 'Coming in contact with someone who has been diagnosed with Covid 19', 'Do you have any kind of Covid 19 symptoms']

    # poppulate data array
    build_dataset()
    # Export data
    df = pd.DataFrame(data, columns=features_list)
    pd.DataFrame(data, columns=features_list).to_csv("data.csv", index=False)

    # Only for testing, do not print for large data sets
    # print(df.to_string(index=False))