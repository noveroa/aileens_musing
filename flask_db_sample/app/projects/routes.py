
from flask import render_template, redirect, request, url_for, jsonify
from . import bp
from app.models.tables import Project, Comment, AlchemyEncoder
from app.database.sqlAlchemy import session

import json

@bp.route('/', methods = ['GET'])
@bp.route('/<int:project_id>/', methods = ['GET'])
def showprojects(project_id = None):
   
    if project_id:
       project = session.query(Project).filter_by(project_id=project_id).join(Comment).first()
       print('****', project)
       return jsonify (project)
   
    else:
       project = session.query(Project).all()
       return render_template("project.html", project=project)

# #Function to edit a project
# @bp.route("/<int:project_id>/", methods = ['GET'])
# def project(project_id): 
#     project = session.query(Project).filter_by(project_id=project_id).join(Comment).all()[0]
    
#     if request.method == 'GET':
#         coms = {"comm" : [json.dumps(c, cls=AlchemyEncoder ) for c in project.comments]}
#         project.update_comments()
#         session.commit()
#         p =  json.dumps(project, cls=AlchemyEncoder)
#         return redirect(url_for('projects.showprojects'))

#Function to add a project
@bp.route('/new',methods=['GET','POST'])
def newproject():
    if request.method == 'POST':
        newProject = Project(
            project_id = request.form['project_id'], 
            project_name = request.form['project_name'], 
            owner_id= request.form['owner_id'], 
            owner_username= request.form['owner_username']
        )
        
        session.add(newProject)
        session.commit()
        return redirect(url_for('projects.showprojects'))
    else:
       return render_template('newproject.html')
    
#Function to edit a project
@bp.route("/<int:project_id>/edit/", methods = ['GET', 'POST'])
def editproject(project_id):
    editedProject = session.query(Project).filter_by(project_id=project_id).one()
    if request.method == 'POST':
        if request.form['project_name']:
            editedProject.subject = request.form['project_name']
            return redirect(url_for('projects.showprojects'))
        if request.form['owner_id']:
            editedProject.subject = request.form['owner_id']
            return redirect(url_for('projects.showProjects'))
        if request.form['owner_username']:
           editedProject.subject = request.form['owner_username']
           return redirect(url_for('projects.showprojects'))
    else:
       return render_template('editProject.html', project = editedProject)
    
#Function to delete a project
@bp.route('/<int:project_id>/delete/', methods = ['GET','POST'])
def deleteproject(project_id):
    projectToDelete = session.query(Project).filter_by(project_id=project_id).one()
    if request.method == 'POST':
       session.delete(projectToDelete)
       session.commit()
       return redirect(url_for('projects.showprojects', project_id=project_id))
    else:
       return render_template('deleteproject.html',project = projectToDelete)


