import cx_Freeze
import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tk8.6"
executables = [cx_Freeze.Executable("GAME.py")]#here are the things to be executed

cx_Freeze.setup(
    name="BALL RUNNER",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["detective.png"]}},
    executables=executables

    )

