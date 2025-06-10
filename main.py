import streamlit as st
from student import Student
from student_manager import StudentManager
import pandas as pd

# Initialize the StudentManager
manager = StudentManager()

# Set page configuration
st.set_page_config(page_title="Student Management System", page_icon="📚", layout="wide")

# Sidebar for navigation
st.sidebar.title("Navigation")
menu_options = ["Add Student", "View Students", "Search Student", "Update Student", "Delete Student"]
choice = st.sidebar.selectbox("Select Option", menu_options)

# Main app title
st.title("Student Management System")

# Add Student
if choice == "Add Student":
    st.header("Add a New Student")
    with st.form("add_student_form"):
        student_id = st.text_input("Student ID")
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=100, step=1)
        grade = st.text_input("Grade")
        submit = st.form_submit_button("Add Student")
        
        if submit:
            if student_id and name and age and grade:
                manager.add_student(Student(student_id, name, age, grade))
                st.success("Student added successfully!")
            else:
                st.error("Please fill in all fields.")

# View Students
elif choice == "View Students":
    st.header("All Students")
    students = manager.view_student()
    if students and students[0] != "No students found.":
        # Convert student list to DataFrame for display
        df = pd.DataFrame([s.to_dict() for s in students])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No students found.")

# Search Student
elif choice == "Search Student":
    st.header("Search Student by ID")
    student_id = st.text_input("Enter Student ID")
    if st.button("Search"):
        student = manager.find_student(student_id)
        if student:
            st.write(f"**ID**: {student.student_id}")
            st.write(f"**Name**: {student.name}")
            st.write(f"**Age**: {student.age}")
            st.write(f"**Grade**: {student.grade}")
        else:
            st.error("Student not found!")

# Update Student
elif choice == "Update Student":
    st.header("Update Student")
    student_id = st.text_input("Enter Student ID to update")
    student = manager.find_student(student_id) if student_id else None
    
    if student_id and not student:
        st.error("Student not found!")
    elif student:
        with st.form("update_student_form"):
            name = st.text_input("New Name (leave blank to keep unchanged)", value=student.name)
            age = st.number_input("New Age (leave as is to keep unchanged)", min_value=1, max_value=100, value=student.age, step=1)
            grade = st.text_input("New Grade (leave blank to keep unchanged)", value=student.grade)
            submit = st.form_submit_button("Update Student")
            
            if submit:
                updated = manager.update_student(student_id, name if name != student.name else None, 
                                              age if age != student.age else None, 
                                              grade if grade != student.grade else None)
                if updated:
                    st.success("Student updated successfully!")
                else:
                    st.error("Update failed!")

# Delete Student
elif choice == "Delete Student":
    st.header("Delete Student")
    student_id = st.text_input("Enter Student ID to delete")
    if st.button("Delete"):
        deleted = manager.delete_students(student_id)
        if deleted:
            st.success("Student deleted successfully!")
        else:
            st.error("Student not found!")

# Add enhanced CSS for a catchy look
st.markdown("""
    <style>
    /* General app styling */
    .stApp {
        max-width: 1700px;
        margin: 0 auto;
        background: linear-gradient(180deg, #7FFFD4, #7c3aed);
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar styling */
    .stSidebar {
        background: linear-gradient(180deg, #4f46e5, #7c3aed);
        color: white;
        border-right: 2px solid #ddd;
    }
    .stSidebar .stSelectbox > div > div {
        background-color: #ffffff20;
        color: white;
        border-radius: 8px;
    }
    .stSidebar h1 {
        color: white;
        font-size: 1.8em;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Main content styling */
    h1 {
        color: #1e3a8a;
        font-weight: 700;
        text-align: center;
        text-decoration: underline;
        margin-bottom: 20px;
    }
    h2 {
        color: #3b82f6;
        font-weight: 600;
    }

    /* Form and input styling */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input {
        border: 2px solid #93c5fd;
        border-radius: 8px;
        padding: 8px;
        transition: border-color 0.3s ease;
    }
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus {
        border-color: #2563eb;
        box-shadow: 0 0 5px rgba(37, 99, 235, 0.3);
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #4f46e5, #7c3aed);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.4);
    }

    /* DataFrame styling */
    .stDataFrame {
        border: 2px solid #bfdbfe;
        border-radius: 8px;
        overflow: hidden;
    }
    .stDataFrame table {
        background-color: white;
    }
    .stDataFrame th {
        background-color: #dbeafe;
        color: #1e40af;
    }

    /* Alerts and messages */
    .stSuccess {
        background-color: #d1fae5;
        color: #065f46;
        border-left: 4px solid #10b981;
    }
    .stError {
        background-color: #fee2e2;
        color: #991b1b;
        border-left: 4px solid #ef4444;
    }
    .stInfo {
        background-color: #e0f2fe;
        color: #1e40af;
        border-left: 4px solid #3b82f6;
    }

    /* Smooth transitions for all elements */
    * {
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    </style>
""", unsafe_allow_html=True)