{
    'name': 'Venta de productos',
    'version': '3.3.1',
    'summary': 'Módulo para vender productos',
    'description': """Módulo para la venta de productos en general""",
    'category': 'Sale',
    'website': 'https://codigobyte2020.github.io/GMax/',
    'depends': ['base'],
    'data': [
            #Archivo de reglas de acceso
            'security/ir.model.access.csv',
            #vistas
            'views/ventas_menus.xml',
            'views/vendedor_views.xml',
            'views/cliente_views.xml',
            'views/producto_views.xml',
            'views/venta_views.xml',
    ],
    'installable': True,
}