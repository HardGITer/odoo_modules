{
    'name': "Construction Company Management",

    'author': "Matvey",

    'depends': ['base', 'product'],

    'application': True,

    'data': [
        'security/construction_security.xml',
        'security/ir.model.access.csv',
        'views/construction_menu.xml',
        'views/product_view.xml',
        'views/company_view.xml',
        'data/company_data.xml',
    ],

    'demo': [
    ]
}