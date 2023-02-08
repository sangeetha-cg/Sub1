# -*- coding: utf-8 -*-
{
    'name': 'Combined General Rental Customer Vehicles',
    'version': '13.0.1.0.0',
    'category': 'Tools',
    'sequence': 100,
    'summary': 'Combined General Rental Customer Vehicles',
    'description': """
                Combined General Rental Customer Vehicles
    """,
    'author': 'Combined General',
    'website': 'www.combinedgeneral.com',
    'depends': ['fleet'],
    'data': [
        'security/ir.model.access.csv',
        'views/rental_customer_driver_view.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
