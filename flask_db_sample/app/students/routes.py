
from flask import render_template, redirect, request, url_for, jsonify
from . import bp
from app.models.tables import Student
from app.database.sqlAlchemy import session
import json
@bp.route('/<int:student_id>',  methods=['GET'])
@bp.route('/', methods=['GET'])
def showStudents(student_id=0):
    if not student_id:
        student = session.query(Student).all()
        return render_template("student.html", student=student)
    else:
        s = session.query(Student).filter_by(id=student_id).first()
        return jsonify(s)


      

#Function to add a student
@bp.route('/new',methods=['GET','POST'])
def newStudent():
   if request.method == 'POST':
       newStudent = Student(fname = request.form['fname'], lname = request.form['lname'], subject = request.form['subject'])
       session.add(newStudent)
       session.commit()
       return redirect(url_for('students.showStudents'))
   else:
       return render_template('newStudent.html')
#Function to edit a student
@bp.route("/<int:student_id>/edit/", methods = ['GET', 'POST'])
def editStudent(student_id):
   editedStudent = session.query(Student).filter_by(id=student_id).one()
   if request.method == 'POST':
       if request.form['subject']:
           editedStudent.subject = request.form['subject']
           return redirect(url_for('students.showStudents'))
   else:
       return render_template('editStudent.html', student = editedStudent)
#Function to delete a student
@bp.route('/<int:student_id>/delete/', methods = ['GET','POST'])
def deleteStudent(student_id):
   studentToDelete = session.query(Student).filter_by(id=student_id).one()
   if request.method == 'POST':
       session.delete(studentToDelete)
       session.commit()
       return redirect(url_for('students.showStudents', student_id=student_id))
   else:
       return render_template('deleteStudent.html',student = studentToDelete)


