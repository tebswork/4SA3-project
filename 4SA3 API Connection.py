#numverify account verification 
import requests

def validate_phone_number(api_key, phone_number):
    url = "http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        if data['valid']:
            print("Phone number {phone_number} is valid.")
            print("Country: {data['country_name']}")
            print("Location: {data['location']}")
            print("Carrier: {data['carrier']}")
            print("Line type: {data['line_type']}")
        else:
            print("Phone number {phone_number} is not valid.")
    else:
        print("Error: {data['error']['info']}")

# Example usage
api_key = 'a40d54f61826e669765590dfb48340b0'
#phone_number = '14374337015'

#To user 
phone_number = input("Please enter your phone number to sign up for text notifications from TrackMe.")
print("The number you have entered is: " + phone_number)
validate_phone_number(api_key, phone_number)
