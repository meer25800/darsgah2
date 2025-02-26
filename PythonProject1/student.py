import streamlit as st
import pandas as pd
import requests
from PIL import Image
import base64
import os
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
    return encoded

# Path to the logo


logo_path = "/mount/src/darsgah2/PythonProject1/q.png"
if not os.path.exists(logo_path):
    print(f"File not found: {logo_path}")

# Get base64 string of the image
logo_base64 = get_image_base64(logo_path)

# Title page


# Set page configuration
st.set_page_config(page_title="Darsgah Taleemul Quran Wal Hadith Kongamdara", page_icon="📘")
st.markdown("""
    <style>
        /* Change background color to white */
        .stApp {
           background-color: #c975d2;

        }
    </style>
""", unsafe_allow_html=True)
st.markdown("""
    <style>
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: #af6382;

        color: #be5f25;
        border-radius: 10px;
        box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2);
        padding-left: 15px;
        padding-right: 15px;
    }
    
    /* Sidebar text color */
    .css-1v3fvcr {
        color: #2e2e3a;
    }
    
    /* Adjust selectbox style */
    .css-1n543e5 {
        background-color: #fff;
        color: #2e2e3a;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Inject custom CSS to handle centering properly
st.markdown("""
    <style>
    
    .front-title-container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: auto;
        margin: 0 auto;
        text-align: center;
        background: #af6382;
        padding: 20px;
        border-radius: 15px;
        
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }
    .front-title {
        
        font-size: 70px;
        color: white; /* Text Color */
        font-weight: bold;
        direction: rtl; /* Ensure proper alignment for Urdu/Arabic */
        margin-bottom: 20px;
    
    }
    </style>
""", unsafe_allow_html=True)

# Use HTML to ensure proper centering
st.markdown('<div class="front-title-container"><div class="front-title" style="color: #ffffff;"> درسگاہ تعلیم القرآن والحدیث  کونگم ڈارہ </div></div>', unsafe_allow_html=True)

# Navigation menu
menu = ["Home", "Student Portal", "Admin Portal", "Syllabus", "Passout 2024","Topper List","Annual Programme","Contact Us"]

choice = st.sidebar.selectbox("Search Here", menu)

# Data storage (mock database using pandas DataFrame)
if "students" not in st.session_state:
    st.session_state["students"] = pd.DataFrame(
        [
            {
                "ID": "101",
                "Name": "Ahmed Khan",
                "Age": 12,
                "Gender": "Male",
                "Class": "6TH",
                "Contact": "1234567890",
                "Marks": {
                    "QURAN": {"Term 1": {"Obtained": 85, "Max": 100}, "Term 2": {"Obtained": 88, "Max": 100}},
                    "FIQH": {"Term 1": {"Obtained": 90, "Max": 100}, "Term 2": {"Obtained": 85, "Max": 100}},
                    "HADEES": {"Term 1": {"Obtained": 78, "Max": 100}, "Term 2": {"Obtained": 80, "Max": 100}},
                    "ADAABI-ZINDAGI": {"Term 1": {"Obtained": 88, "Max": 100}, "Term 2": {"Obtained": 90, "Max": 100}},
                    "USMAL-HUSNA": {"Term 1": {"Obtained": 92, "Max": 100}, "Term 2": {"Obtained": 85, "Max": 100}},
                    "SEERAT": {"Term 1": {"Obtained": 80, "Max": 100}, "Term 2": {"Obtained": 90, "Max": 100}},
                    "DUA": {"Term 1": {"Obtained": 85, "Max": 100}, "Term 2": {"Obtained": 82, "Max": 100}},
                    "TAJWEED": {"Term 1": {"Obtained": 95, "Max": 100}, "Term 2": {"Obtained": 93, "Max": 100}}
                }
            },
            {
                "ID": "102",
                "Name": "Ayesha Siddiqui",
                "Age": 14,
                "Gender": "Female",
                "Class": "8TH",
                "Contact": "9876543210",
                "Marks": {
                    "QURAN": {"Term 1": {"Obtained": 88, "Max": 100}, "Term 2": {"Obtained": 85, "Max": 100}},
                    "FIQH": {"Term 1": {"Obtained": 85, "Max": 100}, "Term 2": {"Obtained": 90, "Max": 100}},
                    "HADEES": {"Term 1": {"Obtained": 82, "Max": 100}, "Term 2": {"Obtained": 88, "Max": 100}},
                    "ADAABI-ZINDAGI": {"Term 1": {"Obtained": 90, "Max": 100}, "Term 2": {"Obtained": 88, "Max": 100}},
                    "USMAL-HUSNA": {"Term 1": {"Obtained": 87, "Max": 100}, "Term 2": {"Obtained": 82, "Max": 100}},
                    "SEERAT": {"Term 1": {"Obtained": 92, "Max": 100}, "Term 2": {"Obtained": 95, "Max": 100}},
                    "DUA": {"Term 1": {"Obtained": 88, "Max": 100}, "Term 2": {"Obtained": 84, "Max": 100}},
                    "TAJWEED": {"Term 1": {"Obtained": 94, "Max": 100}, "Term 2": {"Obtained": 96, "Max": 100}}
                }
            }
        ]
    )

# Home Page
st.markdown("""
<style>
    /* Front page styling */
    .front-title {
        font-size: 55px;
        color: #80281e;
        font-weight: bold;
        text-align: center;
        direction: rtl; /* Ensure proper alignment for Urdu/Arabic */
        margin-bottom: 20px;
        margin-left:30px
    }
    .front-description {
             display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        height: auto;
        margin: 0 auto;
        text-align: center;
        background: #be5f25;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
    }

    /* Button styles */
    .btn {
        background-color: #abdbe3;
        color: #1e8025;
        font-size: 18px;
        padding: 15px 30px;
        border-radius: 8px;
        border: none;
        display: block;
        width: 100%;
        margin: 10px 0;
    }
    .btn:hover {
        background-color: #431e80;
    }
    .btn-admin {
        background-color: #28a745;
    }
    .btn-admin:hover {
        background-color: #431e80;
    }

    /* Student detail section */
    .student-details {
        font-size: 18px;
        background-color: #801e67;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
    }
    .student-details p {
        margin: 10px 0;
        color: #1e4180;
    }
    .marks-section {
        font-size: 16px;
        margin-top: 20px;
        color:#1e4180;
    }

    /* Student result card styling */
    .result-card {
        background-color: #80281e;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .result-card p {
        font-size: 18px;
        margin: 5px 0;
    }

