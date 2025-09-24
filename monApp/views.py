from .app import app
from flask import render_template, request
from monApp.models import Auteur, Livre

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



if __name__== "__main__" :
    app.run()