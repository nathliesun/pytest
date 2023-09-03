import requests
import yaml

with open('config.yaml') as file:
    my_dict=yaml.safe_load(file)

url = my_dict['url']
url1 = my_dict['url1']
username = 'AlexeyZ1'
password = 'e23970376f'

# def login(username, password):
# obj_data = requests.post(url=url, data ={'username':username, 'password':password})
# #print(obj_data.json()) #
# token = obj_data.json()['token']
# #print(token)
# return token

def token_auth(token):
    response=requests.get(url=url1, headers={'X-Auth-Token':token}, params={'owner':"notMe"})
    content_var = [item['content'] for item in response.json()['data']]
    return content_var

def test_step2(login):
    assert 'content' in token_auth(login)

def new_post(token):
    requests.post(url=url1, headers={'X-Auth-Token':token}, params={'title':"суббота", 'description':"выходной",'content':"велосипед" })
    response=requests.get(url=url1, headers={'X-Auth-Token':token}, params={'owner':token['username']})
    content_var = [item['title'] for item in response.json()['data']]
    return content_var

def test_step3(login):
    assert {'description':"выходной"} in new_post(login)

#if __name__ == '__main__':
# print(token_auth(login(username,password)))