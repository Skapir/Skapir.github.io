# ============================================================
# DATOS DEL PORTAFOLIO - Sergio Kevin Perez Nateros
# Edita este archivo para actualizar tu web (no toques el HTML).
# ============================================================

PERFIL = {
    "nombre": "Sergio",
    "apellido": "Perez.",
    "titulo": "Ingeniero de Sistemas · Desarrollador Backend",
    "subtitulo": "Python · FastAPI · Django · Automatización de Procesos",
    "email": "sperezn.dev@gmail.com",
    "cv_url": "web/cv/CV_Sergio_Perez_ES.pdf",  # ruta dentro de static/
    "cv_url_en": "web/cv/CV_Sergio_Perez_EN.pdf",
    "github": "https://github.com/Skapir",
    "linkedin": "https://www.linkedin.com/in/sergio-perez-nateros",
}

SOBRE_MI = (
    "Ingeniero de Sistemas e Informática con más de 13 años en el sector salud "
    "público peruano, los últimos cuatro dedicados al desarrollo backend y la "
    "puesta en producción de sistemas de automatización en un entorno hospitalario "
    "de alta demanda. Especializado en integrar sistemas legacy sin API pública "
    "mediante ingeniería inversa de tráfico HTTP, y en convertir procesos "
    "burocráticos manuales en flujos automatizados."
)

SOBRE_MI_2 = (
    "Stack principal: Python (FastAPI, Django), PostgreSQL, HTMX y Playwright. "
    "Experiencia end-to-end: levantamiento de requerimientos, arquitectura, "
    "desarrollo, despliegue y soporte a usuarios finales. Disponible para "
    "trabajo remoto (GMT-5)."
)

# --------- TRAYECTORIA ---------
TRABAJO = [
    {
        "titulo": "Desarrollador de Software Independiente",
        "texto": "Consultoría y desarrollo a medida — sector salud y retail (remoto): POS de farmacia con trazabilidad FEFO, middleware HL7 para dispensador AMIS-850, e-commerce fotográfico.",
        "fecha": "2024 — Actualidad",
    },
    {
        "titulo": "Hospital I Tingo María — EsSalud · Desarrollador Backend / Analista de Sistemas",
        "texto": "Área de Referencias: automatización end-to-end del flujo de referencias médicas, integración con REFCON/SGSS y ESSI vía ingeniería inversa HTTP, reportes ejecutivos automatizados con Python.",
        "fecha": "2021 — Actualidad",
    },
    {
        "titulo": "Hospital I Tingo María — EsSalud · Digitador Asistencial",
        "texto": "Rotación por áreas asistenciales y administrativas: registro y validación de información clínica en ESSI, REFCON y SGSS. Conocimiento end-to-end de los flujos hospitalarios.",
        "fecha": "Abr 2013 — 2021",
    },
]

EDUCACION = [
    {
        "titulo": "Universidad Tecnológica del Perú (UTP)",
        "texto": "Título Profesional de Ingeniero de Sistemas e Informática (2026) · Bachiller (2021)",
        "fecha": "2015 — 2021",
    },
    {
        "titulo": "Platzi",
        "texto": "Ruta de Desarrollo Backend con Python · Scrum Profesional · Django REST Framework · Frontend Developer",
        "fecha": "2022 — 2025",
    },
    {
        "titulo": "Edutin Academy",
        "texto": "Desarrollador Python (220 h) · Bases de Datos Relacionales (180 h) · Ciberseguridad (180 h) · GNU/Linux (120 h)",
        "fecha": "2025",
    },
    {
        "titulo": "Data Science Analysis",
        "texto": "Análisis de Datos con Python y Power BI · Python con SQL Server y MySQL para Big Data · IA y Machine Learning con Python",
        "fecha": "2025",
    },
]

