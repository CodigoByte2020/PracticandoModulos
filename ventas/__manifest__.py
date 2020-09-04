{
    'name': 'Venta de productos',
    'version': '3.3.1',
    'summary': 'Módulo para vender productos',
    'description': """Módulo para la venta de productos en general""",
    'category': 'Sale',
    'website': 'https://codigobyte2020.github.io/GMax/',
    'depends': ['base'],
    'data': [
            #vistas
            'views/ventas_menus.xml',
            'views/vendedor_views.xml',
            'views/cliente_views.xml',
            #Archivo de reglas de acceso
            'security/ir.model.access.csv',
    ],
    'installable': True,
}