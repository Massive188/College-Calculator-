import tkinter as tk
from tkinter import ttk #translating tkinter to ttk
#Buttons 

def CalculateButton():
    Total_num = int(HouseText.get()) #.
    Total_house = int(VehicleText.get())
    Total_college = int(CollegeText.get())
    Total_electric = int(ElectricText.get())
    Total_heat = int(HeatText.get())
    Total_entertain=int(EntertainmentText.get())
    Total_internet = int(InternetText.get())
    
    Results = Total_num + Total_house + Total_college + Total_electric + Total_heat + Total_entertain + Total_internet#do the math
   
    TotalText.set(round(Results,1))

def ExitButton():
    window.destroy()
    

#Create a root window 
window = tk.Tk()
window.title('Bill Calculator')
window.geometry('300x300')


#Create frame and add it to the root window.
frame = ttk.Frame(window, padding= '10 10 10 10')#frame from Top, bottom, Left and Right
frame.pack(fill=tk.BOTH, expand=True)



#Create labels and textfields and place them on the frame grid

ttk.Label(frame, text="House Bill:").grid(column=0, row=0, padx=5,
                                          pady=5, sticky=tk.W) # House bill position and collision prevention(pads(x and y axis), object leaning to the west (sticky)

ttk.Label(frame, text="Vehicle Bill:").grid(column=0, row=1, padx=5,
                                            pady=5, sticky=tk.W) # Vehicle bill position and collision prevention(pads(x and y axis), object leaning to the west (sticky)

ttk.Label(frame, text="College Bill:").grid(column=0, row=2, padx=5,
                                            pady=5, sticky=tk.W) # College bill position and collision prevention(pads(x and y axis), object leaning to the west (sticky)

ttk.Label(frame, text="Electric Bill:").grid(column=0, row=3, padx=5,
                                             pady=5, sticky=tk.W) # Electric bill position and collision prevention(pads(x and y axis), object leaning to the west (sticky)

ttk.Label(frame, text="Heat Bill:").grid(column=0, row=4, padx=5,
                                         pady=5, sticky=tk.W) # Heat bill position and collision prevention(pads(x and y axis), object leaning to the west (sticky)

ttk.Label(frame, text="Entertainment Bill:").grid(column=0, row=5, 
                                                  padx=5, pady=5, sticky=tk.W) # entertainment bill position and collision prevention(pads(x and y axis), object leaning to the west (sticky)

ttk.Label(frame, text="Internet Bill:").grid(column=0, row=6, 
                                             padx=5, pady=5, sticky=tk.W) # Internet bill position and collision prevention(pads(x and y axis), object leaning to the west (sticky)

HouseText = tk.StringVar()
ttk.Entry(frame, width= 25, 
          textvariable=HouseText).grid(column=1, row= 0)

VehicleText = tk.StringVar()
ttk.Entry(frame, width= 25, 
          textvariable=VehicleText).grid(column=1, row=1)

CollegeText = tk.StringVar()
ttk.Entry(frame, width= 25, 
          textvariable=CollegeText).grid(column=1, row=2)

ElectricText =tk.StringVar()
ttk.Entry(frame, width= 25, 
          textvariable=ElectricText).grid(column=1, row=3)

HeatText = tk.StringVar()
ttk.Entry(frame, width= 25, 
          textvariable=HeatText).grid(column=1, row=4)

EntertainmentText = tk.StringVar()
ttk.Entry(frame, width=25, 
          textvariable=EntertainmentText).grid(column=1, row=5)

InternetText = tk.StringVar()
ttk.Entry(frame, width=25, 
          textvariable=InternetText).grid(column=1, row=6)


#Create buttons and add them to the frame
ttk.Button(frame, text="Calculate", command=CalculateButton).grid(column=0, row=7, 
                                         padx=5, pady=5, sticky=tk.E)

ttk.Button(frame, text="Exit",command = ExitButton).grid(column=1, row=7,
                                    padx=5, pady=5, sticky=tk.W)

#Create output textfield and make it readonly
ttk.Label(frame, text="Total:").grid(column=0, row=10, 
                                             padx=3, pady=3, sticky=tk.E)
TotalText = tk.StringVar()
ttk.Entry(frame, width=25, textvariable=TotalText, state='readonly').grid(column=1, row=10)

window.mainloop()
