from flask_wtf import FlaskForm 
from wtforms import StringField, SubmitField,TextAreaField
from wtforms.validators import DataRequired, ValidationError

class GenerateForm(FlaskForm):
    app_concept = TextAreaField('App Concept', validators=[DataRequired()])
    generate = SubmitField('Generate')
    
    def validate_app_concept(self, app_concept):
        split_concepts = app_concept.data.split(" ")
        
        if 'app' not in split_concepts and 'business' not in split_concepts:
            raise ValidationError("Describe the concept to contains the 'app' or 'business' word ")
        
