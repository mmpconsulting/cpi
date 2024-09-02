# -*- coding: utf-8 -*-
{
    'name': "Merge Delivery",

    'summary': """
        Merge delivery and invoice """,

    'description': """
        Merge delivery and invoice
    """,

    'author': "butirpadi",
    'website': "https://www.github.com/butirpadi",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '16.0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock','sale','sale_stock', 'account_invoice_merge', 'stock_picking_invoice_link'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/merge_delivery_order_wizard_view.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application' : True
}
