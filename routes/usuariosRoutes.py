from fastapi import APIRouter
from pydantic import BaseModel
from controller import usuariosController

appUsuario = APIRouter()

# ---------- Pydantic Models ----------

class CrearUsuarioRequest(BaseModel):
    nombre: str
    apellido: str
    email: str
    contrasena: str
    rol: int

class ActualizarUsuarioRequest(BaseModel):
    nombre: str
    apellido: str
    email: str
    contrasena: str
    rol: int

class LoginRequest(BaseModel):
    email: str
    contrasena: str

class CrearRolRequest(BaseModel):
    nombre_rol: str

class ActualizarRolRequest(BaseModel):
    nombre_rol: str

# ---------- Endpoints Usuarios ----------

@appUsuario.get("/usuarios", tags=["Usuarios"])
def obtener_usuarios():
    return usuariosController.obtener_usuarios()

@appUsuario.get("/usuarios/{usuario_id}", tags=["Usuarios"])
def obtener_usuario_por_id(usuario_id: int):
    return usuariosController.obtener_usuario_por_id(usuario_id)

@appUsuario.post("/usuarios", tags=["Usuarios"])
def crear_usuario(request: CrearUsuarioRequest):
    return usuariosController.crear_usuario(
        request.nombre,
        request.apellido,
        request.email,
        request.contrasena,
        request.rol
    )

@appUsuario.put("/usuarios/{usuario_id}", tags=["Usuarios"])
def actualizar_usuario(usuario_id: int, request: ActualizarUsuarioRequest):
    return usuariosController.actualizar_usuario(
        usuario_id,
        request.nombre,
        request.apellido,
        request.email,
        request.contrasena,
        request.rol
    )

@appUsuario.delete("/usuarios/{usuario_id}", tags=["Usuarios"])
def eliminar_usuario(usuario_id: int):
    return usuariosController.eliminar_usuario(usuario_id)

@appUsuario.post("/usuarios/login", tags=["Usuarios"])
def login_usuario(request: LoginRequest):
    return usuariosController.login_usuario(
        request.email,
        request.contrasena
    )

@appUsuario.get("/usuarios/rol/{rol_id}", tags=["Usuarios"])
def obtener_usuarios_por_rol(rol_id: int):
    return usuariosController.obtener_usuarios_por_rol(rol_id)

# ---------- Endpoints Roles ----------

@appUsuario.get("/roles", tags=["Roles"])
def obtener_roles():
    return usuariosController.obtener_roles()

@appUsuario.get("/roles/{rol_id}", tags=["Roles"])
def obtener_rol_por_id(rol_id: int):
    return usuariosController.obtener_rol_por_id(rol_id)

@appUsuario.post("/roles", tags=["Roles"])
def crear_rol(request: CrearRolRequest):
    return usuariosController.crear_rol(request.nombre_rol)

@appUsuario.put("/roles/{rol_id}", tags=["Roles"])
def actualizar_rol(rol_id: int, request: ActualizarRolRequest):
    return usuariosController.actualizar_rol(rol_id, request.nombre_rol)

@appUsuario.delete("/roles/{rol_id}", tags=["Roles"])
def eliminar_rol(rol_id: int):
    return usuariosController.eliminar_rol(rol_id)

@appUsuario.put("/usuarios/{usuario_id}/rol", tags=["Usuarios"])
def cambiar_rol_usuario(usuario_id: int, nuevo_rol_id: int):
    return usuariosController.cambiar_rol_usuario(usuario_id, nuevo_rol_id)
