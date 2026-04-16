from fastapi.responses import JSONResponse
from model import valoresAguaModel
from datetime import date

# ------- LOCACIONES --------

def obtener_locaciones():
    try:
        locaciones = valoresAguaModel.obtener_locaciones()
        if locaciones:
            return JSONResponse(status_code=200, content={"status": 200, "locaciones": locaciones})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron locaciones"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def obtener_locacion_por_id(locacion_id: int):
    try:
        locacion = valoresAguaModel.obtener_locacion_por_id(locacion_id)
        if locacion:
            return JSONResponse(status_code=200, content={"status": 200, "locacion": locacion})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Locación no encontrada"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def crear_locacion(nombre_lugar: str):
    try:
        locacion_id = valoresAguaModel.crear_locacion(nombre_lugar)
        if locacion_id:
            return JSONResponse(status_code=201, content={"status": 201, "message": "Locación creada exitosamente", "id": locacion_id})
        else:
            return JSONResponse(status_code=400, content={"status": 400, "message": "No se pudo crear la locación"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def actualizar_locacion(locacion_id: int, nombre_lugar: str):
    try:
        actualizado = valoresAguaModel.actualizar_locacion(locacion_id, nombre_lugar)
        if actualizado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Locación actualizada correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Locación no encontrada o no actualizada"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def eliminar_locacion(locacion_id: int):
    try:
        eliminado = valoresAguaModel.eliminar_locacion(locacion_id)
        if eliminado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Locación eliminada correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Locación no encontrada o no eliminada"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

# ------- VALORES AGUA --------

def obtener_valores_agua():
    try:
        valores = valoresAguaModel.obtener_valores_agua()
        if valores:
            return JSONResponse(status_code=200, content={"status": 200, "valores_agua": valores})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron valores de agua"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def obtener_valor_agua_por_id(valor_id: int):
    try:
        valor = valoresAguaModel.obtener_valor_agua_por_id(valor_id)
        if valor:
            return JSONResponse(status_code=200, content={"status": 200, "valor_agua": valor})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Valor de agua no encontrado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def crear_valor_agua(ph: str, solidos_disueltos: str, temperatura: str, locacion_id: int):
    try:
        valor_id = valoresAguaModel.crear_valor_agua(ph, solidos_disueltos, temperatura, locacion_id)
        if valor_id:
            return JSONResponse(status_code=201, content={"status": 201, "message": "Valor de agua creado exitosamente", "id": valor_id})
        else:
            return JSONResponse(status_code=400, content={"status": 400, "message": "No se pudo crear el valor de agua"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def actualizar_valor_agua(valor_id: int, ph: str, solidos_disueltos: str, temperatura: str, locacion_id: int):
    try:
        actualizado = valoresAguaModel.actualizar_valor_agua(valor_id, ph, solidos_disueltos, temperatura, locacion_id)
        if actualizado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Valor de agua actualizado correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Valor de agua no encontrado o no actualizado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def eliminar_valor_agua(valor_id: int):
    try:
        eliminado = valoresAguaModel.eliminar_valor_agua(valor_id)
        if eliminado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Valor de agua eliminado correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "Valor de agua no encontrado o no eliminado"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def obtener_valores_por_locacion(locacion_id: int):
    try:
        valores = valoresAguaModel.obtener_valores_por_locacion(locacion_id)
        if valores:
            return JSONResponse(status_code=200, content={"status": 200, "valores_agua": valores})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron valores para esta locación"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def obtener_valores_por_fecha(fecha_inicio: date, fecha_fin: date):
    try:
        valores = valoresAguaModel.obtener_valores_por_fecha(fecha_inicio, fecha_fin)
        if valores:
            return JSONResponse(status_code=200, content={"status": 200, "valores_agua": valores})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron valores en el rango de fechas"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

# ------- LOCACIÓN ACTUAL --------

def obtener_locacion_actual():
    try:
        locacion = valoresAguaModel.obtener_locacion_actual()
        if locacion:
            return JSONResponse(status_code=200, content={"status": 200, "locacion_actual": locacion})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No hay locación actual configurada"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def cambiar_locacion_actual(nueva_locacion_id: int):
    try:
        # Verificar que la locación existe
        locacion_existe = valoresAguaModel.obtener_locacion_por_id(nueva_locacion_id)
        if not locacion_existe:
            return JSONResponse(status_code=404, content={"status": 404, "message": "La locación especificada no existe"})
        
        cambiado = valoresAguaModel.cambiar_locacion_actual(nueva_locacion_id)
        if cambiado:
            return JSONResponse(status_code=200, content={"status": 200, "message": "Locación actual cambiada correctamente"})
        else:
            return JSONResponse(status_code=400, content={"status": 400, "message": "No se pudo cambiar la locación actual"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def obtener_valores_locacion_actual():
    try:
        valores = valoresAguaModel.obtener_valores_locacion_actual()
        if valores:
            return JSONResponse(status_code=200, content={"status": 200, "valores_agua": valores})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No se encontraron valores para la locación actual"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def verificar_locacion_actual():
    try:
        existe = valoresAguaModel.verificar_locacion_actual_existe()
        return JSONResponse(status_code=200, content={"status": 200, "locacion_configurada": existe})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

# ------- MONITOREO --------

def obtener_estado_monitoreo():
    try:
        estado = valoresAguaModel.obtener_estado_monitoreo()
        if estado is not None:
            return JSONResponse(status_code=200, content={"status": 200, "monitoreo_activado": estado})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No hay locación actual configurada"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def cambiar_estado_monitoreo(activado: bool):
    try:
        cambiado = valoresAguaModel.cambiar_estado_monitoreo(activado)
        if cambiado:
            estado_texto = "activado" if activado else "desactivado"
            return JSONResponse(status_code=200, content={"status": 200, "message": f"Monitoreo {estado_texto} correctamente"})
        else:
            return JSONResponse(status_code=404, content={"status": 404, "message": "No hay locación actual configurada para cambiar el estado del monitoreo"})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": 500, "message": f"Error interno: {str(e)}"})

def activar_monitoreo():
    return cambiar_estado_monitoreo(True)

def desactivar_monitoreo():
    return cambiar_estado_monitoreo(False)