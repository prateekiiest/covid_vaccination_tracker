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

import numpy as np
import random
import pandas as pd

population = 5
data = np.empty((0,10), str)
features = ['UUID', 'Gender', 'Age', 'Profession', 'Locality/Pin Code', 'Rate of infection in that zone', 'Pre-existing medical conditions', 'Travel history in the last 1 month', 'Coming in contact with someone who has been diagnosed with Covid 19', 'Do you have any kind of Covid 19 symptoms']

uuids = random.sample(range(0, population), population)
genders = ["M", "F"]
ages = np.arange(1, 71, 1).tolist()
professions = ["Health Care", "Security", "Police", "Blue Collar worker", "Work from Home", "Public Policy", "Bank"]
localities = [587112, 587201, 587101, 587102, 587103, 587311, 587116, 587114, 587115, 587113]
conditions = ["Diabetes", "Cancer", "Kidney Ailments", "Pulmonary", "Heart"]
yes_no_questions = ["Y", "N"]

curr_uuid = 0
for i in range(population):

    person = np.array([])

    uuid = str(np.random.randint(1000, 9999)) + "-" + str(np.random.randint(1000, 9999)) + "-" + str(np.random.randint(1000, 9999)) + "-" + str(np.random.randint(1000, 9999))
    gender = random.choice(genders)
    age = random.choice(ages)
    profession = random.choice(professions)
    locality = random.choice(localities)
    infection_rate = round(random.uniform(0.8, 1.2), 1)
    condition = random.choice(conditions)
    travel = random.choice(yes_no_questions)
    contact = random.choice(yes_no_questions)
    symptoms = random.choice(yes_no_questions)

    person = np.append(person, uuid)
    person = np.append(person, gender)
    person = np.append(person, age)
    person = np.append(person, profession)
    person = np.append(person, locality)
    person = np.append(person, infection_rate)
    person = np.append(person, condition)
    person = np.append(person, travel)
    person = np.append(person, contact)
    person = np.append(person, symptoms)

    data = np.append(data, [person], axis=0)
    curr_uuid += 1

df = pd.DataFrame(data, columns=features)
pd.DataFrame(data, columns=features).to_csv("data.csv", index=False)
print(df.to_string(index=False))