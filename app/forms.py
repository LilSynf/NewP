from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class RequirementsForm(FlaskForm):
    project_name = StringField('Project Name', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    submit = SubmitField('Generate Program')