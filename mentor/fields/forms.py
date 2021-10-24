from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField,SelectField
from wtforms.validators import DataRequired


class EntireJobForm(FlaskForm):
    fieldtitle = StringField()
    jobtitle = StringField()
    avg_salary = StringField()
    education_req = StringField()



FieldsField = SelectField(
        'Fields',
        choices=[('1','Architecture and Engineering Occupations'),
                 ('2','Arts, Design, Entertainment, Sports, and Media Occupations'),
                 ('3','Building and Grounds Cleaning and Maintenance Occupations'),
                 ('4','Business and Financial Operations Occupations'),
                 ('5','Community and Social Services Occupations'),
                 ('6','Computer and Mathematical Occupations'),
                 ('7','Construction and Extraction Occupations'),
                 ('8','Education, Training, and Library Occupations'),
                 ('9','Farming, Fishing, and Forestry Occupations'),
                 ('10','Food Preparation and Serving Related Occupations'),
                 ('11','Healthcare Practitioners and Technical Occupations'),
                 ('12','Healthcare Support Occupations'),
                 ('13','Installation, Maintenance, and Repair Occupations'),
                 ('14','Legal Occupations'),
                 ('15','Life, Physical, and Social Science Occupations'),
                 ('16','Management Occupations'),
                 ('17','Military Specific Occupations'),
                 ('18','Office and Administrative Support Occupations'),
                 ('19','Personal Care and Service Occupations'),
                 ('20','Production Occupations'),
                 ('21','Protective Service Occupations'),
                 ('22','Sales and Related Occupations')]
    )



























