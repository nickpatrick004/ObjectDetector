import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)

    output.save("./sounds/output.mp3")
    playsound("./sounds/output.mp3")


# capture video from camera source, 0 being the built-in
video = cv2.VideoCapture(0)
# list of labels we find
labels = []

# always run
while True:
# access camera, and get frame
    ret, frame = video.read()
# get the bbox and label from CV
    bbox, label, conf = cv.detect_common_objects(frame)
# draw the camera plus the box and label
    output_image = draw_bbox(frame, bbox, label, conf)
# display to screen
    cv2.imshow("Object Detection", output_image)

# loop through labels, and append to list
    for item in label:
        if item in labels:
            pass
        else:
            labels.append(item)

# Wait and look for "q"
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Iterator to determine how to speak
i = 0
# Blank sentence list to be appended to
new_sentence = []
# iterate through labels, if new, start sentence, if not new, append to old sentence
for label in labels:
    if i == 0:
        new_sentence.append(f"I found a {label}, and, ")
    else:
        new_sentence.append(f"a {label}")

    i += 1

speech(" ".join(new_sentence))