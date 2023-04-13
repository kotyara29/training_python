import json
import requests
from urllib.request import urlopen
import shutil
import tkinter as tk
from PIL import ImageTk, Image

def get_image():
    # Get url from website first. If you open this in browser, it shows a dict 'message': url, 'status': 'success'.
    # Initial website we use is: https://dog.ceo/dog-api/documentation/random
    url = 'https://dog.ceo/api/breeds/image/random'
    #Use urlopen to convert url variable from string to http.client.HTTPResponse type.
    url_response = urlopen(url)
    print(type(url_response))
    #Convert url_response to dictionary
    data_json = json.loads(url_response.read())
    print(type(data_json))
    #Get the link from json dictionary
    img_url = data_json.get('message')
    request_response = requests.get(img_url, stream=True)
    with open('image.jpg', 'wb') as f:
        shutil.copyfileobj(request_response.raw, f)

get_image()
# window = tk.Tk()
# window.title("Random Dog Picture")
# window.geometry('800x500')
# frame = tk.Frame(window, width=700, height=400)
# frame.pack()
# frame.place(anchor='center', relx=0.5, rely=0.5)
# image = ImageTk.PhotoImage(Image.open('example.png'))
# label = tk.Label(frame, image=image)
# # btn = tk.Button(window, text="Не нажимать!")
# # btn.grid(column=1, row=0)
# window.mainloop()

