import tkinter as tk
from tkinter import messagebox as msgbox

#handling button click event
def button_click():
    #print ("Button clicked!")
    #show an info message box
    msgbox.showinfo("Info", "Welcome to COS102 GUI App!\n")

    #ask user confirmation
    result = msgbox.askyesno("Confimation","Do you want to continue?")

#create the main window
root =  tk.Tk()
root.title("Home Page")
root.geometry("300x100")
    
#add a label widget
label = tk.Label(root,text="Hello Friend\n")
label.pack()
#add a button widget
button = tk.Button(root,text="CLick Me!", command=button_click)
button.pack()
#styling the button
button.config(bg="blue", fg="white", font=("Arial", 12))

#start the main event loop
root.mainloop()

    