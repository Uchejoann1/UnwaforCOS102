import tkinter as tk

#handling button click event
def button_click():
    #print ("Button clicked!")
    #show an info message box
    msgbox.showinfo("Info", "Welcome to COS102 GUI App!\n")

    #ask user confirmation
    result = msgbox.askyesno("Confimation","Do you want to continue?")

    #create the main window
    root =  tk.TK()
    root.title("Home Page")
    root.geometry("300x100")
    
    #add a label widget
    label = tk.Label(root,text="Hello Friend\n")
    label.pack()

    #add a button widget
    button = tk.Button(root,text="CLick Me!", command=button_click)
    button.pack()

    