# --------- PROYECTOS ---------
# "estado" se muestra como etiqueta. "url_github"/"url_web": "" = no mostrar icono.
PROYECTOS = [
    {
        "titulo": "Referencias EsSalud → MINSA",
        "descripcion": (
            "Sistema web en producción que permite a los médicos generar "
            "referencias institucionales hacia un centro externo de tomografía "
            "y mamografía (flujo no soportado por ESSI), con citas, aprobaciones "
            "y notificaciones automáticas por WhatsApp."
        ),
        "tecnologias": ["FastAPI", "SQLAlchemy", "HTMX", "ReportLab", "WhatsApp"],
        "estado": "En producción",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "CitaExpress",
        "descripcion": (
            "Middleware que extrae referencias en estado CITADO desde REFCON, "
            "genera PDFs sellados y los entrega a pacientes por enlace tokenizado "
            "de WhatsApp, eliminando viajes innecesarios al hospital."
        ),
        "tecnologias": ["FastAPI", "HTMX", "ReportLab", "httpx", "WhatsApp"],
        "estado": "En producción",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "PediaClinic",
        "descripcion": (
            "Sistema de gestión para clínica pediátrica: dashboards por rol, "
            "login con Google OAuth2, pago por Yape con conciliación automática "
            "por IMAP, reservas con Celery Beat y bot de Telegram."
        ),
        "tecnologias": ["Django", "PostgreSQL", "Celery", "HTMX", "Tailwind"],
        "estado": "Completo",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "Robot de Programación SGSS",
        "descripcion": (
            "Robot con Playwright que carga automáticamente el rol mensual de "
            "horarios del personal al sistema SGSS de EsSalud desde matrices "
            "Excel, validando la meta de 150 horas por trabajador."
        ),
        "tecnologias": ["Python", "Playwright", "openpyxl"],
        "estado": "En producción",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "FotoStudio Pro",
        "descripcion": (
            "E-commerce para estudio fotográfico profesional: catálogo con "
            "marca de agua, carrito de compras, pago con Yape y entrega "
            "digital de las fotos en alta resolución."
        ),
        "tecnologias": ["FastAPI", "Tailwind", "Yape"],
        "estado": "En producción",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "Punto de Venta — Farmacia",
        "descripcion": (
            "POS e inventario para farmacia con registro DIGEMID: caja, "
            "fidelización de clientes y control de lotes con trazabilidad "
            "FEFO por fecha de vencimiento."
        ),
        "tecnologias": ["Python", "PostgreSQL"],
        "estado": "Consultoría",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "Middleware HL7 — AMIS-850",
        "descripcion": (
            "Capa middleware que permite a una clínica con infraestructura HL7 "
            "operar un dispensador de medicamentos AMIS-850 que solo expone "
            "SDK propietario, sin soporte HL7 nativo."
        ),
        "tecnologias": ["Python", "HL7", "SDK"],
        "estado": "Consultoría",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "Sistema de Pasajes",
        "descripcion": (
            "Aplicación Django para el registro de pasajes terrestres con "
            "código QR, notificación por WhatsApp y vista pública de canje."
        ),
        "tecnologias": ["Django", "QR", "WhatsApp"],
        "estado": "Fase 1 completa",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "Sistema de Horarios",
        "descripcion": (
            "Aplicación web para que el personal administrativo gestione los "
            "roles de turnos del hospital desde un tablero de control."
        ),
        "tecnologias": ["FastAPI", "HTMX"],
        "estado": "En uso",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "Reportes SUSALUD",
        "descripcion": (
            "Generador config-driven de tramas de producción asistencial para "
            "18 servicios hospitalarios, con validación automática antes del "
            "envío a SUSALUD."
        ),
        "tecnologias": ["Python", "Pandas", "Excel"],
        "estado": "En producción",
        "url_github": "",
        "url_web": "",
    },
    {
        "titulo": "Facturación Electrónica SUNAT",
        "descripcion": (
            "Modernización de un sistema de facturación electrónica SUNAT "
            "para restaurantes y farmacias."
        ),
        "tecnologias": ["PHP", "Laravel", "SUNAT"],
        "estado": "En desarrollo",
        "url_github": "",
        "url_web": "",
    },
]
