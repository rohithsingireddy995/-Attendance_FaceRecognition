import cv2, face_recognition
import numpy as np
import pandas as pd
from datetime import datetime

known_image = face_recognition.load_image_file("dataset/akhil.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]
known_faces = [known_encoding]
known_names = ["Akhil"]

cap = cv2.VideoCapture(0)
attendance = []

while True:
    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        if True in matches:
            name = known_names[matches.index(True)]
            if name not in [x[0] for x in attendance]:
                attendance.append([name, datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
    cv2.imshow("Face Recognition Attendance", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

df = pd.DataFrame(attendance, columns=["Name", "Timestamp"])
df.to_excel("reports/attendance_report.xlsx", index=False)
cap.release()
cv2.destroyAllWindows()
