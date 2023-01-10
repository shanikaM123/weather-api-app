from tkinter import *
import requests
from tkinter import ttk
from tkinter import messagebox

API_KEY = "23f2f1370e52150c180395abdaf62a0f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


screen = Tk()
screen.title('Wheather App')
screen.geometry('500x600')

bg = PhotoImage(file='/Users/shani_magz/Documents/Automation-1/wheather-api-app/009c5944.gif')
my_label = Label(screen,image=bg)
my_label.place(x=0,y=0,relheight=1,relwidth=1)

welcome_text = Label(text='Welcome', fg='red',bg='yellow')
welcome_text.pack()

click_me = Button(text='Enter the City',fg ='blue',bg='black')
click_me.place(x=10,y=20)



def get_wheather_api_details(): 
    name1 = name_storage.get()
    print(name1)
    name.delete(0,END)
    request_url = f"{BASE_URL}?appid={API_KEY}&q={name1}"
    print(request_url)
    respone = requests.get(request_url)

    if respone.status_code == 200:
        data = respone.json()
        print(data)
        wheather = data['weather'][0]['description']
        print(wheather)
        temp = data["main"]['temp']
        print(temp)
        humidity = data["main"]['humidity']
        country = data['sys']['country']
        lbl.config(text = "Tempreature : "+str(temp)
        +"\n"+"Feels Like : " + wheather
        +"\n"+"Humidity : "+ str(humidity)
        +"\n"+"Country : " + country)

    else:
     print('An Error Occured')
     lbl.config(text = "An error occured")

name_storage = StringVar()
name = Entry(textvariable=name_storage)
name.pack()
click_me2 = Button(text='Check the Weather',fg ='blue',bg='black',command=get_wheather_api_details)
click_me2.pack()



lbl =Label(text = "",fg='Blue')
lbl.pack()

screen.mainloop()

