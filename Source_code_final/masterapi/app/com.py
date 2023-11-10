import requests
api_url = "http://redisapi"
api_get_url = ["http://redisapi/view","http://redisapi2/view"]
api_post_url = ["http://redisapi/add","http://redisapi2/add"]

load_balancer_counter = 0

def get_data():
    print("Convey the request to work node:GET operation")
    load_balancer_counter = load_balancer_counter + 1
    response = requests.get(api_get_url[load_balancer_counter % 2])
    return response.json()
    
def post_data(object):    
    print("Convey the request to work node:POST operation")
    load_balancer_counter = load_balancer_counter + 1
    response = requests.post(api_post_url[load_balancer_counter % 2], json=object)
    return response.json()