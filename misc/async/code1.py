import aiohttp
import asyncio
import time

url = "https://api.nationalize.io/?name={}"
names = ["Liam","Olivia","Noah","Emma","Oliver","Charlotte","Elijah","Amelia","James","Ava","William","Sophia","Benjamin","Isabella","Lucas","Mia","Henry","Evelyn","Theodore","Harper"]
results = []

def get_task(session):
    tasks = []
    for name in names:
        tasks.append(session.get(url.format(name),ssl=False))
    return tasks

async def get_name(names):
    async with aiohttp.ClientSession() as session:
        task = get_task(session)
        responses = await asyncio.gather(*task)
        for response in responses:
            results.append(await response.json())
try:
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_name(names))
    print("time to run is {}".format(time.time() - start)) # print the time it took to run the code
except Exception as e:
    loop.close()    

    
#####################################
# time to run is 0.9785981178283691 #
#####################################


# start = time.time()
# async def get_name(names):
#     async with aiohttp.ClientSession() as session:

#         for name in names:
#             r = await session.get(url.format(name),ssl=False)
#             print(await r.json()) # print the json response

# try:
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(get_name(names))
#     print("time to run is {}".format(time.time() - start)) # print the time it took to run the code
# except Exception as e:
#     loop.close()    
    
####################################
# time to run is 5.099673509597778 #
####################################

# import requests

# start = time.time()

# for name in names:
#     r = requests.get(url.format(name))
#     print(r.json()) # print the json response

# print(time.time() - start) # print the time it took to run the code

#####################################
# time to run is 17.480331420898438 #
#####################################
