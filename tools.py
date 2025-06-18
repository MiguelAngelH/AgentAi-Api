from datetime import datetime

#tool de horario, almacena el horario de atención del local.
def tool_horario():
    return {"apertura": "13:00", "cierre": "15:00"}
# tool de empleados, almacena los empleados y sus roles.
def tool_empleados():
    return {
        "Miguel": "gerente",
        "Claudio": "vendedor",
        "Juan": "tecnico"
    }

# tool de reiniciar router, indica que se debe reiniciar el router para problemas de conexión a Internet.
def tool_reiniciar_router():
    return "Para los problemas de conexión a Internet, se debe indicar que intente reiniciar el router."
#tool de dirección del local, almacena la dirección del local y horario de atención.
def tool_direccion():
    return "La dirección del local es en Palacio La Moneda 717, abierto de 13:00 a 15:00."
