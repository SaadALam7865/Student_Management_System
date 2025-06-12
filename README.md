##Student Management System

A simple yet powerful Student Management System built with Python, Streamlit, and object-oriented programming (OOP). This web application allows users to add, view, search, update, and delete student records through a visually appealing interface. Data is persistently stored in a JSON file (students.json) and a text file (std_data.txt).

Features
Add Student: Input student details (ID, name, age, grade) via a form.
View Students: Display all student records in a clean, tabular format.
Search Student: Find a student by their ID.
Update Student: Modify existing student details.
Delete Student: Remove a student record by ID.
Responsive UI: Modern, gradient-based design with hover effects and smooth transitions.
Persistent Storage: Saves data in both JSON and text formats.

Tech Stack
Python: Core logic and OOP implementation.
Streamlit: Web interface for user interaction.
Pandas: For displaying student data in a table.
JSON: For persistent data storage.
CSS: Custom styling for a vibrant, user-friendly UI.

Installation
Clone the Repository:

git clone https://github.com/your-username/student-management-system.git
cd student-management-system



Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate



Install Dependencies:
pip install streamlit pandas



Run the Application:
streamlit run app.py



Open your browser and navigate to http://localhost:8501.
Usage





Navigation: Use the sidebar to select options (Add, View, Search, Update, Delete).
Add Student: Fill out the form with student details and submit.
View Students: See all students in a table format.
Search Student: Enter a student ID to view their details.
Update Student: Enter a student ID, modify fields, and submit to update.
Delete Student: Enter a student ID to remove the record.
Data is automatically saved to students.json and std_data.txt after each operation.

File Structure

student-management-system/
├── app.py                # Main Streamlit application
├── student.py            # Student class definition
├── student_manager.py    # StudentManager class for data operations
├── students.json         # JSON file for storing student data
├── std_data.txt          # Text file for storing student data
└── README.md             # Project documentation

Screenshots

(Add screenshots of the app here, e.g., main page, add student form, etc.)
Contributing
Contributions are welcome! To contribute:





Fork the repository.
Create a new branch (git checkout -b feature-name).
Make your changes and commit (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.

License
This project is licensed under the MIT License.

Contact
For questions or suggestions, feel free to open an issue or contact saadalam929@gmail.com.
