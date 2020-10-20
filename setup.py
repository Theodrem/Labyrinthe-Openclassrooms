from cx_Freeze import setup, Executable

setup(
    name="Maze",
    version="1.0",
    description="The maze game",
    executables=[Executable("main.py")])
