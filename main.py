from authentification import Authentification
from database import Database

from hashage import hashage
import eel
# import webbrowser
# import os

login = Authentification()
dtb = Database()


eel.init("budget_buddy/web")
# eel.start("index.html",)


@eel.expose
def Signup(nom: str, prenom: str, email: str, passwd: str):

    if "" not in [nom, prenom, email, passwd]:
        # Si l'email n'existe pas alors il crée l'utlisateur
        if not login.read(email):
            # hashage password
            password_hash = hashage(passwd)
            try:
                login.set_new_user(nom, prenom, email, password_hash)
                print("ok")
                global mail
                mail = email
                # eel.redirect_chat()()
                # webbrowser.open('http://localhost:9998/index_chat.html')
            except Exception as e:
                print(f"Il semble y avoir une erreur veuillez réessayer, {e}")


@eel.expose
def Signin(email: str, passwd: str):
    if "" not in [email, passwd]:
        for i in login.read(email):
            # hashage password
            password_hash = hashage(passwd)
            if i[3] == email and i[4] == password_hash:
                global mail
                mail = email
                print("user connected !")
                # eel.redirect_chat()()
                # webbrowser.open('http://localhost:9998/index_chat.html')


def get_iduser():
    '''get_iduser is fonction how get email from Signin

    Returns:
        _description_
    '''
    return login.get_Id_user(mail)


# @eel.expose
# def decode_simple(msg:str):
#     print(codec.decodage_simple(msg))
#     return codec.decodage_simple(msg)


@eel.expose
def close():
    dtb.close()


if __name__ == "__main__":
    # gets the index.html file in mozilla
    eel.start("index.html", mode='mozilla', port=9988)
