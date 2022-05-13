from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from hw_tracker.auth import login_required
from hw_tracker.db import get_db

bp = Blueprint('homework', __name__)

@bp.route('/')
def index():
    db = get_db()
    hw_items = db.execute(
        'SELECT hw.id, course, name, typehw, desc, duedate, completed, author_id'
        '   FROM hw JOIN user u on hw.author_id = u.id'
    ).fetchall()
    return render_template('homework/index.html', hw_items=hw_items)

@bp.route('/create', methods=('POST', 'GET'))
@login_required
def create():
    if request.method =='POST':
        course = request.form.get("course")
        name = request.form.get("name")
        type = request.form.get("type")
        desc = request.form.get("description")
        dd = request.form.get("duedate")
        error = None

        if not course or not name or not type or not desc or not dd:
            error = 'Please enter all fields'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO hw (course, name, typehw, desc, duedate, completed, author_id)'
                '   VALUES (?, ?, ?, ?, ?, ?, ?)',
                (course, name, type, desc, dd, 'no', g.user['id'])
            )
            db.commit()
            return redirect(url_for('homework.index'))

    return render_template('homework/create.html')


def get_hw(id, check_author=True):
    hw = get_db().execute(
        'SELECT hw.id, course, name, typehw, desc, duedate, completed, author_id'
        '   FROM hw JOIN user u on hw.author_id = u.id'
        '   WHERE hw.id = ?',
        (id,)
    ).fetchone()

    if hw is None:
        abort(404, f'Homework id {id} doesn\'t exist.')

    if check_author and hw['author_id'] != g.user['id']:
        abort(403)

    return hw

@bp.route('/<int:id>/update', methods=('POST', 'GET'))
@login_required
def update(id):
    hw = get_hw(id)

    if request.method == 'POST':
        course = request.form.get("course")
        name = request.form.get("name")
        type = request.form.get("type")
        desc = request.form.get("description")
        dd = request.form.get("duedate")
        error = None

        if not course or not name or not type or not desc or not dd:
            error = 'Please enter all fields'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE hw SET course = ?, name = ?, typehw = ?, desc = ?, duedate = ?, completed = ?'
                '   WHERE id = ?',
                (course, name, type, desc, dd, 'no', id)
            )
            db.commit()
            return redirect(url_for('homework.index'))
    
    return render_template('homework/update.html', hw=hw)
        

@bp.route('/<int:id>/delete')
@login_required
def delete(id):
    get_hw(id)
    db = get_db()
    db.execute('DELETE FROM hw WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('homework.index'))