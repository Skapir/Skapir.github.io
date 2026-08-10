from django.shortcuts import render

from . import data


def index(request, lang="es"):
    t = data.TEXTOS[lang]
    return render(
        request,
        "web/index.html",
        {
            "perfil": data.PERFIL,
            "t": t,
            "ui": t["ui"],
            "lang": lang,
            # URL de la version en el otro idioma (para el selector ES/EN)
            "url_es": "/",
            "url_en": "/en/",
        },
    )
