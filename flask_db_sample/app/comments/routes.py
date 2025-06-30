
from flask import render_template, redirect, request, url_for, jsonify
from . import bp
from app.models.tables import Comment
from app.database.sqlAlchemy import session

@bp.route('/<int:comment_id>', methods=['GET'])
@bp.route('/', methods=['GET'])
def showcomments(comment_id=0):
    if comment_id == 0:
        comments = session.query(Comment).all()
        return render_template("comment.html", comments=comments)
    else:
        c = session.query(Comment).filter_by(comment_id=comment_id).first()
        return jsonify(c)

#Function to add a comment
@bp.route('/new',methods=['GET','POST'])
def newcomment():
    if request.method == 'POST':
        newcomment = Comment(
            comment = request.form['comment'], 
            commenter_id = request.form['commenter_id'], 
            commenter_username = request.form['commenter_id'], 
            p_name = request.form['project_name']
        )
        session.add(newcomment)
        session.commit()
        return redirect(url_for('comments.showcomments'))
    else:
       return render_template('newcomment.html')
#Function to edit a comment
@bp.route("/<int:comment_id>/edit/", methods = ['GET', 'POST'])
def editcomment(comment_id):
    editedcomment = session.query(Comment).filter_by(comment_id=comment_id).one()
    if request.method == 'POST':
        if request.form['comment']:
            editedcomment.subject = request.form['comment']
            return redirect(url_for('comments.showcomments'))
    else:
       return render_template('editcomment.html', comment = editedcomment)
#Function to delete a comment
@bp.route('/<int:comment_id>/delete/', methods = ['GET','POST'])
def deletecomment(comment_id):
    commentToDelete = session.query(Comment).filter_by(comment_id=comment_id).one()
    if request.method == 'POST':
       session.delete(commentToDelete)
       session.commit()
       return redirect(url_for('comments.showcomments', comment_id=comment_id))
    else:
       return render_template('deletecomment.html',comment = commentToDelete)


