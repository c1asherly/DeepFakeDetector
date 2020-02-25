import cv2

print("hello world")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(gray, frame):
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	print(faces)


video_capture = cv2.VideoCapture(0)
while True:
  # Read each frame
	if video_capture.read():
		_, frame = video_capture.read()
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		canvas = detect(gray, frame)
		# Show the image in the screen
		cv2.imshow("Video", canvas)
		# Put the condition which triggers the end of program
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		video_capture.release()
		cv2.destroyAllWindows()

