from flask import render_template, request, redirect, url_for, flash
from app.program import program_bp
from app.models import Program, College

@program_bp.route('/')
def index():
    search = request.args.get('search', '')
    programs = Program.get_all(search)
    return render_template('program/index.html', programs=programs, search=search)

@program_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = {
            'code': request.form['code'],
            'name': request.form['name'],
            'college_code': request.form['college_code']  # Changed
        }
        try:
            Program.create(data)
            flash('Program added successfully!', 'success')
            return redirect(url_for('program.index'))
        except Exception as e:
            flash(f'Error adding program: {str(e)}', 'danger')
    
    colleges = College.get_all()
    return render_template('program/add.html', colleges=colleges)

@program_bp.route('/edit/<code>', methods=['GET', 'POST'])
def edit(code):
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'college_code': request.form['college_code']  # Changed
        }
        try:
            Program.update(code, data)
            flash('Program updated successfully!', 'success')
            return redirect(url_for('program.index'))
        except Exception as e:
            flash(f'Error updating program: {str(e)}', 'danger')
    
    program = Program.get_by_code(code)
    colleges = College.get_all()
    return render_template('program/edit.html', program=program, colleges=colleges)

@program_bp.route('/delete/<code>')
def delete(code):
    try:
        Program.delete(code)
        flash('Program deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting program: {str(e)}', 'danger')
    return redirect(url_for('program.index'))