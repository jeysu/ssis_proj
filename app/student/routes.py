from flask import render_template, request, redirect, url_for, flash
from app.student import student_bp
from app.models import Student, Program
import cloudinary.uploader
import os

@student_bp.route('/')
def index():
    search = request.args.get('search', '')
    students = Student.get_all(search)
    return render_template('student/index.html', students=students, search=search)

@student_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        photo_url = None
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename != '':
                try:
                    upload_result = cloudinary.uploader.upload(photo)
                    photo_url = upload_result['secure_url']
                except Exception as e:
                    flash(f'Error uploading photo: {str(e)}', 'danger')
                    photo_url = None
        
        data = {
            'id': request.form['id'],
            'firstname': request.form['firstname'],
            'lastname': request.form['lastname'],
            'course_code': request.form['course_code'],
            'year': request.form['year'],
            'gender': request.form['gender'],
            'photo_url': photo_url
        }
        try:
            Student.create(data)
            flash('Student added successfully!', 'success')
            return redirect(url_for('student.index'))
        except Exception as e:
            flash(f'Error adding student: {str(e)}', 'danger')
    
    programs = Program.get_all()
    return render_template('student/add.html', programs=programs)

@student_bp.route('/edit/<student_id>', methods=['GET', 'POST'])
def edit(student_id):
    if request.method == 'POST':
        photo_url = request.form.get('existing_photo_url')
        if 'photo' in request.files:
            photo = request.files['photo']
            if photo.filename != '':
                try:
                    upload_result = cloudinary.uploader.upload(photo)
                    photo_url = upload_result['secure_url']
                except Exception as e:
                    flash(f'Error uploading photo: {str(e)}', 'danger')
                    photo_url = request.form.get('existing_photo_url')
        
        data = {
            'firstname': request.form['firstname'],
            'lastname': request.form['lastname'],
            'course_code': request.form['course_code'],
            'year': request.form['year'],
            'gender': request.form['gender'],
            'photo_url': photo_url
        }
        try:
            Student.update(student_id, data)
            flash('Student updated successfully!', 'success')
            return redirect(url_for('student.index'))
        except Exception as e:
            flash(f'Error updating student: {str(e)}', 'danger')
    
    student = Student.get_by_id(student_id)
    programs = Program.get_all()
    return render_template('student/edit.html', student=student, programs=programs)

@student_bp.route('/delete/<student_id>')
def delete(student_id):
    try:
        Student.delete(student_id)
        flash('Student deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting student: {str(e)}', 'danger')
    return redirect(url_for('student.index'))