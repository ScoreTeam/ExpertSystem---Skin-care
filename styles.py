# styles.py
import tkinter as tk
from tkinter import ttk

def configure_styles():
    style = ttk.Style()
    
    style.configure("Intro.TLabel", background="light green", font=('Arial', 20))
    style.configure("Intro.TFrame", background="light green", font=('Arial', 30), padding=20)
    
    style.configure('IP.TLabel', background="light green", font=('Trebuchet MS', 18), padding=20)
    style.configure('IP.TButton', font=('Arial', 18), padding=10, background='lightblue')
    
    style.configure("TFrame", background="light green", font=('Arial', 30), padding=20,borderwidth=5,relif='ridge')
    # style.configure("TFrame", background="light green", font=('Arial', 30), padding=20)
    style.configure('TLabel', background="light green", font=('Trebuchet MS', 18,'bold'), padding=20)
    style.configure('TButton', font=('Arial', 18), padding=10, background='lightblue')
    
    style.configure('Custom.TRadiobutton', font=('Comic Sans MS', 18,), background='lightgreen')
    style.map('Custom.TRadiobutton', background=[('active', 'green'), ('disabled', 'lightgreen')],cursor="circle")
    
    # Default style
    style.configure('TProgressbar', thickness=20)
    
    # Custom style 1 - Blue bar with rounded corners
    style.configure('Blue.Horizontal.TProgressbar', troughcolor='lightgrey', background='blue', thickness=20)
    style.layout('Blue.Horizontal.TProgressbar',
                 [('Horizontal.Progressbar.trough', {'children': [('Horizontal.Progressbar.pbar', {'side': 'left', 'sticky': 'ns'})], 'sticky': 'nswe'})])

    # Custom style 2 - Green bar with height and padding
    style.configure('Green.Horizontal.TProgressbar', troughcolor='lightgrey', background='green', thickness=30, padding=10)
    
    # Custom style 3 - Striped style
    style.configure('Striped.Horizontal.TProgressbar', troughcolor='lightgrey', background='red', thickness=20)
    style.configure('Striped.Horizontal.TProgressbar', 
                    troughcolor='grey', background='#4f4', bordercolor='black', lightcolor='white', darkcolor='blue')
    
    # Custom style 4 - Light Blue bar with different thickness
    style.configure('LightBlue.Horizontal.TProgressbar', troughcolor='white', background='lightblue', thickness=15)

# Now import this module in your main file and call the function to apply these styles.
