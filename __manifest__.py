# -*- coding: utf-8 -*-
{
    'name': "New Haza E-Invoice Report",
    'author':
        'ENZAPPS',
    'summary': """
This module is for printing E-Invoice report for Haza.
""",

    'description': """
        This module is for printing E-Invoice report for Haza.
    """,
    'website': "",
    'category': 'base',
    'version': '14.0',
    'depends': ['base','account','uom_unece','base_unece','account_tax_unece','base_vat_sanitized','onchange_helper','base_iban','base_bank_from_iban','base_business_document_import','account_invoice_import','base_ubl_payment','account_payment_partner','account_invoice_import_ubl','account_invoice_ubl','sale','purchase','stock','haza_einvoice_report'],
    'data': [
            'report/reports.xml',
            'report/report_view.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}
