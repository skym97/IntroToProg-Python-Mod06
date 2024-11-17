# ------------------------------------------------------------------------------------------ #
# Title: Assignment06_Starter
# Desc: This assignment demonstrates using functions
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Andy Sul, 11/16/2024, Modified Script
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data

# Class Definitions
class FileProcessor:
    """Processes data to and from a file"""

    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """Reads data from a file into a list of dictionaries"""
        try:
            with open(file_name, "r") as file:
                data = json.load(file)  # Load JSON data
                for entry in data:
                    standardized_entry = {
                        "first_name": entry.get("first_name") or entry.get("FirstName"),
                        "last_name": entry.get("last_name") or entry.get("LastName"),
                        "course_name": entry.get("course_name") or entry.get("CourseName")
                    }
                    student_data.append(standardized_entry)  # Add standardized data to the list
        except FileNotFoundError:
            print(f"{file_name} not found. Starting with an empty list.")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON from {file_name}: {e}")
        except Exception as e:
            print(f"An error occurred while reading {file_name}: {e}")

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """Writes data from a list of dictionaries to a file"""
        try:
            with open(file_name, "w") as file:
                json.dump(student_data, file, indent=4)  # Save list as JSON
            print(f"Data successfully saved to {file_name}.")
        except IOError as e:
            print(f"Error writing to {file_name}: {e}")
        except Exception as e:
            print(f"An error occurred while writing to {file_name}: {e}")

# Initial data loading
FileProcessor.read_data_from_file(FILE_NAME, students)

# IO class
class IO:
    """Handles input and output operations"""

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        print(f"Error: {message}")
        if error:
            print(f"Details: {error}")

    @staticmethod
    def output_menu(menu: str):
        print(menu)

    @staticmethod
    def input_menu_choice() -> str:
        while True:
            choice = input("Please enter your menu choice: ")
            if choice in ["1", "2", "3", "4"]:  # Validate menu choices
                return choice
            else:
                print("Invalid choice. Please enter a valid option (1-4).")

    @staticmethod
    def output_student_courses(student_data: list):
        if not student_data:
            print("No student data available.")
            return
        print(f"{'First Name':<20} {'Last Name':<20} {'Course Name':<20}")
        print("-" * 60)
        for student in student_data:
            print(f"{student['first_name']:<20} {student['last_name']:<20} {student['course_name']:<20}")

    @staticmethod
    def input_student_data(student_data: list):
        try:
            # Input first name
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")

            # Input last name
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")

            # Input course name
            course_name = input("Enter the course name: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")

            # Store the data in the student_data list
            student_data.append({
                "first_name": student_first_name,
                "last_name": student_last_name,
                "course_name": course_name
            })
            print(f"Student {student_first_name} {student_last_name} registered for {course_name}.")
        except ValueError as e:
            IO.output_error_messages(str(e))

# Present and Process the data
while True:
    # Present the menu of choices
    IO.output_menu(MENU)
    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":
        IO.input_student_data(students)

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(students)

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(FILE_NAME, students)

    # Stop the loop
    elif menu_choice == "4":
        break

print("Program Ended")


