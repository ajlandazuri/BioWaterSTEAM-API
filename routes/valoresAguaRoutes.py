from fastapi import APIRouter
from pydantic import BaseModel
from datetime import date
from controller import valoresAguaController

appValoresAgua = APIRouter()

# ---------- Pydantic Models ----------

class CrearLocacionRequest(BaseModel):
    nombre_lugar: str

class ActualizarLocacionRequest(BaseModel):
    nombre_lugar: str

class CrearValorAguaRequest(BaseModel):
    ph: str
    solidos_disueltos: str
    temperatura: str
    locacion_id: int

class ActualizarValorAguaRequest(BaseModel):
    ph: str
    solidos_disueltos: str
    temperatura: str
    locacion_id: int

class FiltroFechasRequest(BaseModel):
    fecha_inicio: date
    fecha_fin: date

class CambiarLocacionActualRequest(BaseModel):
    id_locacion: int

class CambiarEstadoMonitoreoRequest(BaseModel):
    activado: bool

# ---------- Endpoints Locaciones ----------

@appValoresAgua.get("/locaciones", tags=["Locaciones"])
def obtener_locaciones():
    return valoresAguaController.obtener_locaciones()

@appValoresAgua.get("/locaciones/{locacion_id}", tags=["Locaciones"])
def obtener_locacion_por_id(locacion_id: int):
    return valoresAguaController.obtener_locacion_por_id(locacion_id)

@appValoresAgua.post("/locaciones", tags=["Locaciones"])
def crear_locacion(request: CrearLocacionRequest):
    return valoresAguaController.crear_locacion(request.nombre_lugar)

@appValoresAgua.put("/locaciones/{locacion_id}", tags=["Locaciones"])
def actualizar_locacion(locacion_id: int, request: ActualizarLocacionRequest):
    return valoresAguaController.actualizar_locacion(locacion_id, request.nombre_lugar)

@appValoresAgua.delete("/locaciones/{locacion_id}", tags=["Locaciones"])
def eliminar_locacion(locacion_id: int):
    return valoresAguaController.eliminar_locacion(locacion_id)

# ---------- Endpoints Valores Agua ----------

@appValoresAgua.get("/valores-agua", tags=["Valores Agua"])
def obtener_valores_agua():
    return valoresAguaController.obtener_valores_agua()

@appValoresAgua.get("/valores-agua/{valor_id}", tags=["Valores Agua"])
def obtener_valor_agua_por_id(valor_id: int):
    return valoresAguaController.obtener_valor_agua_por_id(valor_id)

@appValoresAgua.post("/valores-agua", tags=["Valores Agua"])
def crear_valor_agua(request: CrearValorAguaRequest):
    return valoresAguaController.crear_valor_agua(
        request.ph,
        request.solidos_disueltos,
        request.temperatura,
        request.locacion_id
    )

@appValoresAgua.put("/valores-agua/{valor_id}", tags=["Valores Agua"])
def actualizar_valor_agua(valor_id: int, request: ActualizarValorAguaRequest):
    return valoresAguaController.actualizar_valor_agua(
        valor_id,
        request.ph,
        request.solidos_disueltos,
        request.temperatura,
        request.locacion_id
    )

@appValoresAgua.delete("/valores-agua/{valor_id}", tags=["Valores Agua"])
def eliminar_valor_agua(valor_id: int):
    return valoresAguaController.eliminar_valor_agua(valor_id)

@appValoresAgua.get("/valores-agua/locacion/{locacion_id}", tags=["Valores Agua"])
def obtener_valores_por_locacion(locacion_id: int):
    return valoresAguaController.obtener_valores_por_locacion(locacion_id)

@appValoresAgua.post("/valores-agua/fecha", tags=["Valores Agua"])
def obtener_valores_por_fecha(request: FiltroFechasRequest):
    return valoresAguaController.obtener_valores_por_fecha(
        request.fecha_inicio,
        request.fecha_fin
    )

# ---------- Endpoints Locación Actual ----------

@appValoresAgua.get("/locacion-actual", tags=["Locación Actual"])
def obtener_locacion_actual():
    """
    Obtiene la locación actualmente seleccionada
    """
    return valoresAguaController.obtener_locacion_actual()

@appValoresAgua.put("/locacion-actual", tags=["Locación Actual"])
def cambiar_locacion_actual(request: CambiarLocacionActualRequest):
    """
    Cambia la locación actualmente seleccionada
    """
    return valoresAguaController.cambiar_locacion_actual(request.id_locacion)

@appValoresAgua.get("/locacion-actual/verificar", tags=["Locación Actual"])
def verificar_locacion_actual():
    """
    Verifica si hay una locación actual configurada
    """
    return valoresAguaController.verificar_locacion_actual()

@appValoresAgua.get("/valores-agua/actual", tags=["Valores Agua"])
def obtener_valores_locacion_actual():
    """
    Obtiene todos los valores de agua de la locación actualmente seleccionada
    """
    return valoresAguaController.obtener_valores_locacion_actual()

# ---------- Endpoints Monitoreo ----------

@appValoresAgua.get("/monitoreo/estado", tags=["Monitoreo"])
def obtener_estado_monitoreo():
    """
    Obtiene el estado actual del monitoreo (activado/desactivado)
    """
    return valoresAguaController.obtener_estado_monitoreo()

@appValoresAgua.put("/monitoreo/estado", tags=["Monitoreo"])
def cambiar_estado_monitoreo(request: CambiarEstadoMonitoreoRequest):
    """
    Cambia el estado del monitoreo (activar/desactivar)
    """
    return valoresAguaController.cambiar_estado_monitoreo(request.activado)

@appValoresAgua.put("/monitoreo/activar", tags=["Monitoreo"])
def activar_monitoreo():
    """
    Activa el monitoreo de la locación actual
    """
    return valoresAguaController.activar_monitoreo()

@appValoresAgua.put("/monitoreo/desactivar", tags=["Monitoreo"])
def desactivar_monitoreo():
    """
    Desactiva el monitoreo de la locación actual
    """
    return valoresAguaController.desactivar_monitoreo()