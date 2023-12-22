import typing
import subprocess
import os


UI_FILES_PATH = "assets/ui_files"
TARGET_UI_FOLDER = "ui"


strOldTargetFiles: typing.List[str] = os.listdir(TARGET_UI_FOLDER)

for strOldTargetFile in strOldTargetFiles:
    try:
        os.remove(os.path.join(TARGET_UI_FOLDER, strOldTargetFile))
    except:
        pass


strFiles: typing.List[str] = os.listdir(UI_FILES_PATH)

with open(os.path.join(TARGET_UI_FOLDER, "__init__.py"), "w") as file:
    for strFile in strFiles:
        file.write(f"from .{strFile[:-3]} import *\n")

        subprocess.run(
            [
                "pyuic5",
                os.path.join(UI_FILES_PATH, strFile),
                "-o",
                f"{os.path.join(TARGET_UI_FOLDER, strFile[:-3])}.py",
            ]
        )
