{
    'name': "training_management",

    'summary': "Module de gestion de cours, formationnet e sessions",

    'description': """
Ceci est un module odoo dédié à la gestion des formation et des cours au sein d'une entreprise, il permet l'intégration facile
et l'acquisition rapide des connaissances au sein d'une entreprise.
    """,

    'author': "N'GASAMA Henoc",
    'website': "https://www.infinityfree-henoc.free/sites/trainning-management/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': "N'GASAMA Henoc",
    'version': '0.1',
    "application": True,
    'installable': True,
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        "views/menu/menu-actions.xml",
        "views/menu/menu.xml",
        
        'security/ir.model.access.csv',
        'views/training_course_views.xml',
        'views/training_session_views.xml',
        'views/training_participant_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

