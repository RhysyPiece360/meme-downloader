import requests
import os
import random
import time
# Create a folder to save the memes if it doesn't already exist
if not os.path.exists('memes'):
    os.makedirs('memes')

# Ask the user how many memes they want to download
num_memes = int(input('How many memes do you want to download? '))

for i in range(num_memes):
    sleep(2)
    # Make a GET request to the API endpoint
    response = requests.get('https://meme-api.com/gimme')

    # Get the image URL and file extension from the response JSON
    image_url = response.json()['url']
    file_ext = os.path.splitext(image_url)[-1]

    # Generate a random 4-digit number to append to the file name
    random_num = random.randint(1000, 9999)

    # Define the file name with the random number and extension
    file_name = f'meme_{random_num}{file_ext}'

    # Send a GET request to the image URL and save the image to the memes folder
    image_response = requests.get(image_url)
    with open(f'memes/{file_name}', 'wb') as f:
        f.write(image_response.content)

    print(f'Meme {i+1} downloaded and saved as {file_name} in the memes folder.')
