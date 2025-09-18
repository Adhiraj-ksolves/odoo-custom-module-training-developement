{
    'name': 'School Management',
    'version': '18.0.1.0.0',
    'summary': 'Manages students and teachers in school',
    'description': 'Provides all-in-one solution for school management',
    'author': 'Adhiraj Ojha',
    'category': 'Education',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/security_group.xml',
        'security/ir.model.access.csv',
        'security/security_access_data.xml',
        'Data/sequence_generator.xml',
        'views/student_view.xml',
        'views/teacher_view.xml',
        'views/class_view.xml',
        'views/fees_view.xml',
        'views/menu_view.xml'
    ],
    'installable': True,
    'application': True,
}
