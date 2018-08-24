# -*- coding: utf-8 -*-
{
    'name': 'Logos Invoice Analysis',
    'category': 'Account',
    'version': '9.0.1.3.0',
    'author': 'ADHOC SA',
    'website': 'www.adhoc.com.ar',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'l10n_ar_account',
        'logos_product_attributes',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/logos_invoice_analysis.xml',
        'view/product_view.xml',
    ],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}