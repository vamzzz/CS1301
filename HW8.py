#!/usr/bin/env python
"""
Georgia Institute of Technology - CS1301
Introduction to Object Oriented Programming using Python.
"""
__author__ = "Vamshi Adimulam"
#903161218
#vamshi.adimulam@gatech.edu
""" I worked on this homework assignment alone, using only this semester's course materials. """

class Student(object):   
    def __init__(self, name, gtid, year = 1):
        """Initialize a Student object whose name is *name*, gtid is *gtid*, gpa is *gpa*, class standing is *year*; courses start empty"""
        self.name = name
        self.gtid = gtid
        self.year = year
        self.courses = {}

    def calculate_gpa(self):
        """ Returns a float of the student's gpa. To calculate GPA:
        1. If student has no courses his gpa must be 0.0
        2. Multiply the grade (0-4) by the number of credit to get quality poins.
        3. Total the credit hours. Total the total quality points.
        4. Divide the total quality points by the total credit hours"""
        GPA = 0.0
        quality = 0
        hours = float(self.get_total_credits())
        if self.courses == {}:
            return 0.0
        else:
            for j in self.courses.keys():
                grade = int(self.courses[j][1])
                credit = int(self.courses[j][0].credits)
                quality = float(quality + (grade * credit))
            GPA = (quality/hours)
        return GPA

    def set_year(self, year):
        """ change student's year. year is now *year* """
        self.year = year

    def in_dean_list(self):
        """ return true if gpa greater than or equal 3, false otherwise """
        if self.calculate_gpa() >= 3:
            return True
        else:
            return False

    def get_real_year(self):
        """ return a string representation of the student's class standing
        1 -> Freshman, 2 -> Sophomore, 3 -> Junior, 4 -> Senior """
        if str(self.year) == "1":
            return "Freshman"
        elif str(self.year) == "2":
            return "Sophomore"
        elif str(self.year) == "3":
            return "Junior"
        elif str(self.year) == "4":
            return "Senior"    

    def get_total_credits(self):
        """ return the amount of credits a student is taking as an int"""
        hours = 0
        for i in self.courses.keys():
            hours = hours + int(self.courses[i][0].credits)
        return hours
     

    def register(self, course):
        cName = course.code
        if cName not in self.courses.keys():
            self.courses[cName] = [course,0]

    def register_many(self, courses):
        """ register courses from a list of Course objects """
        for c in courses:
            self.register(c)        

    def drop(self, course):
        """ Drop a course if student is registered to it. Return True if successfully dropped and False if student is not registered for that course. """
        if course.code in self.courses.keys():
            del self.courses[course.code]
            return True
        else:
            return False 

    def is_taking(self, course):
        """ Returns true if student is registered for a course """
        if course in self.courses:
            return True
        else:
            return False        

    def __str__(self):
        """ String representation of a Student object """
        return "({0}, {1}, {2})".format(self.name, self.get_real_year(), self.calculate_gpa())


class Course(object):
    """ docstring of a Course object.
    Course have the following properties:
    Attributes:
        code: A string representing the course code (i.e CS1301)
        credits: An integer representing the course's amount of credits (i.e 3)
        instructor: An Instructor object representing the instructor of the course
    """

    def __init__(self, code, credits, instructor):
        """Initialize a Course object whose code is *code*, credits is *cresits*, and instructor is *instructor*."""
        self.code = code
        self.instructor = instructor
        self.credits = credits               

    def get_code(self):
        return str(self.code)

    def get_credits(self):
        """ returns int representing the course credits """
        return int(self.credits)   

    def __str__(self):
        """ String representation of a Course object """
        return "({0}, {1}, {2})".format(self.code, self.credits, self.instructor)
    def __repr__(self):
        return "<Course object: ({0}, {1}, {2})>".format(self.code, self.credits, self.instructor)

class Instructor(object):
    """docstring of an Instructor object.
    Instructor have the following properties:
        Attributes:
            name: A string representing the instructor name (i.e CS1301)"""
    name = "none"
    def __init__(self, name):
        """Initialize an Instructor object whose name is *name*."""
        self.name = name 

    def assign_grade(self, student, course, grade):
        """ If student is taking a course, change the student's grade in a course by *grade*. grade is a number between 0 and 4 inclusively. The max a student can get in a course is 4."""
        Max = 4
        for x in student.courses:
            self.grade = int(grade)
            if grade > Max:
                grade = Max
            if course.code in student.courses.keys():
                student.courses[course.code][1] = grade     

    def __str__(self):
        """ String representation of an Instructor object """
        return "{0}".format(self.name)

    def __repr__(self):
        return "<Instructor object: ({0})>".format(self.name)

if __name__ == '__main__':
    pass