import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file = filedialog.askopenfile()
df = pd.read_csv(file.name)
# Pivot your data
pivot_df = df.pivot_table(index='time_stamp', columns='signal_name', values='value', aggfunc='first')

# Optionally, fill missing values
pivot_df.ffill()
file,extension = os.path.splitext(file.name)
directory = filedialog.askdirectory()
print(directory+"/"+os.path.basename(file)+"_pivoted.csv")
pivot_df.to_csv(directory+"/"+os.path.basename(file)+"_pivoted.csv")