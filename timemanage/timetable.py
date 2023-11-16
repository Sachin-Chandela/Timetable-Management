import csv

class TIMETABLE:
    def __init__(self,):
        self.courses=[]
    def enroll_subject(self,course):
        self.courses.append(course)
    def clashes(self):
        exam_ddate=[]
        n=int(input("How many dates you want to enter:-"))
        for i in range(0,n):
            b=input(f"ENter your {i+1}th date:-")
            exam_ddate.append(b)
            
        for course in self.courses:
            for date in course.exam_date:
                if date in exam_ddate:
                    print(f"exam clash of :{course.course_name} on {date}")
                else:
                    exam_ddate.add(date)
        
    def section_clashes(self):
        section_schedule={}
        for course in self.courses:
            for section in course.get_all_section():
                if section.day in section_schedule and section.slot in section_schedule:
                    print(f"Clashes of {section.section_type} on {section.day} , {section.slot} ")
                else:
                    continue

    def export_to_csv(self, filename="timetable.csv"):
        """Export the timetable to a CSV file"""
        with open(filename, "w", newline="") as csvfile:
            fieldnames = [
                "Course Code",
                "Course Name",
                "Instructor",
                "Exam Dates",
                "Section Type",
                "Day",
                "Time Slots",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()

            for course in self.courses:
                for section in course.get_all_section():
                    writer.writerow(
                        {
                            "Course Code": course.course_code,
                            "Course Name": course.course_name,
                            "Section Type": course.Instructure_Name,
                            "Exam Dates": ", ".join(course.exam_date),
                            "Section Type": section.section_type,
                            "Day": section.day,
                            "Time Slots": ", ".join(section.slot),
                        }
                    )

# to export to a csv file
my_timetable = TIMETABLE()
# # ... (enroll subjects and check clashes)
my_timetable.export_to_csv("timetable.csv")










    



