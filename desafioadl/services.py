from .models import Tarea, SubTarea


def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.filter(eliminada=False).prefetch_related("subtareas")
    resultado = []
    for tarea in tareas:
        resultado.append(
            {"id": tarea.id, "descripcion": tarea.descripcion, "subtareas": []}
        )
        for subtarea in tarea.subtareas.filter(eliminada=False):
            resultado[-1]["subtareas"].append(
                {"id": subtarea.id, "descripcion": subtarea.descripcion}
            )
    return resultado


def crear_nueva_tarea(descripcion):
    tarea = Tarea.objects.create(descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()


def crear_sub_tarea(tarea_id, descripcion):
    tarea = Tarea.objects.get(id=tarea_id, eliminada=False)
    SubTarea.objects.create(tarea=tarea, descripcion=descripcion)
    return recupera_tareas_y_sub_tareas()


def elimina_tarea(tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    tarea.eliminada = True
    tarea.save()
    return recupera_tareas_y_sub_tareas()


def elimina_sub_tarea(sub_tarea_id):
    subtarea = SubTarea.objects.get(id=sub_tarea_id)
    subtarea.eliminada = True
    subtarea.save()
    return recupera_tareas_y_sub_tareas()


def imprimir_en_pantalla(tareas_y_subtareas):
    for tarea in tareas_y_subtareas:
        print(f"[{tarea['id']}] {tarea['descripcion']}")
        for subtarea in tarea["subtareas"]:
            print(f".... [{subtarea['id']}] {subtarea['descripcion']}")
