from django.shortcuts import render

from . import data


def index(request):
    return render(
        request,
        "web/index.html",
        {
            "perfil": data.PERFIL,
            "sobre_mi": data.SOBRE_MI,
            "sobre_mi_2": data.SOBRE_MI_2,
            "trabajo": data.TRABAJO,
            "educacion": data.EDUCACION,
            "proyectos": data.PROYECTOS,
        },
    )
