import random
import cv2
import numpy as np

frames = []
path = "test6.mp4"
cap = cv2.VideoCapture(path)
ret = True
while ret:
    ret, img = cap.read()  # read one frame from the 'capture' object; img is (H, W, C)
    if ret:
        frames.append(img)
video = np.stack(frames, axis=0).astype('uint8')

print(video.shape)

num_frames, height, width, _ = video.shape

writer = cv2.VideoWriter("output.mp4",
                         cv2.VideoWriter_fourcc(*"mp4v"), 30, (num_frames, height))
cadr = np.empty([height, num_frames, 3]).astype('uint8')

for frame in range(width):
    for i in range(num_frames):
        for j in range(height):
            for k in range(3):
                cadr[j, i, k] = video[i, j, frame, k]

    writer.write(cadr)
    print(frame, "/", width)

writer.release()
