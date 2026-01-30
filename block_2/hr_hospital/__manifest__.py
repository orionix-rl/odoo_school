{
    'name': 'HR Hospital',
    'version': '19.0.1.0.4',
    'author': 'Oleksii Popov',
    'category': 'Customizations',
    'license': 'OPL-1',

    'depends': [
        'base'
    ],

    'data': [
        'data/hr_hospital_disease.xml',
        'security/ir.model.access.csv',
        'views/hr_hospital_menu.xml',
        'views/hr_hospital_visit_views.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_disease_views.xml',
    ],

    'demo': [
        'demo/hr_hospital_doctor.xml',
        'demo/hr.hospital.patient.csv',
    ],

    'installable': True,
    'auto_install': False,

    'images': ['static/description/icon.png'],
}
