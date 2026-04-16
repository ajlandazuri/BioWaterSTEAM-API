from fastapi.responses import JSONResponse
from model import usuariosModel
# ------- USUARIOS --------

def obtener_usuarios():
    try:
        usuarios = usuariosModel.obtener_usuarios()
        if usuarios:
            return JSONResponse(status_code=200, content={"status": 200, "usuarios": usuarios})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron usuarios"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def obtener_usuario_por_id(usuario_id: int):
    try:
        usuario = usuariosModel.obtener_usuario_por_id(usuario_id)
        if usuario:
            return JSONResponse(status_code=200, content={"status": 200, "usuario": usuario})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Usuario no encontrado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def crear_usuario(nombre: str, apellido: str, email: str, contrasena: str, rol: int):
    try:
        usuario_id = usuariosModel.crear_usuario(nombre, apellido, email, contrasena, rol)
        if usuario_id:
            return JSONResponse(status_code=201, content={"status": 201, "message": "Usuario creado exitosamente", "id": usuario_id})
        else:
            return JSONResponse(status_code=400, content={"status": 400, "message": "No se pudo crear el usuario"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def actualizar_usuario(usuario_id: int, nombre: str, apellido: str, email: str, contrasena: str, rol: int):
    try:
        actualizado = usuariosModel.actualizar_usuario(usuario_id, nombre, apellido, email, contrasena, rol)
        if actualizado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Usuario actualizado correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Usuario no encontrado o no actualizado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def eliminar_usuario(usuario_id: int):
    try:
        eliminado = usuariosModel.eliminar_usuario(usuario_id)
        if eliminado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Usuario eliminado correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Usuario no encontrado o no eliminado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def login_usuario(email: str, contrasena: str):
    try:
        usuario = usuariosModel.login_usuario(email, contrasena)
        if usuario:
            return JSONResponse(status_code=200, content={"status": 200, "usuario": usuario})
        else:
            return JSONResponse(status_code=401, content={"status": 401, "message": "Credenciales incorrectas"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def obtener_usuarios_por_rol(rol_id: int):
    try:
        usuarios = usuariosModel.obtener_usuarios_por_rol(rol_id)
        if usuarios:
            return JSONResponse(status_code=200, content={"status": 200, "usuarios": usuarios})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron usuarios con ese rol"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

# ------- ROLES --------

def obtener_roles():
    try:
        roles = usuariosModel.obtener_roles()
        if roles:
            return JSONResponse(status_code=200, content={"status": 200, "roles": roles})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron roles"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def obtener_rol_por_id(rol_id: int):
    try:
        rol = usuariosModel.obtener_rol_por_id(rol_id)
        if rol:
            return JSONResponse(status_code=200, content={"status": 200, "rol": rol})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Rol no encontrado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def crear_rol(nombre_rol: str):
    try:
        rol_id = usuariosModel.crear_rol(nombre_rol)
        if rol_id:
            return JSONResponse(status_code=201, content={"status": 201, "message": "Rol creado exitosamente", "id": rol_id})
        else:
            return JSONResponse(status_code=400, content={"status": 400, "message": "No se pudo crear el rol"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def actualizar_rol(rol_id: int, nombre_rol: str):
    try:
        actualizado = usuariosModel.actualizar_rol(rol_id, nombre_rol)
        if actualizado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Rol actualizado correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Rol no encontrado o no actualizado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def eliminar_rol(rol_id: int):
    try:
        eliminado = usuariosModel.eliminar_rol(rol_id)
        if eliminado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Rol eliminado correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Rol no encontrado o no eliminado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def cambiar_rol_usuario(usuario_id: int, nuevo_rol_id: int):
    try:
        cambiado = usuariosModel.cambiar_rol_usuario(usuario_id, nuevo_rol_id)
        if cambiado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Rol de usuario cambiado correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Usuario no encontrado o rol no cambiado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})