import streamlit as st
from pathlib import Path
import os
import datetime

st.title("ZeroX")

st.markdown("")
with st.form(key="Form :",clear_on_submit=True):
    Name=st.text_input("Enter your name: ")
    Files=st.file_uploader(label="Upload file",type=["pdf","docx","png","jpeg","jpg"],accept_multiple_files=True)
    Submit=st.form_submit_button(label='Submit')
if Submit:
    new_dir=Name+'_'+datetime.datetime.now().time().strftime("%I-%M-%S %p")
    save_folder=os.path.join('F:\zeroX\scan',new_dir.replace(' ','_'))
    os.makedirs(save_folder, exist_ok=True)
    for File in Files:
        save_path=Path(save_folder,File.name)
        with open(save_path,mode='wb') as w:
            w.write(File.getvalue())
        if save_path.exists():
            st.success(f'File{File.name} is successfully saved!') 