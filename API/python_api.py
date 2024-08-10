# API KEY : abcc758ec39ede0fba77b215e890256fed45a2c6edd86e36668564be194535cbb6eb95d8d25a3cb0

# weather app api with endpoint 
# import requests

# api_key = "0e19937b6842f72222a2224b867b3f1c"
# endpoint = "https://api.openweathermap.org/data/3.0/onecall?api_key=0e19937b6842f72222a2224b867b3f1c"+"&lat=33.44"+"&lon=-94.04"
# #endpoint = "https://api.openweathermap.org/data/3.0/onecall?appid=0e19937b6842f72222a2224b867b3f1c"+"&lat=4444"+"&lon=55555"+"&dsfgdfsg=55666"+"&somethingelse=23333"
# headers = {
#     "key": api_key,
#     "Accept":"application/json"
# }
# # data = {"ipAddress":"8.8.8.8"}

# # lat = "?ipAddress=8.8.8.8"

# response = requests.get(endpoint,headers=headers)
# response =requests.post()

# print(response.text)
# print(response.status_code)
# print(response.headers)

# post method
import requests
url = "https://api.themoviedb.org/3/movie/21371631api_key=f491eed2d305a15e44d4fc0850c59759/favorite/movies?language=en-US&page=1&sort_by=created_at.asc"
# url = "https://api.themoviedb.org/3/movie/157336?api_key=f491eed2d305a15e44d4fc0850c59759&append_to_response=videos"

headers = {
    "accept": "application/json",
    "Authorization": "f491eed2d305a15e44d4fc0850c59759"
}

response = requests.get(url, headers=headers)

print(response.text)