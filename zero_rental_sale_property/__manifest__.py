{
    "name": "zero_rental_sale_property",
    'version': '1.0',
    "summary": "rental and sales properaty management ",
    'description': """this App for Renting and Sales Properaty management full cycle integrated with odoo 12 (sales ,ecommerce and accouting)-tested on odoo community and enterprise 12-Support English and Arabic interface""",
    'depends': ['base', 'sale_management', 'account','l10n_generic_coa', 'analytic','om_account_asset','website_sale'],
    "category": 'real estate',
    'author': 'Zero Systems',
    'company': 'Zero for Information Systems',
    'website': "https://www.erpzero.com",
    'email': "sales@erpzero.com",
    'data': [
        #'security/security.xml',
        #'security/ir.model.access.csv',
        'report/report_contract.xml',
        'report/contract_views.xml','views/property.xml',
        'views/tenant.xml',
        'views/tenancy.xml',
        'views/sale_order.xml',
        'views/rent_type.xml',
        'views/property_menuitem.xml',
        'views/res_city.xml',
        'data/property_conf.xml','data/mail_template.xml',
    ],
    'images': ['static/description/logo.PNG'],
    'installable': True,
    'auto_install': False,
    'application': True,
}
