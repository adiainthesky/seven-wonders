import requests

path = "https://us1.locationiq.com/v1/search.php"

LOCATIONIQ_API_KEY = "pk.a5329fcd810599b01d7c6fa83a6c3871"
search_term = "Great Wall of China"
query_params = {
    "key": LOCATIONIQ_API_KEY,
    "q": search_term,
    "format": "json"
}

response = requests.get(path, params=query_params)

response_body = response.json()

print("/n/n")
print(f"The lat and lon of {search_term}, also known as {response_body[0]['display_name']}, is {response_body[0]['lat']} , {response_body[0]['lon']} and it is a {response_body[0]['type']} {response_body[0]['class']}")
