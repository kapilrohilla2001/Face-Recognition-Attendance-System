import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendancerealtime-5ed2f-default-rtdb.firebaseio.com/"
})


ref = db.reference('Students')

data = {
    "20162":
        {
            "Name": "Kapil",
            "Course": "MCA",
            "Section": "2B",
            "Total_Attendance": 6,
            "Starting_Year": 2023,
            "Last_Attendance_Time": "2024-10-11 00:54:34"
        },
    "20163":
        {
            "Name": "Murtaza Hassan",
            "Course": "BCA",
            "Section": "1A",
            "Total_Attendance": 20,
            "Starting_Year": 2022,
            "Last_Attendance_Time": "2024-10-09 00:54:34"
        },

    "20164":
        {
            "Name": "Emili",
            "Course": "BCA",
            "Section": "1B",
            "Total_Attendance": 10,
            "Starting_Year": 2022,
            "Last_Attendance_Time": "2024-10-09 00:54:34"
        },

    "20165":
        {
            "Name": "Elon Musk",
            "Course": "MCA",
            "Section": "2A",
            "Total_Attendance": 5,
            "Starting_Year": 2023,
            "Last_Attendance_Time": "2024-10-11 00:54:34"
        },

}

for key, value in data.items():
    ref.child(key).set(value)
