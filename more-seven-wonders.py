import requests
import time


path = "https://us1.locationiq.com/v1/search.php"
LOCATIONIQ_API_KEY = "pk.a5329fcd810599b01d7c6fa83a6c3871"
wonders = ["Great Wall of China", "Petra", "Colosseum", "Chichen Itza", "Machu Picchu", "Taj Mahal", "Christ the Redeemer"]


#this creates a dict
def get_lat_lon_dict(locations):
    coordinates = {}
    for location in locations:

        query_params = {
            "key": LOCATIONIQ_API_KEY,
            "q": location,
            "format": "json"
        }
        response = requests.get(path, params=query_params)
        response_body = response.json()[0]   #this limits it to first record
        location_coords = {
            "latitude":response_body['lat'],
            "longitude":response_body['lon'],
        }
        coordinates[location] = location_coords
        time.sleep(.25)   
    return coordinates    

print(get_lat_lon_dict(wonders))



# def get_lat_lon(list_of_locations):
#     for location in list_of_locations:

#         query_params = {
#             "key": LOCATIONIQ_API_KEY,
#             "q": location,
#             "format": "json"
#         }
#         response = requests.get(path, params=query_params)
#         response_body = response.json()
    
#         print(f"{location}: {response_body[0]['lat']} , {response_body[0]['lon']}")
#         time.sleep(.25)   

# get_lat_lon(list_of_locations)

# def get_lat_lon(list_of_locations):
#     locations = {}
#     for location in list_of_locations():
#         locations["name"]=location
#     print(locations)    

# dict[query_params["q"] = {
#         "latitude":response_body[0]['lat'],
#         "longitude":response_body[0]['lon'],
# }



# locations.append({search_terms:{"latitude":[response_body[location]['lat']]}})    

# print(get_lat_lon(search_terms))        
# print("/n/n")
# print(f"The lat and lon of {search_term}, also known as {response_body[0]['display_name']}, is {response_body[0]['lat']} , {response_body[0]['lon']} and it is a {response_body[0]['type']} {response_body[0]['class']}")