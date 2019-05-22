import distutils
import time
import mss
import numpy
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from accessible_output2.outputs.auto import *
from difflib import SequenceMatcher

output = Auto()
old_text = ""

def similar(a, b):
	return SequenceMatcher(None, a, b).ratio()

output.output("Subtitle reader started. Now simply watch something with subtitles in full screen")
with mss.mss() as sct:
	#monitor = {'top': int(sct.monitors[0]["height"])-300, 'left': 200, 'width': int(sct.monitors[0]["width"]-200), 'height': int(sct.monitors[0]["height"]/2)}
	monitor = {'top': int(sct.monitors[0]["height"]-250), 'left': 0, 'width': sct.monitors[0]["width"]-200, 'height': int(180)}
	while True:
		img_data = numpy.array(sct.grab(monitor))
		im = Image.fromarray(img_data)
		text = pytesseract.image_to_string(im, config="-l eng --psm 3")
		text = ''.join(e for e in text if e.isalnum() or e == " " or e == "," or e == ".")
		if similar(old_text, text) < 0.5:
			old_text = text
			print(text)
			print("")
			output.output(text)
		time.sleep(.005)

