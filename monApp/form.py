from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, FloatField
from wtforms.validators import DataRequired

class FormAuteur(FlaskForm):
    idA=HiddenField('idA')
    Nom = StringField ('Nom', validators =[DataRequired()])



class FormLivre(FlaskForm):
    idL=HiddenField('idL')
    prix = FloatField('Prix', validators=[DataRequired()])
    titre = StringField('Titre', validators =[DataRequired()])
    url = StringField('Url', validators =[DataRequired()])
    img = StringField('Img', validators =[DataRequired()])
    auteur = StringField('Auteur', validators =[DataRequired()])