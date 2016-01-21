from openerp import models, fields, api
from openerp.osv import osv
from openerp import _
import logging
_logger = logging.getLogger(__name__)

class lead_with_quotations(models.Model):
    _inherit = ['crm.lead']

    quotation_ids = fields.One2many('sale.order', 'opportunity_id', string="Quotations and Sales Orders")