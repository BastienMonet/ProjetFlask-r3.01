from .app import app
from flask import render_template, request
from monApp.models import Auteur, Livre
from monApp.form import FormAuteur, FormLivre

from flask import url_for , redirect
from .app import db


@app.route ('/auteur/save/', methods =("POST" ,))
def saveAuteur():
    updatedAuteur = None
    unForm = FormAuteur()
    #recherche de l'auteur à modifier
    idA = int(unForm.idA.data)
    updatedAuteur = Auteur.query.get(idA)
    #si les données saisies sont valides pour la mise à jour
    if unForm.validate_on_submit():
        updatedAuteur.Nom = unForm.Nom.data
        db.session.commit()
        return redirect(url_for('viewAuteur', idA=updatedAuteur.idA))
    return render_template("auteur_update.html",selectedAuteur=updatedAuteur, updateForm=unForm)


@app.route('/auteurs/<idA>/view/')
def viewAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur (idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_view.html",selectedAuteur=unAuteur, viewForm=unForm)


@app.route('/livres/<idL>/view/')
def viewLivre(idL):
    unLivre = Livre.query.get(idL)
    unForm = FormLivre(idL=unLivre.idL , titre=unLivre.Titre, prix=unLivre.Prix, url=unLivre.Url, img=unLivre.Img, auteur_id=unLivre.auteur_id)
    return render_template("livre_view.html",selectedLivre=unLivre, viewForm=unForm)



@app.route('/auteur/')
def createAuteur():
    unForm = FormAuteur()
    return render_template("auteur_create.html", createForm=unForm)

@app.route('/livre/')
def createLivre():
    unForm = FormLivre()
    return render_template("livre_create.html", createForm=unForm)


@app.route('/')
def helloworld() :
    return "Hello world !"

@app.route('/auteurs/')
def getAuteurs():
    lesAuteurs = Auteur.query.all()
    return render_template('auteurs_list.html', title="R3.01 Dev Web avec Flask", auteurs=lesAuteurs)

@app.route('/livres/')
def getLivres():
    lesLivre = Livre.query.all()
    return render_template('livres_list.html', title="R3.01 Dev Web avec Flask, les livres", livres=lesLivre)


@app.route('/auteurs/<idA>/update/')
def updateAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA , Nom=unAuteur.Nom)
    return render_template("auteur_update.html",selectedAuteur=unAuteur, updateForm=unForm)

@app.route("/about/")
def about() :
    return render_template("about.html", config=app.config["ABOUT"])


@app.route("/contact/")
def contact() :
    return render_template("contact.html", title="lol", contact="ça marche")

@app.route('/index/')
def index():
    # request.path renvoie la route demandée
    #  request.method renvoie la méthode HTTP utilisée
    #  request.args renvoie un dictionnaire contenant les paramètres présents dans l'URL.
    if len(request.args)==0:
        return render_template("index.html",title="R3.01 Dev Web avec Flask",name="Cricri")
    else :
        param_name = request.args.get('name')
    return render_template("index.html",title="R3.01 Dev Web avec Flask",name=param_name)



@app.route('/base/')
def base():
    return render_template("baseMieux.html")

@app.route ('/auteur/insert/', methods =("POST" ,))
def insertAuteur():
    insertedAuteur = None
    unForm = FormAuteur()
    if unForm.validate_on_submit():
        insertedAuteur = Auteur(Nom=unForm.Nom.data)
        db.session.add(insertedAuteur)
        db.session.commit()
        insertedId = Auteur.query.count()
        return redirect(url_for('viewAuteur', idA=insertedId))
    return render_template("auteur_create.html", createForm=unForm)


@app.route ('/livres/insert/', methods =("POST" ,))
def insertLivre():
    insertedLivre = None
    unForm = FormLivre()
    if unForm.validate_on_submit():
        insertedLivre = Livre(Prix=unForm.prix.data, Titre=unForm.titre.data, Url=unForm.url.data, Img=unForm.img.data, auteur_id=unForm.auteur.data)
        db.session.add(insertedLivre)
        db.session.commit()
        insertedId = Livre.query.count()
        return redirect(url_for('viewLivre', idL=insertedId))
    return render_template("livre_create.html", createForm=unForm)


@app.route('/auteurs/<idA>/delete/')
def deleteAuteur(idA):
    unAuteur = Auteur.query.get(idA)
    unForm = FormAuteur(idA=unAuteur.idA, Nom=unAuteur.Nom)
    return render_template("auteur_delete.html",selectedAuteur=unAuteur, deleteForm=unForm)

@app.route ('/auteur/erase/', methods =("POST" ,))
def eraseAuteur():
    deletedAuteur = None
    unForm = FormAuteur()
    #recherche de l'auteur à supprimer
    idA = int(unForm.idA.data)
    deletedAuteur = Auteur.query.get(idA)
    #suppression
    db.session.delete(deletedAuteur)
    db.session.commit()
    return redirect(url_for('getAuteurs'))


if __name__== "__main__" :
    app.run()