# -*- coding: utf-8 -*-
{
    'name'     : u'InfoSaône - Module Odoo pour ALTINEA',
    'version'  : '0.1',
    'author'   : u'InfoSaône',
    'category' : u'InfoSaône',


    'description': u"""
InfoSaône - Module Odoo pour ALTINEA
===================================================
""",
    'maintainer' : u'InfoSaône',
    'website'    : 'http://www.infosaone.com',
    'depends'    : [
        'base',
        'account',
        'account_accountant',
        'document',
        'professional_templates',
],
    'data' : [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/partner_view.xml',
        'views/crm_lead_views.xml',
        'views/is_export_compta_view.xml',
        'views/sale_view.xml',
        'views/account_invoice_view.xml',
        'views/account_analytic_account_view.xml',
    ],
    'installable': True,
    'application': True,
    'qweb': [
    ],
}

