{
    'name': "Opportunities to/from Quotations",
    'version': '1.0',
    'depends': ['sale', 'crm'],
    'author': "Valentin THIRION, AbAKUS it-solutions SARL",
    'website': "http://www.abakusitsolutions.eu",
    'category': 'Sale/CRM',
    'description': 
    """
Quotations from and to CRM Leads
This modules adds a possible linkage between CRM Leads and Quotations.

On Leads, it is possible to list linked quotations and create new ones related.

On quotations, it is possible to link the document to a specific Lead for the same customer.

This module has been developed by Valentin THIRION @ AbAKUS it-solutions.
    """,
    'data': [
        'view/crm_lead_view.xml',
        'view/sale_order_view.xml',
    ],
}
