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
        pivot_df = df.pivot_table(index='time_stamp', columns='signal_name', values='value', aggfunc='first')
        
        pivot_df.ffill()
        pivot_df.to_csv(output_directory+"/"+file+"_pivoted.csv")
        A