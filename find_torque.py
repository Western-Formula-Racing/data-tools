import tkinter as tk
from tkinter import filedialog
import os
import pandas as pd


root = tk.Tk()
root.withdraw()
directory = filedialog.askdirectory()
output_directory = filedialog.askdirectory()

for filename in os.listdir(directory):
    file,extension = os.path.splitext(filename)
    if extension == ".csv":
        df = pd.read_csv(directory+"/"+filename)
        if (df['torqueRequest']>200).any():
            print(directory+"/"+filename +": "+ (str)( os.path.getsize(directory+"/"+filename)))