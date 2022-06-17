# -*- coding: utf-8 -*-
{
    'name': """Bolivia - E-invoicing""",
    "version": "14.0.0.2",
    #     'description': """
    # EDI Bolivian Localization
    # ========================
    # This code allows to generate the DTE document for Bolivian invoicing.
    # - DTE (Electronic Taxable Document) format in XML
    # - Direct Communication with SIN (Sistema de Impuestos Nacionales) to send invoices and other tax documents related to sales.
    # - Communication with Customers to send sale DTEs.
    # - Communication with Suppliers (vendors) to accept DTEs from them.
    # - Direct Communication with SII informing the acceptance or rejection of vendor bills or other DTEs.

    #  In order to see the barcode on the invoice, you need the pdf417gen library.

    #     """,

    'author': "Indasoge-Alphasys",
    'website': "http://www.alphasys.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting/Localizations',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'l10n_bo',
                'sale_management',
                'purchase',
                'account'
                # 'point_of_sale'
                ],

    # always loaded
    'data': [
        'views/views.xml',
        'views/templates.xml',
        'views/dte_cuf_view.xml',
        'views/company_activities_view.xml',
        'views/account_move_form_inherit.xml',
        'views/base_view_users_form_inherit.xml',
        'views/branch_office.xml',
        'views/selling_point_view.xml',
        'views/cufd_view.xml',
        # 'views/pos_config_view_inherit.xml',
        'views/res_partner_form_inherit.xml',
        'views/sin_items_view.xml',
        'views/product_template_form_inherit.xml',
        'views/l10n_bo_edi_actions.xml',
        'views/res_config_settings_view.xml',
        'security/ir.model.access.csv',
        'reports/graphic_representation.xml',
        'reports/graphic_representation_templates.xml',
        'views/invoice_dosage.xml',
        # 'views/action_manager.xml',
        # 'wizard/sales_book_wizard_view.xml',
        # 'views/account_report_menuitems.xml',
        # 'reports/sales_book.xml',
        # 'reports/sales_book_templates.xml'
        # Account Payment
        'security/account_payment_mode.xml',
        'views/res_bank_inherit.xml',
        'views/account_payment_method.xml',
        'views/account_journal.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
