from tkinter import *
import requests
import json
from PIL import Image,ImageTk
from io import StringIO


def wheather():

    api_key = "43892e929efd4d397accbe15a9549cb9"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = city_value.get()

    information_url = base_url + "q="+ city_name+ "&appid=" + api_key
    response = requests.get(information_url)
    responses= response.json()



    if responses["cod"] !="404" :

        #print (responses)
        main_key = responses["main"]

        current_temperature = main_key["temp"]

        current_pressure = main_key["pressure"]

        current_humidity = main_key["humidity"]

        maximum_temp = main_key["temp_max"]

        minimum_temp = main_key["temp_min"]

        weath= responses["weather"]
        wheather_description =weath[0]["description"]

        coord= responses["coord"]
        long=coord["lon"]
        lang=coord["lat"]


        temp_value.insert(20, str(current_temperature)+" kelvin")
        pressure_value.insert(20,str(current_pressure)+ " hpa")
        humidity_value.insert(20,str(current_humidity)+ " %")
        descp_value.insert(200,str(wheather_description))
        max_temp_value.insert(20,str(maximum_temp)+" kelvin")
        min_temp_value.insert(20,str(minimum_temp)+" kelvin")
        longitude_value.insert(20,str(long));
        langitude_value.insert(20,str(lang));

    else:

        messagebox.showerror("Error","invalid city name\n")

        city_value.delete(0,END)


def clear_all():
    city_value.delete(0,END)
    temp_value.delete(0,END)
    pressure_value.delete(0,END)
    humidity_value.delete(0,END)
    descp_value.delete(0,END)
    max_temp_value.delete(0,END)
    min_temp_value.delete(0,END)
    langitude_value.delete(0,END)
    longitude_value.delete(0,END)
    
    city_value.focus_set()


def ex():
    root.destroy()
    
def start():

    #create Gui
    global root,city_value,temp_value,pressure_value,humidity_value,descp_value,max_temp_value,min_temp_value
    global langitude_value,longitude_value
    root=Tk()
    root.title("wheather forecast")
    root.config(bg='lightblue')
    root.geometry("640x420")

    right=ImageTk.PhotoImage(Image.open("image/weather.GIF"))
    Label(root,image=right).place(x=0,y=0)

    city_name =Label(root, text ="Enter City Name  ", fg='black',bg='light blue')
    city_name.place(x=350,y=30)

    temperature =Label(root , text="Temperature - ",fg='black', bg='light blue')
    temperature.place(x=360,y=130)

    humidity =Label(root, text="Humidity - ",fg='black',bg='light blue')
    humidity.place(x=360,y=160)

    pressure=Label(root,text="Atm_pressure",fg='black',bg='light blue')
    pressure.place(x=360,y=190)

    description =Label(root,text="Description",fg='black',bg='light blue')
    description.place(x=360,y=220)

    max_temp=Label(root, text="Maximum Temperature",fg='black',bg='light blue')
    max_temp.place(x=360,y=250)

    min_temp=Label(root,text="Minimum Temperature",fg="black",bg="light blue")
    min_temp.place(x=360,y=280)

    langitude=Label(root,text="Langitude",fg="black",bg="light blue")
    langitude.place(x=360,y=310)

    longitude=Label(root,text="Longitude",fg="black", bg="light blue")
    longitude.place(x=360,y=340)

    city_value = Entry(root)
    city_value.place(x=350,y=50)


    temp_value = Entry(root)
    temp_value.place(x=500,y=130)

    pressure_value = Entry(root)
    pressure_value.place(x=500,y=160)

    humidity_value = Entry(root)
    humidity_value.place(x=500,y=190)

    descp_value = Entry(root)
    descp_value.place(x=500,y=220)

    max_temp_value =Entry(root)
    max_temp_value.place(x=500,y=250)

    min_temp_value =Entry(root)
    min_temp_value.place(x=500,y=280)

    langitude_value=Entry(root)
    langitude_value.place(x=500,y=310)

    longitude_value=Entry(root)
    longitude_value.place(x=500,y=340)


    submit = Button(root,text="submit" , bg="light blue", fg="black",activeforeground="red",command=wheather)
    submit.place(x=480,y=50)

    clear =Button(root,text="Clear",bg="light blue",fg='black',command=clear_all)
    clear.place(x=500,y=370)

    exi= Button(root,text="Exit",bg="lightblue",fg="black",command= ex)
    exi.place(x=360,y=370)
    root.mainloop()
start()
    

    
