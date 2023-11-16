# Timetable-Management

Hello \
Myself **Sachin Chandela**\
And this is the Repositories for Timetable Management System
Includes various classes such as course sections timetable and various function.

## course

course is a class that takes input such as eg.(course_name,course_code,Instructure_Name,exam_date) and varoius function like to get all sections to add section and to print basic information about course

## sections

as course it is also a class which takes (lecture name date and slot) 

## timetable
it's a Class to enroll in a course and checking for clashes 

# Implementation 
```python
from timemanage import Course, Section, Timetable

#To intialize course
my_course=course("CSE","CS F11","Rajiv Kumar",["23-12-2023"])

# To intialize Sections
my_section=sections("Lecture",["Monday","Wednesday","Friday"],["12pm-01pm","12pm-01pm","12pm-01pm"])
```

### To add section to course
``` python
my_course.add(my_sections)
```

### To get all sections
``` python
get_section=my_course.get_all_section()
for i in get_section:
    ptint(i)
```

### To enroll a subject into a course and to export it to a csv file
``` python
my_timetable=timetable()
my_timetable.enroll_subject(my_course)
my_timetable.export_to_csv("timetable.csv")
```

### For checking clashes 
``` python
my_timetable.clashes()

```
### Populating Subjects from Excel

Use the populate_subject function to populate new courses from an Excel spreadsheet. This function reads the spreadsheet, creates new courses, and adds them to the persistent database.

```python
from timemanage import populate_subject

# Provide the path to the Excel file
file_path = "courses.xlsx"

# Populate subjects from the Excel file
populate_subject(file_path)
```






