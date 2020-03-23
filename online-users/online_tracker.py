import requests, math, time

#greetings
print("Time: ",time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))
print(" ")

#init
target_subreddit = input("r/")
waittime = int(input("How many seconds between updates?"))
subreddit_name = ("r/"+target_subreddit)
counter = 0

headers = {
    "User-Agent": "track online users"
}

def get_active_users(subreddit):
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers=headers)
    if not resp.ok:
        return -1
    content = resp.json()
    return content["data"]["accounts_active"]

#main
while True:
    counter+=1
    timeofget = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
    users = get_active_users(target_subreddit)
    print(subreddit_name , "has", users, "active users as of", timeofget)
    write = (str(counter)+","+str(users)) 
    f = open("plotting.txt","a+")
    f.write(write)
    f.write("\n")

    time.sleep(waittime)
#run plotter for graph
