import streamlit as st
import pandas as pd
from PIL import Image
import base64
import os
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode("utf-8")
    return encoded

# Path to the logo


logo_path = "/mount/src/darsgah2/PythonProject1/Screenshot__193_-removebg-preview.png"
if not os.path.exists(logo_path):
    print(f"File not found: {logo_path}")

# Get base64 string of the image
logo_base64 = get_image_base64(logo_path)

# Title page
st.set_page_config(page_title="Darsgah Taleemul Quran Wal Hadith Kongamdara", page_icon="📘")
st.title("درسگاہ  تعلیم  القرآن  والحدیث  کانگمڈا")

# Navigation menu
menu = ["Home", "Student Portal", "Admin Portal", "Contact"]
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
                "Class": "Class 6",
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
                "Class": "Class 8",
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

syllabus_links = {
    "Class 1": "https://drive.google.com/file/d/1IbQBpjhfgtrcQlHH-cqs2I6GGXNAI2d-/view?usp=sharing",
    "Class 2": "https://drive.google.com/file/d/1IbQBpjhfgtrcQlHH-cqs2I6GGXNAI2d-/view?usp=sharing",
    "Class 3": "https://drive.google.com/file/d/1IbQBpjhfgtrcQlHH-cqs2I6GGXNAI2d-/view?usp=sharing",
    "Class 4": "https://drive.google.com/file/d/1IbQBpjhfgtrcQlHH-cqs2I6GGXNAI2d-/view?usp=sharing",
    "Class 5": "https://drive.google.com/file/d/1IbQBpjhfgtrcQlHH-cqs2I6GGXNAI2d-/view?usp=sharing",
    "Class 6": "https://drive.google.com/file/d/1IbQBpjhfgtrcQlHH-cqs2I6GGXNAI2d-/view?usp=sharing",
    "Class 7": "https://drive.google.com/file/d/1IbQBpjhfgtrcQlHH-cqs2I6GGXNAI2d-/view?usp=sharing",
    "Class 8": "https://drive.google.com/file/d/1IbQBpjhfgtrcQlHH-cqs2I6GGXNAI2d-/view?usp=sharing",
}

# Home Page
st.markdown("""
<style>
    /* Front page styling */
    .front-title {
        font-size: 55px;
        color: #80281e;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .front-description {
        font-size: 20px;
        color: #1e8025;
        text-align: center;
        margin-bottom: 40px;
    }

    /* Button styles */
    .btn {
        background-color: #abdbe3;
        color: white;
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
    st.markdown('<p class="front-title">Welcome to Darsgah Taleemul Quran Wal Hadith Kongamdara</p>', unsafe_allow_html=True)

    # Display Logo

    st.markdown('<p class="front-description">جو شخص قرآن کو سمجھ کر اس پر عمل کرتا ہے، وہ نہ صرف دنیاوی کامیابی حاصل کرتا ہے بلکہ آخرت میں بھی فلاح پاتا ہے۔ آئیے قرآن کو اپنے دلوں کی روشنی اور زندگی کا رہنما بنائیں۔"</p>', unsafe_allow_html=True)

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

            st.subheader("Syllabus")
            syllabus_link = syllabus_links.get(student_info['Class'], None)

            if syllabus_link:
                st.write(f"Download the syllabus for {student_info['Class']}:")
                st.markdown(f"[Download Syllabus]({syllabus_link})", unsafe_allow_html=True)
            else:
                st.write("Syllabus not available.")
        else:
            st.error("Student ID not found. Please try again.")

        # Admin Portal
# Admin Portal
elif choice == "Admin Portal":
    st.header("Admin Portal")
    admin_password = st.text_input("Enter Admin Password", type="password")
    if admin_password == "admin123":
        admin_choice = st.selectbox("Admin Options", ["Add Student", "View All Students", "Update Students via CSV"])

        if admin_choice == "Add Student":
            st.subheader("Add New Student")
            with st.form("add_student_form"):
                student_id = st.text_input("Student ID")
                name = st.text_input("Full Name")
                age = st.number_input("Age", min_value=5, max_value=100, step=1)
                gender = st.selectbox("Gender", ["Male", "Female"])
                student_class = st.selectbox("Class", [f"Class {i}" for i in range(1, 9)])
                contact = st.text_input("Contact Number")

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

        elif admin_choice == "Update Students via CSV":
            st.subheader("Update Students via CSV")
            uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

            if uploaded_file is not None:
                try:
                    # Read the uploaded CSV file
                    uploaded_data = pd.read_csv(uploaded_file)

                    # Ensure columns match the required format
                    required_columns = ["ID", "Name", "Age", "Gender", "Class", "Contact", "Marks"]
                    if not all(col in uploaded_data.columns for col in required_columns):
                        st.error("Uploaded CSV does not have the required columns: " + ", ".join(required_columns))
                    else:
                        # Merge the data and update the student records
                        uploaded_data["Marks"] = uploaded_data["Marks"].apply(eval)  # Convert Marks column to dictionary
                        st.session_state["students"] = pd.concat([st.session_state["students"], uploaded_data], ignore_index=True).drop_duplicates(subset="ID", keep="last")
                        st.success("Student data updated successfully!")
                        st.dataframe(st.session_state["students"])

                except Exception as e:
                    st.error(f"Error processing file: {e}")
    else:
        st.error("Incorrect password.")

# Contact Page
elif choice == "Contact":
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
    st.markdown('<p class="contact-title">Contact Us</p>', unsafe_allow_html=True)
    st.markdown('<p class="contact-info">For inquiries, please contact us at:</p>', unsafe_allow_html=True)
    st.markdown('<p class="contact-info">📞 <strong>Phone:</strong> +91-12345-67890</p>', unsafe_allow_html=True)
    st.markdown('<p class="contact-info">📧 <strong>Email:</strong> info@darsgah.com</p>', unsafe_allow_html=True)

    # Contact Button
    contact_button = st.button('Get in Touch', key='contact_button', help="Click here to send your inquiry")
    if contact_button:
        st.write("Thank you for reaching out! We'll get back to you soon.")
