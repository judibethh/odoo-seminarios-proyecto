{
    'name': 'Seminar Attendance ISI',
    'version': '1.0',
    'summary': 'Gestión de seminarios y asistencia',
    'description': 'Módulo para crear seminarios, inscribir contactos y controlar asistencia.',
    'author': 'Tu Nombre',
    'category': 'Educación',
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/seminar_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}