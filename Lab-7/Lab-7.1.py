import json

file_path = '/Red_Light_Camera_Violations_2023.json'


with open("Red_Light_Camera_Violations_2023.json") as file:
    data = json.load(file)


# print(data)
# print(type(data))

lstIntersections = [feature['properties']['INTERSECTION']for feature in data['features']]

lstStreetNames = sorted(set(street.strip().lower().title() for intersection in lstIntersections for street in intersection.split('@')))

lstToSanitize = [name for name in lstStreetNames if '/' in name]

lst1 = sorted(set(lstStreetNames).symmetric_difference(set(lstToSanitize)))

sanitizedStreets = sorted(set(street.strip() for name in lstToSanitize for street in name.split('/')))

lstOfStreets = sorted(set(lst1 + sanitizedStreets))

lstIntersections[:5] , lstStreetNames[:5], lstToSanitize[:5], lst1[:5], lstOfStreets[:5]

# print(lstOfStreets)


