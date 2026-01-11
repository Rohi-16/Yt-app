import streamlit as st
import yt_dlp
import os

st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube Video URL")

if url:
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }

    if st.button("Download"):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)

        if os.path.exists(file_name):
            with open(file_name, "rb") as file:
                st.download_button(
                    label="Click to Download Video",
                    data=file,
                    file_name=os.path.basename(file_name),
                    mime="video/mp4"
                )
            st.success("Video Ready!")
        else:
            st.error("Download failed!")