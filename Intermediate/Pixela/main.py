import requests 

USERNAME = "henrippppp"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"
COLORS = ["momiji", "momiji", "momiji"]
TOKEN = " gzrgzgzrhgziughzigjzrgagaegage"

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
params = {"token":TOKEN, 
          "username":USERNAME, 
          "agreeTermsOfService":"yes", 
          "notMinor":"yes"}

post =  requests.post(url=GRAPH_ENDPOINT, json=params, verify=False)
print(post.status_code)
 


