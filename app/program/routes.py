from flask import render_template, request, redirect, url_for, flash
from app.program import program_bp
from app.models import Program, College

@program_bp.route('/')
def index():
    search = request.args.get('search', '')
    page = int(request.args.get('page', 1))
    per_page = 7
    
    # Get all programs for counting total
    all_programs = Program.get_all(search)
    total_programs = len(all_programs)
    total_pages = (total_programs + per_page - 1) // per_page
    
    # Calculate offset and slice the programs
    offset = (page - 1) * per_page
    programs = all_programs[offset:offset + per_page]
    
    return render_template('program/index.html', 
                         programs=programs, 
                         search=search,
                         page=page,
                         total_pages=total_pages,
                         total_programs=total_programs)

@program_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = {
            'code': request.form['code'],
            'name': request.form['name'],
            'college_code': request.form['college_code']
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
            'college_code': request.form['college_code']
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