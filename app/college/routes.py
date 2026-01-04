from flask import render_template, request, redirect, url_for, flash
from app.college import college_bp
from app.models import College

@college_bp.route('/')
def index():
    search = request.args.get('search', '')
    colleges = College.get_all(search)
    return render_template('college/index.html', colleges=colleges, search=search)

@college_bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = {
            'code': request.form['code'],
            'name': request.form['name']
        }
        try:
            College.create(data)
            flash('College added successfully!', 'success')
            return redirect(url_for('college.index'))
        except Exception as e:
            flash(f'Error adding college: {str(e)}', 'danger')
    
    return render_template('college/add.html')

@college_bp.route('/edit/<code>', methods=['GET', 'POST'])
def edit(code):
    if request.method == 'POST':
        data = {
            'name': request.form['name']
        }
        try:
            College.update(code, data)
            flash('College updated successfully!', 'success')
            return redirect(url_for('college.index'))
        except Exception as e:
            flash(f'Error updating college: {str(e)}', 'danger')
    
    college = College.get_by_code(code)
    return render_template('college/edit.html', college=college)

@college_bp.route('/delete/<code>')
def delete(code):
    try:
        College.delete(code)
        flash('College deleted successfully!', 'success')
    except Exception as e:
        flash(f'Error deleting college: {str(e)}', 'danger')
    return redirect(url_for('college.index'))