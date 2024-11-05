Slovnik_type_znachen = {
    "name": "Pavlo",
    "age": 16,
    "contact_information": {
        "email_adres": "pavlosoroka30gmail.com",
        "city": "Lutsk",
        "country": 'Ukraine',
        "adress": 'Konyakina_5a'
    },
    "Is_student": True
}
type_dict = {}  
for key, value in Slovnik_type_znachen.items():
    if type(value) == dict:
        for k1, v1 in value.items():
            type_dict[k1] = type(v1)
    else:
        type_dict[key] = type(value) 
print(type_dict)
