import requests
url= "https://dog.ceo/api/breeds/image/random"

response= requests.get(url=url)
image= response.json()
print(image)
image_url = image["message"]
print(image_url)
print (response.status_code)

