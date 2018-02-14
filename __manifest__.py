# -*- coding: utf-8 -*-
{
    'name'     : 'InfoSaône - Module Odoo pour ALTINEA',
    'version'  : '0.1',
    'author'   : 'InfoSaône',
    'category' : 'InfoSaône',


    'description': """
InfoSaône - Module Odoo pour ALTINEA
===================================================
""",
    'maintainer' : 'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'account',
        'account_accountant',
        'document',
],
    'data' : [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/is_export_compta_view.xml',
        'views/sale_view.xml',
        'views/account_analytic_account_view.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

