from app import app
from flask import render_template, request, redirect, url_for, send_file
from app.forms import RequirementsForm
from generate_code import generate_program

@app.route('/', methods=['GET', 'POST'])
def index():
    form = RequirementsForm()
    if form.validate_on_submit():
        requirements = form.requirements.data
        project_name = form.project_name.data
        file_path = generate_program(requirements, project_name)
        return send_file(file_path, as_attachment=True)
    return render_template('index.html', form=form)