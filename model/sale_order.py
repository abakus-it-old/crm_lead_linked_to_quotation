from openerp import models, fields, api
from openerp.osv import osv
from openerp import _
import logging
_logger = logging.getLogger(__name__)

class sale_order_with_opportunity(models.Model):
    _inherit = ['sale.order']

    opportunity_id = fields.Many2one('crm.lead', string="Opportunity")