import requests
from requests_oauthlib import OAuth2Session

# Naver API credentials
client_id = 'HN3GGCMDdTgGUfl0kFCo'
client_secret = 'ftZjkkRNMR'
redirect_uri = 'YOUR_REDIRECT_URI'

# Obtain authorization URL
oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)
authorization_url, state = oauth.authorization_url('https://nid.naver.com/oauth2.0/authorize')

print('Please go to {} and authorize access.'.format(authorization_url))
authorization_response = input('Enter the full callback URL: ')

# Fetch the access token
oauth.fetch_token('https://nid.naver.com/oauth2.0/token',
                  authorization_response=authorization_response,
                  client_secret=client_secret)

# Now you can use the token to access Naver Pay API
headers = {
    'Authorization': 'Bearer {}'.format(oauth.token['access_token']),
}

# Request to get receipt data
response = requests.get('https://new-m.pay.naver.com/receipts/history/list/20240101/20240131', headers=headers)

if response.status_code == 200:
    receipt_data = response.json()
    print(receipt_data)
else:
    print("Failed to retrieve data: {}".format(response.status_code))
