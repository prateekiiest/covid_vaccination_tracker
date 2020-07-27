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
features = ['uuid', 'gender', 'age', 'profession', 'locality', 'infection_rate', 'condition', 'travel', 'contact', 'symptoms']

uuids = random.sample(range(0, population), population)
genders = ["M", "F"]
ages = np.arange(0, 100, 1).tolist()
professions = ["not employed", "doctor", "lawyer", "architect", "construction worker", "engineer", "self-employed", "consultant", "dentist", "psychologist"]
localities = { 587112:0.8, 587201:0.9, 587101:1.1, 587102:1.0, 587103:1.2, 587311:0.9, 587116:1.1, 587114:0.8, 587115:1.0, 587113:1.2}
conditions = ["none", "diabetes", "cancer", "hypertension", "arthritis", "asthma", "blindness", "dementia", "chronic bronchitis", "heart disease"]
yes_no_questions = ["y", "n"]

curr_uuid = 0
for i in range(population):

    person = np.array([])

    uuid = str(uuids[curr_uuid])
    gender = random.choice(genders)
    age = str(random.choice(ages))
    profession = random.choice(professions)
    locality = str(random.choice(list(localities.keys())))
    infection_rate = str(random.choice(list(localities.values())))
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
print(df)