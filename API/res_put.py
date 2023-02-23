import requests
import subprocess as sp


def get_newId(end_point, nickname):
    res = requests.get(end_point +"?nickname=" + nickname)

    res_json = res.json()

    id = res_json["id"]

    return id

def get_id(key):
    #res = requests.post(end_point + "?nickname=" + nickname)
    #res_json = res.json()
    #print(res_json)
    #print(i)
    challenge_key = key
    
   

    headers = {"X-Challenge-Id": challenge_key}
    
    req = requests.put(end_point, headers=headers)
    
    req_json = req.json()
    print(req_json)

    return challenge_key 

def get_id_from_one(end_point, nickname):
    challenge_key = get_id(end_point,nickname)

    headers = {"X-Challenge-Id": challenge_key}
    
    req = requests.put(end_point, headers=headers)
    
    req_json = req.json()
    print(req_json)

if __name__ == "__main__":
    end_point= ""
    nickname = "shun"

    #key = get_id(end_point, nickname)

    #command = f"curl -X PUT -H X-Challenge-Id:{key} ''"

    res = requests.post(end_point + "?nickname=" + nickname)
    res_json = res.json()
    print(res_json)
    challenge_key = res_json["id"]

    for i in range(50):

        key = get_id(challenge_key)


        






    

