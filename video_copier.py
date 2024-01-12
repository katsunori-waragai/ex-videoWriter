from pathlib import Path
import cv2

import argparse

parser = argparse.ArgumentParser(description="movie copier")
parser.add_argument("src", help="video source")
parser.add_argument("dst", help="video dst")
args = parser.parse_args()

src = Path(args.src)
dst = Path(args.dst)

cap = cv2.VideoCapture(str(src))

r, image = cap.read()

H, W = image.shape[:2]

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter(str(dst), fourcc, 20.0, (W, H))

while True:
    r, image = cap.read()
    if image is None:
        break
    writer.write(image)

writer.release()
