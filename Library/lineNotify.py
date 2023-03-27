import requests
# Set Line Notify API token
#token = '9btZfWSP61xFB608ZyOrGOIGiLaDaJNLnXAVVsxA3JP'
token = '6tA0qnCW3qp6jtAMEVyL2T3CIINiEusqZ3nJH5kuzKL'

# Set image file path
image_path = "D:/Project/Project 1/Code/Files/MessageDigest-QRCode.png"

# Set Line Notify API endpoint
url = "https://notify-api.line.me/api/notify"

while(1):
    
    message = input("Enter Message : ")
    if message == "exit":
        break
    
    # Set headers and payload for the API request
    headers = {"Authorization": "Bearer " + token}
    payload = {"message": message}


    # Open the image file in binary mode and attach it to the payload
    with open(image_path, "rb") as image_file:
        files = {"imageFile": image_file}
        response = requests.post(url, headers=headers, params=payload, files=files)

    # Check if the API request was successful
    if response.status_code == 200:
        print("Image sent successfully!")
    else:
        print("Failed to send image.")
        