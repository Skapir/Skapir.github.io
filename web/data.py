# ============================================================
# DATOS DEL PORTAFOLIO - Sergio Kevin Perez Nateros
# Bilingue: TEXTOS['es'] y TEXTOS['en'].
# Edita este archivo para actualizar tu web (no toques el HTML).
# ============================================================

# Datos compartidos entre idiomas
PERFIL = {
    "nombre": "Sergio",
    "apellido": "Perez.",
    "email": "sperezn.dev@gmail.com",
    "github": "https://github.com/Skapir",
    "linkedin": "https://www.linkedin.com/in/sergio-perez-nateros",
    "whatsapp": "51994400662",
    "whatsapp_display": "+51 994 400 662",
    "cv_es": "web/cv/CV_Sergio_Perez_ES.pdf",
    "cv_en": "web/cv/CV_Sergio_Perez_EN.pdf",
}

TEXTOS = {
    # ==================== ESPAÑOL ====================
    "es": {
        "titulo": "Ingeniero de Sistemas · Desarrollador Backend",
        "subtitulo": "Python · FastAPI · Django · Automatización de Procesos",
        "cv_principal": "web/cv/CV_Sergio_Perez_ES.pdf",
        "wa_msg": "Hola%20Sergio,%20vi%20tu%20portafolio%20web",
        "sobre_mi": (
            "Ingeniero de Sistemas e Informática con más de 13 años en el sector salud "
            "público peruano, los últimos cuatro dedicados al desarrollo backend y la "
            "puesta en producción de sistemas de automatización en un entorno hospitalario "
            "de alta demanda. Especializado en integrar sistemas legacy sin API pública "
            "mediante ingeniería inversa de tráfico HTTP, y en convertir procesos "
            "burocráticos manuales en flujos automatizados."
        ),
        "sobre_mi_2": (
            "Stack principal: Python (FastAPI, Django), PostgreSQL, HTMX y Playwright. "
            "Experiencia end-to-end: levantamiento de requerimientos, arquitectura, "
            "desarrollo, despliegue y soporte a usuarios finales. Disponible para "
            "trabajo remoto (GMT-5)."
        ),
        "trabajo": [
            {
                "titulo": "Desarrollador de Software Independiente",
                "texto": "Consultoría y desarrollo a medida - sector salud y retail (remoto): POS de farmacia con trazabilidad FEFO, middleware HL7 para dispensador AMIS-850, e-commerce fotográfico.",
                "fecha": "2024 - Actualidad",
            },
            {
                "titulo": "EsSalud, Hospital I Tingo María · Desarrollador Backend / Analista de Sistemas",
                "texto": "Área de Referencias: automatización end-to-end del flujo de referencias médicas, integración con REFCON/SGSS y ESSI vía ingeniería inversa HTTP, reportes ejecutivos automatizados con Python.",
                "fecha": "2021 - Actualidad",
            },
            {
                "titulo": "EsSalud, Hospital I Tingo María · Digitador Asistencial",
                "texto": "Rotación por áreas asistenciales y administrativas: registro y validación de información clínica en ESSI, REFCON y SGSS. Conocimiento end-to-end de los flujos hospitalarios.",
                "fecha": "Abr 2013 - 2021",
            },
        ],
        "educacion": [
            {
                "titulo": "Universidad Tecnológica del Perú (UTP)",
                "texto": "Título Profesional de Ingeniero de Sistemas e Informática (2026) · Bachiller (2021)",
                "fecha": "2015 - 2021",
            },
            {
                "titulo": "Platzi",
                "texto": "Ruta de Desarrollo Backend con Python · Scrum Profesional · Django REST Framework · Frontend Developer",
                "fecha": "2022 - 2025",
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
        ],
        "proyectos": [
            {
                "titulo": "Referencias EsSalud → MINSA",
                "descripcion": "Sistema web en producción que permite a los médicos generar referencias institucionales hacia un centro externo de tomografía y mamografía (flujo no soportado por ESSI), con citas, aprobaciones y notificaciones automáticas por WhatsApp.",
                "tecnologias": ["FastAPI", "SQLAlchemy", "HTMX", "ReportLab", "WhatsApp"],
                "estado": "En producción",
            },
            {
                "titulo": "CitaExpress",
                "descripcion": "Middleware que extrae referencias en estado CITADO desde REFCON, genera PDFs sellados y los entrega a pacientes por enlace tokenizado de WhatsApp, eliminando viajes innecesarios al hospital.",
                "tecnologias": ["FastAPI", "HTMX", "ReportLab", "httpx", "WhatsApp"],
                "estado": "En producción",
            },
            {
                "titulo": "PediaClinic",
                "descripcion": "Sistema de gestión para clínica pediátrica: dashboards por rol, login con Google OAuth2, pago por Yape con conciliación automática por IMAP, reservas con Celery Beat y bot de Telegram.",
                "tecnologias": ["Django", "PostgreSQL", "Celery", "HTMX", "Tailwind"],
                "estado": "Completo",
            },
            {
                "titulo": "Robot de Programación SGSS",
                "descripcion": "Robot con Playwright que carga automáticamente el rol mensual de horarios del personal al sistema SGSS de EsSalud desde matrices Excel, validando la meta de 150 horas por trabajador.",
                "tecnologias": ["Python", "Playwright", "openpyxl"],
                "estado": "En producción",
            },
            {
                "titulo": "FotoStudio Pro",
                "descripcion": "E-commerce para estudio fotográfico profesional: catálogo con marca de agua, carrito de compras, pago con Yape y entrega digital de las fotos en alta resolución.",
                "tecnologias": ["FastAPI", "Tailwind", "Yape"],
                "estado": "En producción",
            },
            {
                "titulo": "Punto de Venta - Farmacia",
                "descripcion": "POS e inventario para farmacia con registro DIGEMID: caja, fidelización de clientes y control de lotes con trazabilidad FEFO por fecha de vencimiento.",
                "tecnologias": ["Python", "PostgreSQL"],
                "estado": "Consultoría",
            },
            {
                "titulo": "Middleware HL7 - AMIS-850",
                "descripcion": "Capa middleware que permite a una clínica con infraestructura HL7 operar un dispensador de medicamentos AMIS-850 que solo expone SDK propietario, sin soporte HL7 nativo.",
                "tecnologias": ["Python", "HL7", "SDK"],
                "estado": "Consultoría",
            },
            {
                "titulo": "Sistema de Pasajes",
                "descripcion": "Aplicación Django para el registro de pasajes terrestres con código QR, notificación por WhatsApp y vista pública de canje.",
                "tecnologias": ["Django", "QR", "WhatsApp"],
                "estado": "Fase 1 completa",
            },
            {
                "titulo": "Sistema de Horarios",
                "descripcion": "Aplicación web para que el personal administrativo gestione los roles de turnos del hospital desde un tablero de control.",
                "tecnologias": ["FastAPI", "HTMX"],
                "estado": "En uso",
            },
            {
                "titulo": "Reportes SUSALUD",
                "descripcion": "Generador config-driven de tramas de producción asistencial para 18 servicios hospitalarios, con validación automática antes del envío a SUSALUD.",
                "tecnologias": ["Python", "Pandas", "Excel"],
                "estado": "En producción",
            },
            {
                "titulo": "Facturación Electrónica SUNAT",
                "descripcion": "Modernización de un sistema de facturación electrónica SUNAT para restaurantes y farmacias.",
                "tecnologias": ["PHP", "Laravel", "SUNAT"],
                "estado": "En desarrollo",
            },
        ],
        "ui": {
            "nav_sobre": "Sobre mí",
            "nav_proyectos": "Mis proyectos",
            "nav_contacto": "Contáctame",
            "hero_hola": "Hola 👋🏼, soy",
            "btn_contacto": "Contáctame",
            "btn_cv": "Descargar CV",
            "sobre_title": "Sobre mí",
            "sobre_sub": "Quién soy",
            "sobre_dev": "Software Developer,",
            "ver_proyectos_pre": "Puedes ver algunos de mis proyectos en la sección de",
            "ver_proyectos_link": "proyectos.",
            "contacto_pre": "Si tienes alguna pregunta o algún comentario no dudes en",
            "contacto_link": "contactarme.",
            "tray_title": "Mi trayectoria.",
            "tray_sub": "Educación y trabajo",
            "tab_trabajo": "Trabajo",
            "tab_educacion": "Educación",
            "proy_title": "Mis proyectos",
            "proy_sub": "Sistemas reales, en producción",
            "cont_title": "Contáctame",
            "cont_sub": "¿Hablamos?",
            "escribeme": "Escríbeme a",
            "cv_es_label": "CV en Español (PDF)",
            "cv_en_label": "CV in English (PDF)",
            "gracias": "Gracias por visitar mi sitio web! 😊",
            "footer_otros": "O también me puedes contactar a través de:",
            "hecho": "Hecho con ❤️ y Django por Sergio Perez.",
        },
    },
    # ==================== ENGLISH ====================
    "en": {
        "titulo": "Systems Engineer · Backend Developer",
        "subtitulo": "Python · FastAPI · Django · Process Automation",
        "cv_principal": "web/cv/CV_Sergio_Perez_EN.pdf",
        "wa_msg": "Hi%20Sergio,%20I%20saw%20your%20portfolio",
        "sobre_mi": (
            "Systems and Computer Engineer with 13+ years in Peru's public healthcare "
            "sector, the last four building and shipping production automation systems "
            "inside a high-volume hospital. Specialized in integrating closed legacy "
            "systems with no public API by reverse-engineering their HTTP traffic, and "
            "in replacing manual bureaucratic processes with automated pipelines."
        ),
        "sobre_mi_2": (
            "Core stack: Python (FastAPI, Django), PostgreSQL, HTMX and Playwright. "
            "End-to-end experience: requirements, architecture, implementation, "
            "deployment and end-user support. Available for remote work (GMT-5, "
            "full-day overlap with US time zones)."
        ),
        "trabajo": [
            {
                "titulo": "Independent Software Developer",
                "texto": "Custom software consulting - healthcare and retail (remote): pharmacy POS with FEFO traceability, HL7 middleware for an AMIS-850 dispenser, photography e-commerce.",
                "fecha": "2024 - Present",
            },
            {
                "titulo": "EsSalud, Hospital I Tingo María · Backend Developer / Systems Analyst",
                "texto": "Patient Referrals Unit: end-to-end automation of the medical referral workflow, integration with REFCON/SGSS and ESSI via HTTP reverse-engineering, automated executive reporting with Python.",
                "fecha": "2021 - Present",
            },
            {
                "titulo": "EsSalud, Hospital I Tingo María · Healthcare Data & Operations Assistant",
                "texto": "Multi-department rotation: recording and validating clinical data in ESSI, REFCON and SGSS. End-to-end knowledge of hospital workflows.",
                "fecha": "Apr 2013 - 2021",
            },
        ],
        "educacion": [
            {
                "titulo": "Universidad Tecnológica del Perú (UTP)",
                "texto": "Professional Degree in Systems & Computer Engineering (2026) · Bachelor's Degree (2021)",
                "fecha": "2015 - 2021",
            },
            {
                "titulo": "Platzi",
                "texto": "Backend Development with Python track · Professional Scrum · Django REST Framework · Frontend Developer",
                "fecha": "2022 - 2025",
            },
            {
                "titulo": "Edutin Academy",
                "texto": "Python Developer (220 h) · Relational Databases (180 h) · Cybersecurity (180 h) · GNU/Linux (120 h)",
                "fecha": "2025",
            },
            {
                "titulo": "Data Science Analysis",
                "texto": "Data Analysis with Python & Power BI · Python with SQL Server & MySQL for Big Data · AI & Machine Learning with Python",
                "fecha": "2025",
            },
        ],
        "proyectos": [
            {
                "titulo": "EsSalud → MINSA Referrals",
                "descripcion": "Production web system that lets physicians issue institution-format referrals to an external CT and mammography imaging center (a workflow the official system does not support), with appointments, approvals and automatic WhatsApp notifications.",
                "tecnologias": ["FastAPI", "SQLAlchemy", "HTMX", "ReportLab", "WhatsApp"],
                "estado": "In production",
            },
            {
                "titulo": "CitaExpress",
                "descripcion": "Middleware that scrapes scheduled referrals from REFCON, generates stamped PDFs and delivers them to patients over tokenized WhatsApp links, removing unnecessary trips to the hospital.",
                "tecnologias": ["FastAPI", "HTMX", "ReportLab", "httpx", "WhatsApp"],
                "estado": "In production",
            },
            {
                "titulo": "PediaClinic",
                "descripcion": "Pediatric clinic management platform: role-based dashboards, Google OAuth2 login, mobile-wallet (Yape) payments reconciled automatically over IMAP, reservation expiry with Celery Beat and a Telegram bot.",
                "tecnologias": ["Django", "PostgreSQL", "Celery", "HTMX", "Tailwind"],
                "estado": "Completed",
            },
            {
                "titulo": "SGSS Scheduling Robot",
                "descripcion": "Playwright robot that automatically loads the monthly staff roster into EsSalud's SGSS system from Excel grids, validating the 150-hour monthly target per employee.",
                "tecnologias": ["Python", "Playwright", "openpyxl"],
                "estado": "In production",
            },
            {
                "titulo": "FotoStudio Pro",
                "descripcion": "E-commerce for a professional photography studio: watermarked catalog, shopping cart, mobile-wallet (Yape) payment and digital delivery of high-resolution photos.",
                "tecnologias": ["FastAPI", "Tailwind", "Yape"],
                "estado": "In production",
            },
            {
                "titulo": "Pharmacy Point of Sale",
                "descripcion": "POS and inventory platform for a pharmacy with national drug-registry (DIGEMID) lookup: cash management, customer loyalty and FEFO lot tracking with expiry control.",
                "tecnologias": ["Python", "PostgreSQL"],
                "estado": "Consulting",
            },
            {
                "titulo": "HL7 Middleware - AMIS-850",
                "descripcion": "Middleware layer that allows an HL7-based clinic to operate an AMIS-850 medication dispenser that ships with a proprietary SDK only, with no native HL7 support.",
                "tecnologias": ["Python", "HL7", "SDK"],
                "estado": "Consulting",
            },
            {
                "titulo": "Ticketing System",
                "descripcion": "Django application for registering ground-transport tickets with QR codes, WhatsApp notifications and a public redemption view.",
                "tecnologias": ["Django", "QR", "WhatsApp"],
                "estado": "Phase 1 complete",
            },
            {
                "titulo": "Staff Scheduling System",
                "descripcion": "Web application for hospital administrative staff to manage shift rosters from a control dashboard.",
                "tecnologias": ["FastAPI", "HTMX"],
                "estado": "In use",
            },
            {
                "titulo": "SUSALUD Reports",
                "descripcion": "Config-driven generator of healthcare production data files for 18 hospital services, with automatic validation before submission to the regulator (SUSALUD).",
                "tecnologias": ["Python", "Pandas", "Excel"],
                "estado": "In production",
            },
            {
                "titulo": "SUNAT e-Invoicing",
                "descripcion": "Modernization of a SUNAT electronic invoicing system for restaurants and pharmacies.",
                "tecnologias": ["PHP", "Laravel", "SUNAT"],
                "estado": "In development",
            },
        ],
        "ui": {
            "nav_sobre": "About me",
            "nav_proyectos": "My projects",
            "nav_contacto": "Contact me",
            "hero_hola": "Hi 👋🏼, I'm",
            "btn_contacto": "Contact me",
            "btn_cv": "Download CV",
            "sobre_title": "About me",
            "sobre_sub": "Who I am",
            "sobre_dev": "Software Developer,",
            "ver_proyectos_pre": "You can see some of my work in the",
            "ver_proyectos_link": "projects section.",
            "contacto_pre": "If you have any questions or comments, feel free to",
            "contacto_link": "contact me.",
            "tray_title": "My journey.",
            "tray_sub": "Education and work",
            "tab_trabajo": "Work",
            "tab_educacion": "Education",
            "proy_title": "My projects",
            "proy_sub": "Real systems, in production",
            "cont_title": "Contact me",
            "cont_sub": "Let's talk!",
            "escribeme": "Email me at",
            "cv_es_label": "CV en Español (PDF)",
            "cv_en_label": "CV in English (PDF)",
            "gracias": "Thanks for visiting my website! 😊",
            "footer_otros": "You can also reach me through:",
            "hecho": "Built with ❤️ and Django by Sergio Perez.",
        },
    },
}
