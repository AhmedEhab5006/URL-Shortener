#importing libraries
import customtkinter
from customtkinter import *
import pyperclip
import pyshorteners
from tkinter import messagebox as msg



#creating shorten function which shortens URL
def shorten () :
    global URL
    URL = URL_entry.get()
    if URL == "" :
        error_label = customtkinter.CTkLabel(root , text_color = "red" , text = "You must enter a link")
        error_label.place(x = 328 , y = 230 )
    else :
        try :
            Shortened_URL = pyshorteners.Shortener().tinyurl.short(URL)
            URL = Shortened_URL
            Shortened_URL_label = customtkinter.CTkLabel(root , text_color = "green" , text = f"Shortened URL : {Shortened_URL}")
            Shortened_URL_label.place(x = 150 , y = 370)
            copy_btn = customtkinter.CTkButton(root , text = "Copy URL" , command = Copy , fg_color = "red")
            copy_btn.place(x = 560  , y = 370)
        except :
            msg.showerror(title = "URL Shortener" , message = "An error occurred")




#creating copy function which copies URL to the clipboard
def Copy () :
    global URL
    pyperclip.copy(URL)
    copy_btn = customtkinter.CTkButton(root, text="Copied!" , fg_color = "green")
    copy_btn.place(x=560, y=370)
    msg.showinfo(title = "URL Shortener" , message = "URL is copied to clipboard" )




#creating app's window
root = CTk ()
URL = ""
#setting the theme to light mode as a default choice
customtkinter.set_appearance_mode("Light")



#creating a function for dark mode switch which sets the theme to dark mode
def Set_theme () :
    theme = theme_switch.get()
    if theme == 1 :
        customtkinter.set_appearance_mode("Dark")
    else :
        customtkinter.set_appearance_mode("Light")


root.title("URL Shortener")
root.iconbitmap("Elements\\Images\\icon.ico")
root.resizable(False , False)
root.geometry("780x488")
customtkinter.deactivate_automatic_dpi_awareness()
theme_switch = customtkinter.CTkSwitch(root , text = "" , switch_width = 70 , command = Set_theme , offvalue = 0 , onvalue = 1 )
theme_switch.place(x = 50 , y = 440)
dark_mode_text = customtkinter.CTkLabel(root , text = "Dark mode")
dark_mode_text.place(x = 53 , y = 410)
title_label = customtkinter.CTkLabel(root , text = "URL Shortener" , font = customtkinter.CTkFont(size = 30))
title_label.place(x = 297 , y = 75)
URL_entry = customtkinter.CTkEntry(root , placeholder_text = "Enter a URL" , width = 400)
URL_entry.place(x = 195 , y = 180 )
shorten_btn = customtkinter.CTkButton(root , text = "Shorten" , command = shorten)
shorten_btn.place(x = 320 , y = 300)
root.mainloop()