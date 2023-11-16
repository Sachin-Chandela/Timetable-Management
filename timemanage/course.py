import openpyxl
class Course:
    
    def __init__(self,course_name,course_code,Instructure_Name,exam_date=[]):
        self.course_name=course_name
        self.course_code=course_code
        self.Instructure_Name=Instructure_Name
        self.exam_date=exam_date
        self.section=[]
    
    def get_all_section(self):
        """Get all lecture/tutorial/lab sections available"""
        return self.section
    
    def add(self,sections):
        """Add a section to the course"""
        self.section.append(sections)
    
    def __str__(self):
        """Print basic information about the course"""
        course_info= f"course name is {self.course_name}\ncourse code is {self.course_code}\nInstructure Name is {self.Instructure_Name}"
        return course_info
    
    def _populate_section(self,new_section):
        """
        It's a private method.
        Populate new sections of the course (restricted access)
        """
        self.new_section=new_section
        self.section.append(new_section)




def populate_subject(new_section, file_path):
    """Populate new courses to the database from an Excel spreadsheet."""

    # Load the Excel file
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    # Get column indices from the header
    header = [cell.value.lower() for cell in sheet[1]]
    code_index = header.index("code")
    name_index = header.index("name")
    instructor_index = header.index("instructor")
    exam_dates_index = header.index("exam_dates")

    # Iterate through rows and populate courses
    for row in sheet.iter_rows(min_row=2, values_only=True):
        course_code = row[code_index]
        course_name = row[name_index]
        instructor = row[instructor_index]
        exam_dates = row[exam_dates_index].split(", ")

        # Create a new course instance
        new_course = Course(course_code, course_name, instructor, exam_dates)

        # Populate lecture sections using the method in the Course class
        new_course._populate_section(new_section)

        # Add the new course to the persistent database (you can define your database logic here)
        # For example, you might add it to a list or store it in a database
        # For simplicity, I'll just print the course details
        # print(f"Added new course: {new_course.course_code} - {new_course.course_name}")



        