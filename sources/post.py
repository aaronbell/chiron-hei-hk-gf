import glob
import shutil
from pathlib import Path
import os
import ufoLib2
from fontTools.ttLib import TTFont

for file in Path("fonts/variable").glob("*.ttf"):
	font = TTFont(file)

	font["name"].setName("Chiron Hei HK",1,3,1,1033)
	
	uniqueName = str(font["name"].getName(3,3,1,1033))
	if "Italic" in uniqueName:
		font["name"].setName(uniqueName.replace("ExtraLight",""),3,3,1,1033)
	else:
		font["name"].setName(uniqueName.replace("ExtraLight","Regular"),3,3,1,1033)

	fullName = str(font["name"].getName(4,3,1,1033))
	font["name"].setName(fullName.replace(" ExtraLight",""),4,3,1,1033)
	
	psName = str(font["name"].getName(6,3,1,1033))
	if "Italic" in psName:
		font["name"].setName(psName.replace("ExtraLight",""),6,3,1,1033)
	else:
		font["name"].setName(psName.replace("ExtraLight","Regular"),6,3,1,1033)

	font.save(file)