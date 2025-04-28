# import tkinter as tk

# window=tk.Tk()
# window.title("CalendarDex")

# window.geometry("540x780")
# window.configure(bg="red")
# frame=None
# def mainInterface():
    
#     frame = tk.Frame(window, bg="green4", bd=3, relief="solid", width=450, height=300)
#     frame.place(relx=0.5, rely=0.3, relheight=0.5, relwidth=0.8, anchor="center")
#     frame.pack_propagate(False)

#     label=tk.Label(frame,text="CalendarDex" ,fg="black")
#     label.pack(padx= 20, pady=20)
    
#     button=tk.Button(frame, text="Select Month", command=monthSelector)
#     button.pack(pady=10, padx=10)
#     window.mainloop()

# def monthSelector():

#     frame = tk.Frame(window, bg="green4", bd=3, relief="solid", width=450, height=300)
#     frame.place(relx=0.5, rely=0.3, relheight=0.5, relwidth=0.8, anchor="center")
#     frame.pack_propagate(False)

#     label=tk.Label(frame,text="Select Month" ,fg="black")
#     label.pack(padx= 20, pady=20)

#     window.mainloop()

import tkinter as tk
from tkinter.font import Font
import functions
import calendar
from datetime import datetime
import random

class CalendarDexApp:

    def __init__(self, window):
        self.window = window
        self.window.title("CalendarDex")
        self.window.geometry("540x780")
        self.window.configure(bg="red")

        # Con esta parte del código se crea el frame y se encapsula para poder reutilizarlo
        self.frame = tk.Frame(self.window, bg="green4", bd=3, relief="solid", width=450, height=300)
        self.frame.place(relx=0.5, rely=0.3, relheight=0.5, relwidth=0.8, anchor="center")
        self.frame.pack_propagate(False)

        # Cargar la pantalla principal al inicio
        self.mainInterface()

    # Método para limpiar el Frame
    def clear_frame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    # Primera interfaz
    def mainInterface(self):
        self.clear_frame()

        label = tk.Label(self.frame, text="CalendarDex", fg="black")
        label.pack(padx=20, pady=20)

        button = tk.Button(self.frame, text="Select Month", command=self.monthSelector)
        button.pack(pady=10, padx=10)

    # Segunda interfaz
    def monthSelector(self):
        self.clear_frame()

        label = tk.Label(self.frame, text="Select Month", fg="black")
        label.grid(row=0, column=0, columnspan=3, pady=10)

        # Agrupamos los meses en una tabla de 3 columnas
        for i in range(3):  
            self.frame.grid_columnconfigure(i, weight=1)

        months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        row, col = 1, 0
        
        # Creamos un botón por cada mes del año
        for month in months:
            btn_font=Font(family="fixedsys", size=14)
            btn=tk.Button(self.frame, text=month, width=10, height=2, bg="OliveDrab1", command=lambda m=month: self.showMonth(m), font=btn_font)
            
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

            col += 1  # Moverse a la siguiente columna
            if col > 2:  # Si llega a la tercera columna, saltar de fila
                col = 0
                row += 1

        button = tk.Button(self.frame, text="Back", command=self.mainInterface)
        button.grid(row=row + 1, column=0, columnspan=3, pady=10)
    
    # Tercera interfaz
    def showMonth(self, month):
        
        all_font=Font(family="fixedsys")

        self.clear_frame()
        
        year = datetime.now().year

        month_number = list(calendar.month_name).index(month)

        _,num_days = calendar.monthrange(year, month_number)

        

        label= tk.Label(self.frame, text=f"{month}", font=all_font, fg="black", bg="OliveDrab1")
        label.grid(row=0, column=0, columnspan=7, pady=(20,10))
        
        for i in range(7):
            self.frame.grid_columnconfigure(i, weight=1)

        row_offset=2
        for day in range(1, num_days + 1):
            row=((day-1)//7)+row_offset
            col=(day-1)%7
            btn = tk.Button(self.frame, text=str(day), width=2, height=2, command=lambda d=day: self.showDay(d,month), font=all_font, fg="black", bg="OliveDrab1")
            btn.grid(row=row, column=col, padx=3, pady= 3, sticky="nsew")
        
        total_rows=((num_days-1) // 7) + row_offset + 1

        button_back = tk.Button(self.frame, text="Back",bg="firebrick1", font=all_font ,command=self.monthSelector)
        button_back.grid(row=total_rows, column=0, columnspan=7, pady=15)

        # # Fuente del texto, se puede regular tanto el tipo de letra como el tamaño.
        # all_font=Font(family="fixedsys")
        # # Cuadro de texto a usar en los días
        # text_area = tk.Text(self.frame, height=5, width=40, bg="OliveDrab1", font=all_font)
        # text_area.pack(pady=10)
        
        # def saveText():
        #     global text 
        #     text = text_area.get("1.0", "end-1c")
            
        # button_save = tk.Button(self.frame, text="Save",bg="OliveDrab1" ,font=all_font, command=lambda: (saveText() ,functions.writeFile(month,text)))
        # button_save.pack(pady=10, padx=10)

        # button_back = tk.Button(self.frame, text="Back",bg="firebrick1", font=all_font ,command=self.monthSelector)
        # button_back.pack(pady=10, padx=10)

    def showDay(self, day, month):
        self.clear_frame()

        text = functions.readFile(day, month)

        all_font=Font(family="fixedsys")

        label= tk.Label(self.frame, text=f"{day} of {month}", font=all_font, fg="black", bg="OliveDrab1")
        label.pack(padx=20, pady=20)
        
        # Fuente del texto, se puede regular tanto el tipo de letra como el tamaño.
        all_font=Font(family="fixedsys")
        # Cuadro de texto a usar en los días
        text_area = tk.Text(self.frame, height=5, width=40, bg="OliveDrab1", font=all_font)
        text_area.pack(pady=10)
        text_area.insert("1.0", text)
        
        def saveText():
            current_text = text_area.get("1.0", "end-1c")
            functions.writeFile(month, day, current_text)
            
        button_save = tk.Button(self.frame, text="Save",bg="OliveDrab1" ,font=all_font, command=saveText)
        button_save.pack(pady=10, padx=10)

        button_back = tk.Button(self.frame, text="Back",bg="firebrick1", font=all_font ,command=self.monthSelector)
        button_back.pack(pady=10, padx=10)

    def pokemonGueser(self, day, month):
        self.clear_frame()

        all_font=Font(family="fixedsys")

        label= tk.Label(self.frame, text="Who is that pokemon?", font=all_font, fg="black", bg="OliveDrab1")
        label.pack(padx=20, pady=20)

        pokemonId=random.randint(1,493)

# Ejecutar la aplicación solo si el script es el principal
# if __name__ == "__main__":
#     window = tk.Tk()
#     app = CalendarDexApp(window)
#     window.mainloop()