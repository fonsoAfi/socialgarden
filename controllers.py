"""
This file defines actions, i.e. functions the URLs are mapped into
The @action(path) decorator exposed the function at URL:

    http://127.0.0.1:8000/{app_name}/{path}

If app_name == '_default' then simply

    http://127.0.0.1:8000/{path}

If path == 'index' it can be omitted:

    http://127.0.0.1:8000/

The path follows the bottlepy syntax.

@action.uses('generic.html')  indicates that the action uses the generic.html template
@action.uses(session)         indicates that the action uses the session
@action.uses(db)              indicates that the action uses the db
@action.uses(T)               indicates that the action uses the i18n & pluralization
@action.uses(auth.user)       indicates that the action requires a logged in user
@action.uses(auth)            indicates that the action requires the auth object

session, db, T, auth, and tempates are examples of Fixtures.
Warning: Fixtures MUST be declared with @action.uses({fixtures}) else your app will result in undefined behavior
"""
from contextlib import redirect_stderr
from datetime import datetime
from py4web import action, request, abort, redirect, URL, response , Session
from requests.models import REDIRECT_STATI
from yatl.helpers import A
from .common import (
    db,
    session,
    T,
    cache,
    auth,
    logger,
    authenticated,
    unauthenticated,
    flash,
)
import secrets
from .utils.validations import *
# from .utils.database_operations import *
from .models import Persistencia
from .utils.passw_util import *
from .common import *
from .settings import *
from .orm.Usuario import Usuario


# Creo el objeto de mi clase Persistencia
mydb = Persistencia()


@action("index")
@action.uses("index", T)
def index():
    usuario = Usuario(nombre='Wilfredo',nacimiento='1990-09-01')
    usuario.crear_usuario()
    return dict()

# Expongo la sesión
@action("register", method = ["GET","POST"])
@action.uses(session, "autenticacion/register.html", db)
def register():

    datos_usuario = {}
    coluns = ("email", "nic")
    tabla = "Usuario"
    datos_usuario.update(
        email = request.POST.get("email"),
        nic = request.POST.get("nic"),
    )
    if request.method == "POST":
        condicion = f"{coluns[0]} = %s AND {coluns[1]} = %s"
        valores = (datos_usuario[coluns[0]], datos_usuario[coluns[1]])
        resultados = select(MYDB_CONEX, tabla, coluns, condicion, valores)
        if len(resultados) == 0:
            datos_usuario.update(
                nombre = request.POST.get("nombre"),
                apellido1 = request.POST.get("apellido1"),
                apellido2 = request.POST.get("apellido2"),
                nacimiento = request.POST.get("nacimiento"),
                genero = request.POST.get("genero"),
                descripcion = None,
                passw = hash_password(request.POST.get("passw")),
                fecha_hora = datetime.now(),
                id_direccion = None
            )
            insertar_un_registro(MYDB_CONEX, tabla, datos_usuario) 

            direccion = {}
            direccion.update(
                id_direccion = None,
                localidad = request.POST.get("localidad"),
                numero = request.POST.get("numero"),
                codigo_postal = request.POST.get("cp"),
                puerta = request.POST.get("puerta"),
                letra = request.POST.get("letra")
            )
            tabla = "Direccion"
            insertar_un_registro(MYDB_CONEX, tabla, direccion) 

            telefono = {}
            telefono.update(
                telefono = request.POST.get("telefono"),
                Usuario_email = request.POST.get("email")
            )
            tabla = "Telefono"
            insertar_un_registro(MYDB_CONEX, tabla, telefono)
            
            if request.POST.get("usuario") == "Jardinero":
                tabla = "Jardinero"
                jardinero = {}
                jardinero.update(
                    email = request.POST.get("email"),
                    experiencia = request.POST.get("experiencia"),
                    empresa = request.POST.get("empresa"),
                    visibilidad = request.POST.get("visibilidad")
                )
                insertar_un_registro(MYDB_CONEX, tabla, jardinero)
            else:
                tabla = "Propietario"
                propietario = {}
                propietario.update(email = datos_usuario["email"])
                insertar_un_registro(MYDB_CONEX, tabla, propietario)

            # Cierro la conexión después de realizar las operaciones sino me daria error
        else:
            return f"El usuario con mail {coluns[0]} ya está registrado"
        
        MYDB_CONEX.close()
            
            # Cerrar sesion
        session.clear()
        redirect('index')

    return dict(register=register)


@action("login", method = ["GET","POST"])
@action.uses(session, "autenticacion/login.html")
def login():
    mensaje = ""
    if request.method == "POST":
        email = request.POST.get("email")
        passw = request.POST.get("passw")
        condicion = f"email = %s"
        conexion = getConexionDB(host="localhost",database="SOCIALGARDEN", user="admin", password="admin")
        resultados = select(conexion, "Usuario", "clave", condicion, (email,))
        if len(resultados) != 0 and verify_password(passw, resultados[0][0]):
            if(len(select(conexion, "Jardinero", "email", condicion, (email,)))):
                redirect('perfil_jardinero')
            elif (len(select(conexion, "Propietario", "email", condicion, (email,))) != 0):
                redirect('perfil_propietario')
            else:
                mensaje = f"El mail {email} no está registrado"
            # Comprobar que tipo de usuario es y redirigir al perfil correspondiente
    return dict(mensaje=mensaje)


@action("change_password", method = ["GET","POST"])
@action.uses(session, "autenticacion/change_password.html", db)
def change_password(mensaje=''):
    if request.method == "POST":
        tabla = "Usuario"
        email = request.POST["email"]
        passw = request.POST["passw"]
        campos = (hash_password(passw), email)
        condicion = f"WHERE email = %s"
        rowcount = update_un_registro(MYDB_CONEX, tabla, "clave", condicion, campos)
        MYDB_CONEX.close()
        session.clear()
        if rowcount != 0:
            mensaje = "La contraseña se ha cambiado correctamente"
        else:
            mensaje = f"No se ha podido cambiar la contraseña porque no está ergistrado el mail {email}"
    return dict(mensaje=mensaje)


@action("logout")
@action.uses(session, "autenticacion/logout.html")
def logout():
    session.clear()
    redirect('index')
    return dict()


@action("edit_profile")
@action.uses("autenticacion/edit_profile.html", T)
def edit_profile():
    return dict()


@action("perfil_jardinero")
@action.uses("perfiles/perfil_jardinero.html", T)
def perfil_jardinero():
    return dict()


@action("perfil_propietario")
@action.uses(session, "perfiles/perfil_propietario.html", T)
def perfil_propietario():
    print(session.items())

    return dict()

# Controlador para cargar las fotos
@action('mostrar_foto')
@action.uses('mostrar_foto.html', db, session)
def mostrar_foto():
    nombre_foto = 'perfil_propietario.jpg'
    # foto_id = session.get('foto_id')
    # if foto_id:
    #     usuario = db.usuario[foto_id]
    foto_url = f"static/uploads/{nombre_foto}"
    # else:
    #     foto_url = None

    return dict(foto_url=foto_url)


@action('tarea', method=["GET","POST"])
@action.uses('registro_tareas/tarea.html', db)
def tarea():
    return dict()


@action('privado', method=["GET","POST"])
@action.uses('chat/privado.html', db)
def privado():
    datos = request.json
    print(datos)
    # Ahora habria que comprobar lo correspondiente e insertar en la Base Datos
    return dict()