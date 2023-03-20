api_key = 'e8cf03a48915da2f70adfb45ae906ce940e837c47ba572bb30a8f1b8573df8e8'
file = "./Files/Bonus.png"


import requests

# url = 'https://www.virustotal.com/vtapi/v2/file/scan'

# params = {'apikey': api_key}

# files = {'file': ('myfile.exe', open(file, 'rb'))}

# response = requests.post(url, files=files, params=params)

# print(response.json())

# url = 'https://www.virustotal.com/vtapi/v2/file/report'

# params = {'apikey': api_key, 'resource': 'a7bfa50f7286330af42aefd63ddc6318a7ff5fb4b3ea07597b5868bbf0affcbd'}

# response = requests.get(url, params=params)

# print(response.json())

'''' Normal Scan '''
# import requests

# url = 'https://www.virustotal.com/vtapi/v2/file/scan'

# params = {'apikey': 'e8cf03a48915da2f70adfb45ae906ce940e837c47ba572bb30a8f1b8573df8e8'}

# files = {'file': ('myfile.exe', open('Files/Bonus.png', 'rb'))}

# response = requests.post(url, files=files, params=params)

# print(response.json())

# '''' Report Scan '''
# import requests

# url = 'https://www.virustotal.com/vtapi/v2/file/report'

# params = {'apikey': api_key, 'resource': 'a7bfa50f7286330af42aefd63ddc6318a7ff5fb4b3ea07597b5868bbf0affcbd'}

# response = requests.get(url, params=params)

# print(response.json())

''' URL Scan'''
url = "https://fb.watch/jldEw0RWjs/"

import requests

url = 'https://www.virustotal.com/vtapi/v2/url/scan'

params = {'apikey': api_key, 'url': url}

response = requests.post(url, data=params)

#print(response.json())

# import requests

url = 'https://www.virustotal.com/vtapi/v2/url/report'

params = {'apikey': api_key, 'resource':'https://fb.watch/jldEw0RWjs/'}

response = requests.get(url, params=params)

print(response.json())

# import requests

# url = 'https://www.virustotal.com/vtapi/v2/file/search'

# params = {
#     'apikey': api_key,
#     'query': 'Files/Bonus.png',
#     'offset': 0,
#     'limit': 10,
#     'order': 'first_submission_date'
# }

# response = requests.get(url, params=params)

# if response.status_code == 200:
#     search_results = response.json()
#     for result in search_results['results']:
#         print(result['sha256'])
# else:
#     print('Error: ', response.status_code, response.content)
    
# import requests

# url = 'https://www.virustotal.com/vtapi/v2/file/search'

# params = {'apikey': api_key, 'query': 'a7bfa50f7286330af42aefd63ddc6318a7ff5fb4b3ea07597b5868bbf0affcbd'}

# response = requests.get(url, params=params)

# print(response.json())


# import requests

# url = 'https://www.virustotal.com/vtapi/v2/url/scan'

# params = {'apikey': api_key, 'url':'https://idmcrackeys.com'}

# response = requests.post(url, data=params)

# print(response.json())