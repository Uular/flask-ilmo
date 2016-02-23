from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField, ValidationError
from wtforms.validators import DataRequired, Email, InputRequired


class KmpForm(Form):
    name = StringField('Nimi', id='name', validators=[DataRequired()])
    email = StringField('Sähköposti', id='email', validators=[DataRequired(), Email()])
    phone = StringField('Puhelinnumero', id='phone', validators=[DataRequired()])
    guild = RadioField('guild',
                       choices=[('otit', 'OTiT'), 
                                ('sik', 'SIK'), 
                                ('muu', 'Muu')], 
                       default='otit', validators=[InputRequired()])
    station = RadioField('station',
                         choices=[('linnanmaa', 'Yliopisto'),
                                  ('tuira', 'Tuira'),
                                  ('keskusta','Linja-autoasema')],
                         default='linnanmaa', validators=[InputRequired()])
    sitsit = BooleanField('sitsit', default=False)

    @staticmethod
    def validate_sitsit(form, field):
        if field.data == True and form.guild.data != 'otit':
            raise ValidationError('Vain tietoteekkarit pääsevät Titeeneille!')
