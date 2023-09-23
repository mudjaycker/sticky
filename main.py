import webview
from tkinter import Tk
from data.db import API

root = Tk()

sx = root.winfo_screenwidth()
sy = root.winfo_screenheight()


# percent = lambda x, p: (p*x)/100
dev_url = "http://localhost:5173/"
test_url = "dist/index.html"
api = API()
webview.create_window(
    "nakala",
    dev_url,
    background_color="#4f384a",
    width=300,
    height=500,
    on_top=True,
    x=sx - 310,
    y=sy - 550,
    js_api=api,
)
webview.start(debug=True)
