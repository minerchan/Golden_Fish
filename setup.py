import sys
from cx_Freeze import setup, Executable


dependecies = {"packages": ["os"], "includes": ["tkinter", "pyautogui", "colorama", "OpenCV", "threading"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Goldenfish",
    version="0.1",
    description="A macro to make your fishing easier",
    options={"build_exe": dependecies},
    executables=[Executable("app.py", base=base)]
)