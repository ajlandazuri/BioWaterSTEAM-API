from datetime import datetime, date
from conect.conexion_app import get_connection, put_connection

def convertir_a_dict(cursor, rows):
    columnas = [col[0] for col in cursor.description]
    resultado = []
    for row in rows:
        row_dict = {}
        for col, val in zip(columnas, row):
            # Manejar tanto datetime como date
            if isinstance(val, (datetime, date)):
                row_dict[col] = val.isoformat()
            else:
                row_dict[col] = val
        resultado.append(row_dict)
    return resultado

# ---------- LOCACIONES ----------

def obtener_locaciones():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM locaciones ORDER BY fecha_creacion DESC")
        rows = cursor.fetchall()
        return convertir_a_dict(cursor, rows)
    except Exception as e:
        print(f"Error al obtener locaciones: {e}")
        return []
    finally:
        cursor.close()
        put_connection(conn)

def obtener_locacion_por_id(locacion_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM locaciones WHERE id_locacion = %s", (locacion_id,))
        row = cursor.fetchone()
        if row:
            return convertir_a_dict(cursor, [row])[0]
        else:
            return None
    except Exception as e:
        print(f"Error al obtener locación por ID: {e}")
        return None
    finally:
        cursor.close()
        put_connection(conn)

def crear_locacion(nombre_lugar):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO locaciones (nombre_lugar) VALUES (%s) RETURNING id_locacion",
            (nombre_lugar,)
        )
        locacion_id = cursor.fetchone()[0]
        conn.commit()
        return locacion_id
    except Exception as e:
        print(f"Error al crear locación: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()
        put_connection(conn)

def actualizar_locacion(locacion_id, nombre_lugar):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE locaciones SET nombre_lugar = %s WHERE id_locacion = %s",
            (nombre_lugar, locacion_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar locación: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)

def eliminar_locacion(locacion_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM locaciones WHERE id_locacion = %s", (locacion_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar locación: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)

# ---------- VALORES AGUA ----------

def obtener_valores_agua():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT v.id_valor, v.ph, v.solidos_disueltos, v.temperatura, 
                   v.fecha_medicion, v.locacion_id, l.nombre_lugar
            FROM valores_agua v
            LEFT JOIN locaciones l ON v.locacion_id = l.id_locacion
            ORDER BY v.fecha_medicion DESC
            """
        )
        rows = cursor.fetchall()
        return convertir_a_dict(cursor, rows)
    except Exception as e:
        print(f"Error al obtener valores de agua: {e}")
        return []
    finally:
        cursor.close()
        put_connection(conn)

def obtener_valor_agua_por_id(valor_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT v.id_valor, v.ph, v.solidos_disueltos, v.temperatura, 
                   v.fecha_medicion, v.locacion_id, l.nombre_lugar
            FROM valores_agua v
            LEFT JOIN locaciones l ON v.locacion_id = l.id_locacion
            WHERE v.id_valor = %s
            """,
            (valor_id,)
        )
        row = cursor.fetchone()
        if row:
            return convertir_a_dict(cursor, [row])[0]
        else:
            return None
    except Exception as e:
        print(f"Error al obtener valor de agua por ID: {e}")
        return None
    finally:
        cursor.close()
        put_connection(conn)

def crear_valor_agua(ph, solidos_disueltos, temperatura, locacion_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO valores_agua (ph, solidos_disueltos, temperatura, locacion_id) VALUES (%s, %s, %s, %s) RETURNING id_valor",
            (ph, solidos_disueltos, temperatura, locacion_id)
        )
        valor_id = cursor.fetchone()[0]
        conn.commit()
        return valor_id
    except Exception as e:
        print(f"Error al crear valor de agua: {e}")
        conn.rollback()
        return None
    finally:
        cursor.close()
        put_connection(conn)

def actualizar_valor_agua(valor_id, ph, solidos_disueltos, temperatura, locacion_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE valores_agua SET ph = %s, solidos_disueltos = %s, temperatura = %s, locacion_id = %s WHERE id_valor = %s",
            (ph, solidos_disueltos, temperatura, locacion_id, valor_id)
        )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al actualizar valor de agua: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)

