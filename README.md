# -Attendance_FaceRecognition
# 🎯 Attendance Using Face Recognition System

This project automates student attendance marking using **facial recognition technology**.  
It captures students’ faces in real-time, compares them with stored face data, and records attendance automatically.

## 🚀 Features
- Real-time **face detection and recognition**  
- **Automated attendance marking** and report generation  
- Exports attendance reports in **Excel format**  
- **Secure data storage** using a local or cloud database  
- **User-friendly interface** for both faculty and students  

## 🧱 Tech Stack
| Component | Technology Used |
|------------|----------------|
| Programming Language | Python |
| Libraries | OpenCV, Dlib, face_recognition, NumPy, Pandas |
| Framework (optional) | Flask |
| Database | SQLite / MySQL |
| Tools | PyCharm / VSCode |

## ⚙️ Setup Instructions
```bash
pip install opencv-python dlib face_recognition numpy pandas flask
python src/face_recognition_main.py
```

## 📂 Folder Structure
```
src/
 ├── face_detection.py
 ├── face_recognition_main.py
 ├── database_handler.py
 ├── report_generator.py
 └── app.py
```

## 🔍 Future Enhancements
- Integrate **deep learning models (CNNs)** for improved accuracy  
- Build a **mobile app** for attendance tracking  
- Add **multi-biometric support** (e.g., fingerprint + face)  
- Implement **cloud-based dashboards** for analytics  

## 👥 Team Members
- **T. Akhil Singh**  
- **Tunk Ashwin Raj**  
- **Singireddy Rohith**  
- **K. Nikhil Chary**  

**Guided by:** Mr. Radhe Shyam Panda (Assistant Professor, CMREC)
