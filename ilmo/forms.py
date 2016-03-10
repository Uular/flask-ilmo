from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, RadioField, ValidationError
from wtforms.validators import DataRequired, Email, InputRequired, Length


class KmpForm(Form):
    name = StringField('Nimi', id='name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Sähköposti', id='email', validators=[DataRequired(), Email(), Length(max=50)])
    phone = StringField('Puhelinnumero', id='phone', validators=[DataRequired(), Length(max=15)])
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
    friends = StringField('Hyttikaveritoiveet', id='friends')
    nationality = StringField('Kansallisuus', id='nationality')

    @staticmethod
    def validate_sitsit(form, field):
        if field.data == True and form.guild.data != 'otit':
            raise ValidationError('Vain tietoteekkarit pääsevät Titeeneille!')

    @staticmethod
    def validate_nationality(form, field):
        if form.guild.data == 'sik' and not field.data:
            raise ValidationError('Ole hyvä ja ilmoita kansallisuus risteilyä varten!')


class HumuForm(Form):
    name = StringField('Nimi', id='name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Sähköposti', id='email', validators=[DataRequired(), Email(), Length(max=50)])
    phone = StringField('Puhelinnumero', id='phone', validators=[DataRequired(), Length(max=15)])
    guild = RadioField('guild',
                       choices=[('otit', 'OTiT'),
                                ('olo', 'OLO'),
                                ('communica', 'Communica'),
                                ('muu', 'Muu')],
                       default='otit', validators=[InputRequired()])
    alcohol_free = BooleanField('Alkoholiton', default=False)
    wine = RadioField('wine',
                         choices=[('puna', 'Punaviini'),
                                  ('valko', 'Valkoviini')])
    mild = RadioField('mild',
                      choices=[('olut', 'Olut'),
                               ('siideri', 'Siideri'),
                               ('lonkero', 'Lonkero')])
    avec = BooleanField('Avec', id='avec', default=False)

    @staticmethod
    def validate_wine(form, field):
        if not form.alcohol_free.data and not field.data:
            raise ValidationError('Ole hyvä ja valitse viini!')

    @staticmethod
    def validate_mild(form, field):
        if not form.alcohol_free.data and not field.data:
            raise ValidationError('Ole hyvä ja valitse mieto!')
