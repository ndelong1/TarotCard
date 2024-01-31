"""TKINTER WINDOW for User Input of thier Birthdate"""

import tkinter as tk
from tkinter import ttk



class BirthDate:
    def __init__(self):
        """Sets up the screen information for gathering:
        User's Birthdate"""
        
        root = tk.Tk()
        root.title("User's Birthdate")
        
        
        screen = ttk.Frame(root)
        screen.grid(row=0, column=0, padx= 20, pady=20)
        
        #List of the Months
        month_str = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        #List of the Days:
        day_int = [x for x in range(1, 32)]
        
		#List years
        year_int = [x for x in range(1900, 2101)]
        
        
        #Variables to store the listbox selections
        self.selected_month = tk.StringVar()
        self.selected_day = tk.StringVar()
        self.selected_year = tk.StringVar()
        
            
        #print(day_int)
    	#print(year_int)
     
        list_box_month = tk.Listbox(screen, height= 12, selectmode=tk.SINGLE, justify='left', exportselection=False)
        list_box_month.grid(column=1, row=2, padx=5, pady=5)
        for month in month_str:
            list_box_month.insert(tk.END, month)
        
        
        list_box_day = tk.Listbox(screen,listvariable=tk.StringVar(value=day_int), height=12, selectmode=tk.SINGLE, justify='center', exportselection=False)
        list_box_day.grid(column=2, row=2, padx=5, pady=5)

        
        list_box_year = tk.Listbox(screen,listvariable=tk.StringVar(value=year_int), height=12, selectmode=tk.SINGLE, justify=tk.CENTER, exportselection=False)
        list_box_year.grid(column=3, row=2, padx=5, pady=5)

        
        def get_selection():
            if list_box_month.curselection():
                self.selected_month.set(month_str[list_box_month.curselection()[0]])
            else:
                self.selected_month.set("No month selected")

            if list_box_day.curselection():
                self.selected_day.set(day_int[list_box_day.curselection()[0]])
            else:
                self.selected_day.set("No day selected")
            
            if list_box_year.curselection():
                self.selected_year.set(year_int[list_box_year.curselection()[0]])
            else:
                self.selected_year.set("No year selected")

            print("Selected Month:", self.selected_month.get())
            print("Selected Day:", self.selected_day.get())
            print("Selected Year:", self.selected_year.get())
            screen.destroy()
            root.destroy()

        # Button to trigger the function
        submit_button = ttk.Button(screen, text="Submit", command=get_selection)
        submit_button.grid(row=1, column=0, columnspan=2, pady=10)
        
        screen.mainloop()
        
    def get_selected_month(self):
        return self.selected_month.get()
    def get_selected_day(self):
        return self.selected_day.get()
    def get_selected_year(self):
        return self.selected_year.get()
    
    
if __name__ == '__main__':
    app = BirthDate()