def eliminar_valor_agua(valor_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM valores_agua WHERE id_valor = %s", (valor_id,))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al eliminar valor de agua: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)

def obtener_valores_por_locacion(locacion_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT v.id_valor, v.ph, v.solidos_disueltos, v.temperatura, 
                   v.fecha_medicion, v.locacion_id, l.nombre_lugar
            FROM valores_agua v
            LEFT JOIN locaciones l ON v.locacion_id = l.id_locacion
            WHERE v.locacion_id = %s
            ORDER BY v.fecha_medicion DESC
            """,
            (locacion_id,)
        )
        rows = cursor.fetchall()
        return convertir_a_dict(cursor, rows)
    except Exception as e:
        print(f"Error al obtener valores por locación: {e}")
        return []
    finally:
        cursor.close()
        put_connection(conn)

def obtener_valores_por_fecha(fecha_inicio, fecha_fin):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT v.id_valor, v.ph, v.solidos_disueltos, v.temperatura, 
                   v.fecha_medicion, v.locacion_id, l.nombre_lugar
            FROM valores_agua v
            LEFT JOIN locaciones l ON v.locacion_id = l.id_locacion
            WHERE v.fecha_medicion BETWEEN %s AND %s
            ORDER BY v.fecha_medicion DESC
            """,
            (fecha_inicio, fecha_fin)
        )
        rows = cursor.fetchall()
        return convertir_a_dict(cursor, rows)
    except Exception as e:
        print(f"Error al obtener valores por fecha: {e}")
        return []
    finally:
        cursor.close()
        put_connection(conn)

# ---------- LOCACIÓN ACTUAL ----------

def obtener_locacion_actual():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            """
            SELECT l.id_locacion, l.nombre_lugar, l.fecha_creacion, a.monitoreo_activado
            FROM locacion_actual a
            JOIN locaciones l ON a.id_locacion = l.id_locacion
            """
        )
        row = cursor.fetchone()
        if row:
            return convertir_a_dict(cursor, [row])[0]
        else:
            return None
    except Exception as e:
        print(f"Error al obtener locación actual: {e}")
        return None
    finally:
        cursor.close()
        put_connection(conn)

def cambiar_locacion_actual(nueva_locacion_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Verificar si existe una fila en locacion_actual
        cursor.execute("SELECT id FROM locacion_actual WHERE id = 1")
        row = cursor.fetchone()
        
        if row:
            # Actualizar la locación existente (mantener el estado actual del monitoreo)
            cursor.execute(
                "UPDATE locacion_actual SET id_locacion = %s WHERE id = 1",
                (nueva_locacion_id,)
            )
        else:
            # Insertar la primera locación con monitoreo activado por defecto
            cursor.execute(
                "INSERT INTO locacion_actual (id, id_locacion, monitoreo_activado) VALUES (1, %s, TRUE)",
                (nueva_locacion_id,)
            )
        
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al cambiar locación actual: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)

def cambiar_estado_monitoreo(activado: bool):
    """
    Cambia solo el estado del monitoreo sin cambiar la locación
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE locacion_actual SET monitoreo_activado = %s WHERE id = 1",
            (activado,)
        )
        
        # Verificar si se actualizó alguna fila
        if cursor.rowcount == 0:
            # No hay ninguna locación configurada
            return False
            
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al cambiar estado de monitoreo: {e}")
        conn.rollback()
        return False
    finally:
        cursor.close()
        put_connection(conn)

def obtener_estado_monitoreo():
    """
    Obtiene solo el estado del monitoreo
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT monitoreo_activado FROM locacion_actual WHERE id = 1")
        row = cursor.fetchone()
        if row:
            return row[0]
        else:
            return None
    except Exception as e:
        print(f"Error al obtener estado de monitoreo: {e}")
        return None
    finally:
        cursor.close()
        put_connection(conn)