# Proyecto Django

Aplicación web estilo blog desarrollada en **Django**. Incluye: admin, perfiles, registro/login/logout, páginas con CRUD, mensajería entre usuarios, herencia de templates, manejo de imágenes y texto enriquecido (CKEditor).

## Requisitos
- Python 3.11+ (probado en Windows 11 con 3.13)
- Git
- (Opcional) VS Code

## Instalación rápida (Windows 11)
```powershell
git clone <URL_DE_TU_REPO>
cd Proyecto_django
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Rutas principales

- **Home**: `/`
- **About**: `/about/`

**Pages**
- Listado: `/pages/`
- Detalle: `/pages/<id>/`
- Crear (login requerido): `/pages/create/`
- Editar (login requerido): `/pages/<id>/edit/`
- Borrar (login requerido): `/pages/<id>/delete/`

**Accounts**
- Signup: `/accounts/signup/`
- Login: `/accounts/login/`
- Logout (POST): `/accounts/logout/`
- Perfil: `/accounts/profile/`
- Editar perfil: `/accounts/profile/edit/`
- Cambiar contraseña: `/accounts/password/change/`

**Mensajes**
- Inbox: `/messages/`
- Nuevo mensaje: `/messages/compose/`
- Detalle: `/messages/<id>/`
