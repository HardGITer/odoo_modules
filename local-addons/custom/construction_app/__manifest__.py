{
    'name': "Construction Company Management",

    'author': "Matvey",

    'depends': ['base'],

    'application': True,

    'data': [
        'security/construction_security.xml',
        'security/ir.model.access.csv',
        'views/construction_menu.xml',
        'views/product_view.xml',
        'views/company_view.xml',
    ],

    'demo': [
        'data/company_demo.xml'
    ]
}