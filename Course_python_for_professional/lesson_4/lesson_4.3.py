# {
#   "name": "Russia",
#   "phone_code": 7,
#   "capital": "Moscow",
#   "cities": ["Abakan", "Almetyevsk", "Anadyr", "Anapa", "Arkhangelsk", "Astrakhan"],
#   "currency": "RUB"
# }
# Приведенный ниже код:
# import json
# with open('data.json') as file:
#     data = json.load(file)                # передаем файловый объект
#     for key, value in data.items():
#         if type(value) == list:
#             print(f'{key}: {", ".join(value)}')
#         else:
#             print(f'{key}: {value}')

# import json
# lines = {
#          True: 97,
#          2: "I've been running for a reason",
#          "3": ("I", "could", "never", "retain"),
#          4: ["Sweet", "lips", "like", "pink", "lemonade"],
#          5.0: "When he's feeling generous he's gonna give me a taste",
#          "six": "10"
#         }
#
# lines_json = json.dumps(lines)
# lines = json.loads(lines_json)
# print(lines)
































