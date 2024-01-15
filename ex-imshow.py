import os
from pathlib import Path
import cv2

name = Path("astronaut.png")
if not name.is_file():
  cmd = "wget https://github.com/scikit-image/scikit-image/blob/v0.22.0/skimage/data/astronaut.png?raw=true"
  os.system(cmd)
  files = Path(".").glob("*?raw=true")
  for p in files:
  	new_suffix = p.suffix.replace("?raw=true","")
  	newname = p.with_suffix(new_suffix)
  	p.rename(newname)
img = cv2.imread(str(name))
cv2.imshow("img", img)
key = cv2.waitKey(-1)
cv2.destroyAllWindows()