</style>
""", unsafe_allow_html=True)

# Home Page (Front Page)
if choice == "Home":
    st.markdown(
        f"""
            <div style="text-align:center; margin-top:20px; margin-bottom:20px;">
                <img src="data:image/png;base64,{logo_base64}" alt="Logo" style="width:150px; height:150px;">
            </div>
            """,
        unsafe_allow_html=True,
    )
    st.markdown('<p class="front-title" style="color: #ffffff;">الرَّحْمَـٰنُ   عَلَّمَ   الْقُرْآنَ   خَلَقَ   الْإِنسَانَ   عَلَّمَهُ   الْبَيَانَ</p>', unsafe_allow_html=True)

    # Display Logo

    st.markdown('<p class="front-description">جو شخص قرآن کو سمجھ کر اس پر عمل کرتا ہے، وہ نہ صرف دنیاوی کامیابی حاصل کرتا ہے بلکہ آخرت میں بھی فلاح پاتا ہے۔ آئیے قرآن کو اپنے دلوں کی روشنی اور زندگی کا رہنما بنائیں۔"</p>', unsafe_allow_html=True)
  
    st.markdown("""
        <style>
            /* Marquee container styling */
            .top-performers-container {
                text-align: center;
                overflow: hidden;
                white-space: nowrap;
                background: #be5f25;
                color: #ffffff;
                padding: 10px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                margin-top: 20px;
            }
            .top-performers-text {
                display: inline-block;
                padding-left: 100%;
                animation: scroll-text 10s linear infinite;
                font-size: 22px;
                font-weight: bold;
            }
            
            /* Animation for scrolling text */
            @keyframes scroll-text {
                0% { transform: translateX(100%); }
                100% { transform: translateX(-100%); }
            }
        </style>
        <div class="top-performers-container">
            <span class="top-performers-text">🏆 Top Performers of the Year: A, B, C, D, E 🏆</span>
           
        </div>
        <div class="top-performers-container">
            <span class="top-performers-text">🎓 Passout Students: X, Y, Z, A, B, C 🎓</span>
           
        </div>
    """, unsafe_allow_html=True)
 


#student portal
elif choice == "Student Portal":
    st.header("Student Login")
    student_id = st.text_input("Enter Your Student ID")
    login_button = st.button("Login")

    if login_button:
        student_data = st.session_state["students"][st.session_state["students"]["ID"] == student_id]

        if not student_data.empty:
            student_info = student_data.iloc[0]
            st.subheader(f"Welcome, {student_info['Name']}!")
            st.write(f"**Class:** {student_info['Class']}")
            st.write(f"**Contact:** {student_info['Contact']}")
            st.write(f"**Position:** {student_info.get('Position', 'Not Assigned')}")  # Added Position
            

            st.subheader("Marks Sheet")
            marks = student_info['Marks']
            if marks:
                total_obtained = 0
                total_max = 0
                result_lines = []

                for subject, scores in marks.items():
                    term1_obtained = scores.get("Term 1", {}).get("Obtained", 0)
                    term1_max = scores.get("Term 1", {}).get("Max", 0)
                    term2_obtained = scores.get("Term 2", {}).get("Obtained", 0)
                    term2_max = scores.get("Term 2", {}).get("Max", 0)
                    print(end=" ")

                    total_obtained += term1_obtained + term2_obtained
                    total_max += term1_max + term2_max

                    result_lines.append(
                        f"{subject}\n  - Term 1: {term1_obtained}/{term1_max}\n  - Term 2: {term2_obtained}/{term2_max}\n"
                    )

                percentage = (total_obtained / total_max) * 100
                result = "Pass" if percentage >= 40 else "Fail"
                

                st.write("\n".join(result_lines))
                st.write(f"**Total:** {total_obtained}/{total_max}")
                st.write(f"**Percentage:** {percentage:.2f}%")
                st.write(f"**Result:** {result}")
                

                result_text = "\n".join(result_lines) + f"\nTotal: {total_obtained}/{total_max}\nPercentage: {percentage:.2f}%\nResult: {result}"
                st.download_button(label="Download Result",
                                   data=result_text,
                                   file_name=f"Result_{student_info['Name']}.txt")
            else:
                st.write("No marks available yet.")

                
        else:
            st.error("Student ID not found. Please try again.")
            # Admin Portal
# Admin Portal
elif choice == "Admin Portal":
    st.header("Admin Portal")
    admin_password = st.text_input("Enter Admin Password", type="password")
    if admin_password == "aamir123786":
        admin_choice = st.selectbox("Admin Options", ["Add Student", "View All Students"])
       

        if admin_choice == "Add Student":
            st.subheader("Add New Student")
            with st.form("add_student_form"):
                student_id = st.text_input("Student ID")
                name = st.text_input("Full Name")
                age = st.number_input("Age", min_value=5, max_value=100, step=1)
                gender = st.selectbox("Gender", ["Male", "Female"])
               # student_class = st.selectbox("Class", [f" {i} TH" for i in range(1, 9)])
                class_labels = ["1ST" if i == 1 else  "2ND" if i == 2 else "3RD" if i==3 else  f"{i}th"  for i in range(1, 9)]

# Display the selectbox
                student_class = st.selectbox("Class", class_labels)

# Display the selected class
                st.write(f"Class: {student_class}")

                
                contact = st.text_input("Contact Number")
                position = st.text_input("Position")

                # Initialize an empty dictionary for marks
                marks = {}
                subjects = ["QURAN", "FIQH", "HADEES", "ADAABI-ZINDAGI", "USMAL-HUSNA", "SEERAT", "DUA", "TAJWEED"]

                # Input fields for Term 1 and Term 2 marks for each subject
                for subject in subjects:
                    term1_obtained = st.number_input(f"Marks Obtained in {subject} (Term 1)", min_value=0, max_value=100, step=1)
                    term1_max = st.number_input(f"Max Marks in {subject} (Term 1)", min_value=1, max_value=100, step=1)
                    term2_obtained = st.number_input(f"Marks Obtained in {subject} (Term 2)", min_value=0, max_value=100, step=1)
                    term2_max = st.number_input(f"Max Marks in {subject} (Term 2)", min_value=1, max_value=100, step=1)

                    # Store the marks for Term 1 and Term 2 in the marks dictionary
                    marks[subject] = {
                        "Term 1": {"Obtained": term1_obtained, "Max": term1_max},
                        "Term 2": {"Obtained": term2_obtained, "Max": term2_max}
                    }
                    
                submit = st.form_submit_button("Add Student")

                if submit:
                    new_student = {
                        "ID": student_id,
                        "Name": name,
                        "Age": age,
                        "Gender": gender,
                        "Class": student_class,
                        "Contact": contact,
                        "Position": position,
                        "Marks": marks
                    }
                    new_student_df = pd.DataFrame([new_student])
                    st.session_state["students"] = pd.concat([st.session_state["students"], new_student_df], ignore_index=True)
                    st.success(f"Student {name} has been added successfully!")

        elif admin_choice == "View All Students":
            st.subheader("All Students")
            if st.session_state["students"].empty:
                st.write("No students have been added yet.")
            else:
                st.dataframe(st.session_state["students"])
        
    
       
    else:
        st.error("Incorrect password.")
# passout students
elif choice == "Passout 2024":
    st.header("Passout Students - 2024")

    # List of Passout Students
    passout_students = [
        "Ahmed Khan",
        "Ayesha Siddiqui",
        "Ali Raza",
        "Fatima Noor",
        "Sara Ahmed",
        "Zain Ul Abideen"
    ]

    # Display Passout Students
    st.markdown("""
        <style>
            .passout-list-container {
                background: #be5f25;
                color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                margin-top: 20px;
            }
            .passout-list-container h3 {
                color: #ffeb3b;
                text-align: center;
            }
            .passout-list-container ul {
                list-style-type: none;
                padding: 0;
                font-size: 20px;
            }
            .passout-list-container ul li {
                margin: 10px 0;
            }
        </style>
        <div class="passout-list-container">
            <h3>🎓 Congratulations to  8TH Class Students (2024)🎓</h3>
            <ul>
                <li>Aftab Shabir</li>
                <li>Arsalaan Fayaz</li>
                <li>Basharat Ayoub</li>
                <li>Faheem-ul-Islam</li>
                <li>Muqadas Shabaan</li>
                <li>Toiba Rashid</li>
                
            
        </div>
    """, unsafe_allow_html=True)

    
 # Add this import to fetch the image from the URL
elif choice == "Syllabus":
    st.header("Class Syllabus")
    
    # Class options
    classes = [f"Class {i}{'st' if i == 1 else 'nd' if i == 2 else 'rd' if i == 3 else 'th'}" for i in range(1, 9)]
    selected_class = st.selectbox("Select Class", classes)

    # Mapping of syllabus images with raw GitHub URLs for each class
    syllabus_images = {
        "Class 1st": "https://raw.githubusercontent.com/meer25800/darsgah2/main/PythonProject1/Screenshot__193_-removebg-preview.png",
        "Class 2nd": "https://raw.githubusercontent.com/meer25800/darsgah2/main/PythonProject1/Screenshot__193_-removebg-preview.png",
        "Class 3rd": "https://raw.githubusercontent.com/meer25800/darsgah2/main/PythonProject1/a-3.png",
        "Class 4th": "https://raw.githubusercontent.com/meer25800/darsgah2/main/PythonProject1/a-3.png",
        "Class 5th": "https://raw.githubusercontent.com/meer25800/darsgah2/main/PythonProject1/5th Syllabus-1.png",
        "Class 6th": "https://raw.githubusercontent.com/meer25800/darsgah2/main/PythonProject1/6th Syllabus-1.png",
        "Class 7th": "https://raw.githubusercontent.com/meer25800/darsgah2/main/PythonProject1/Screenshot__193_-removebg-preview.png",
        "Class 8th": "https://raw.githubusercontent.com/meer25800/darsgah2/main/PythonProject1/Screenshot__193_-removebg-preview.png",
    }

    syllabus_url = syllabus_images.get(selected_class)

    if syllabus_url:
        # Fetch the image from the URL
        response = requests.get(syllabus_url)
        if response.status_code == 200:
            # Display the image
           # st.image(response.content, caption=f"{selected_class} Syllabus", width=600)

            # Allow the user to download the image
            st.download_button(
                label=f"Download {selected_class} Syllabus",
                data=response.content,
                file_name=f"{selected_class}_Syllabus.png",
                mime="image/png"
            )
        else:
            st.error(f"Failed to fetch the syllabus image for {selected_class}.")
    else:
        st.error("Syllabus not available for the selected class.")

#topper list
elif choice == "Topper List":
    st.header("Topper List")

    # List of Toppers
   

    # Display Toppers
    st.markdown("""
        <style>
            .topper-list-container {
                background: #283593;
                color: #ffffff;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
                margin-top: 20px;
            }
            .topper-list-container h3 {
                color: #ffeb3b;
                text-align: center;
            }
            .topper-table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            .topper-table th, .topper-table td {
                border: 1px solid #ffffff;
                padding: 10px;
                text-align: center;
                font-size: 18px;
            }
            .topper-table th {
                background: #3949ab;
            }
            .topper-table tr:nth-child(even) {
                background: #3f51b5;
            }
        </style>
        <div class="topper-list-container">
            <h3>🏆 Top Performers of the Year 🏆</h3>
            <table class="topper-table">
                <tr>
                    <th>Name</th>
                    <th>Percentage</th>
                    <th>Position</th>
                    <th>Class</th>
                </tr>
                <tr>
                    <td>Name</td>
                    <td>Percentage</td>
                    <td>Position</td>
                    <td>Class</td>
                </tr>
    """, unsafe_allow_html=True)

    # Loop through toppers list to display each student
    
    
    # Close the table and container div
    st.markdown("""
            </table>
        </div>
    """, unsafe_allow_html=True)


#events
elif choice == "Annual Programme":
    st.title("Annual Programme")
    st.markdown("""
    <style>
        .programme-table {
            width: 80%;
            margin: 0 auto;
            border-collapse: collapse;
            text-align: center;
            background: #81c784;
            color: #fff;
            font-size: 18px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        .programme-table th, .programme-table td {
            padding: 12px;
            border: 1px solid #ffffff;
        }
        .programme-table th {
            background: #388e3c;
        }
        .programme-table tr:nth-child(even) {
            background: #66bb6a;
        }
        .programme-table tr:hover {
            background: #43a047;
        }
    </style>
""", unsafe_allow_html=True)

    st.markdown("""
        <div style='background: #4caf50; border-radius: 15px; padding: 20px;'>
            <h2 style='color: #fff; text-align: center;'>🌟 Annual Programme Schedule 🌟</h2>
            <table class='programme-table'>
                <tr>
                    <th>Category</th>
                    <th>Student Name</th>
                </tr>
                <tr>
                    <td>Quran Recitation</td>
                    <td>Ahmed Khan</td>
                </tr>
                <tr>
                    <td>Naat</td>
                    <td>Fatima Noor</td>
                </tr>
                <tr>
                    <td>Nazm</td>
                    <td>Ayesha Siddiqui</td>
                </tr>
                <tr>
                    <td>Dars-e-Quran</td>
                    <td>Ali Raza</td>
                </tr>
                <tr>
                    <td>Dars-Hadees</td>
                    <td>Sara Ahmed</td>
                </tr>
                <tr>
                    <td>Hadees</td>
                    <td>Zainab Fatima</td>
                </tr>
                <tr>
                    <td>General Topics</td>
                    <td>Usman Ali</td>
                </tr>
            </table>
        </div>
    """, unsafe_allow_html=True)


elif choice == "Contact Us":
    # Custom CSS for styling
    st.markdown("""
    <style>
        .contact-title {
            font-size: 36px;
            color: #4CAF50;
            font-weight: bold;
        }
        .contact-info {
            font-size: 20px;
            color: #1E88E5;
        }
        .contact-button {
            background-color: #FF5733;
            color: white;
            font-size: 18px;
            padding: 12px 24px;
            border-radius: 8px;
            border: none;
        }
        .contact-button:hover {
            background-color: #D35400;
        }
    </style>
    """, unsafe_allow_html=True)

    # Contact Us Section
    st.markdown('<p class="contact-title" style="color: #ffffff;">Contact Us</p>', unsafe_allow_html=True)
    st.markdown('<p class="contact-info" style="color: #ffffff;">For inquiries, please contact us at:</p>', unsafe_allow_html=True)
    st.markdown('<p class="contact-info" style="color: #ffffff;">📞 <strong>Phone:</strong> +91-7889652569</p>', unsafe_allow_html=True)
    st.markdown('<p class="contact-info" style="color: #ffffff;">📧 <strong>Email:</strong> aamirmir08@gmail.com</p>', unsafe_allow_html=True)

    # Contact Button
    contact_button = st.button('Get in Touch', key='contact_button', help="Click here to send your inquiry")
    if contact_button:
        st.write("Thank you for reaching out! We'll get back to you soon.") 
