import streamlit as st
import pandas as pd
import shutil
import os

# Create a folder to save uploaded files, if it doesn't exist
save_folder = "uploaded_files"
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

fl = st.file_uploader(":file_folder: Upload a file", type=(["json"]))

if fl is not None:
    filename = fl.name
    st.write(f"You uploaded {filename}")
    
    # Save the file in the 'uploaded_files' folder
    with open(os.path.join(save_folder, filename), "wb") as f_out:
        f_out.write(fl.read())
        
    saved_file_path = os.path.join(save_folder, filename)
    
    # Now read the saved file into a DataFrame
    df_2 = pd.read_json(saved_file_path, encoding = "ISO-8859-1")

else:
    df_2 = pd.read_json(r'\\rbsres01\shareddata\rassre\AIMLData\TNTR\TNTR_trade_prodprl_sample_sept.json\TNTR_trade_prodprl_sample_sept.json')

# Rest of your code
