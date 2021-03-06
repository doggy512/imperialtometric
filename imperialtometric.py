import tkinter as tk


def main():

    #This section is what converts from mi to km. The window is created using
    #window.geometry and there is also a button to convert. The miles the
    #user inputs are multiplied by 1.609 and then it will output.
    window= tk.Tk()
    window.title("Miles to Kilometres")
    window.geometry("400x200")
    
    sec1 = tk.Label(window, text="Miles:")
    
    sec2 = tk.Label(window, text="Kilometres:")

    sec1.place(x=30,y=20)
    
    textbox1 = tk.Entry(window, width=10)

    textbox1.place(x=200,y=35)
    
    sec2.place(x=50,y=100)

    sec3 = tk.Label(window, text=" ")

    sec3.place(x=180,y=100)

         
    def button1_click():
        kilometres = round(float(textbox1.get()) * 1.609,5)
        sec3.configure(text = str(kilometres)+ '  Kilometres')
        

    #This section converts from lbs to kg. Again, the window and button are created
    #and lbs is multiplied by 0.45 and it outputs.
    button1 = tk.Button(window, text="Convert", command=button1_click)
    button1.place(x=100,y=150)
    window.mainloop()

    window= tk.Tk()
    window.title("Pounds to Kilograms")
    window.geometry("400x200")
    
    sec1 = tk.Label(window, text="Pounds:")
    
    sec2 = tk.Label(window, text="Kilograms:")

    sec1.place(x=30,y=20)
    
    textbox1 = tk.Entry(window, width=10)

    textbox1.place(x=200,y=35)
    
    sec2.place(x=50,y=100)

    sec3 = tk.Label(window, text=" ")

    sec3.place(x=180,y=100)

         
    def button1_click():
        kilograms = round(float(textbox1.get()) * 0.45,5)
        sec3.configure(text = str(kilograms)+ '  Kilograms')
        

    #This section converts from fl oz to ml. The window and button are created
    #and then fl oz is multiplied by 29.57 then outputs.
    button1 = tk.Button(window, text="Convert", command=button1_click)
    button1.place(x=100,y=150)
    window.mainloop()

    window= tk.Tk()
    window.title("Fluid Ounces to Millilitres")
    window.geometry("400x200")
    
    sec1 = tk.Label(window, text="Fluid Ounces:")
    
    sec2 = tk.Label(window, text="Millilitres:")

    sec1.place(x=30,y=20)
    
    textbox1 = tk.Entry(window, width=10)

    textbox1.place(x=200,y=35)
    
    sec2.place(x=50,y=100)

    sec3 = tk.Label(window, text=" ")

    sec3.place(x=180,y=100)

         
    def button1_click():
        millilitres = round(float(textbox1.get()) * 29.57,5)
        sec3.configure(text = str(millilitres)+ '  Millilitres')
        

    button1 = tk.Button(window, text="Convert", command=button1_click)
    button1.place(x=100,y=150)
    window.mainloop()
    

main()
