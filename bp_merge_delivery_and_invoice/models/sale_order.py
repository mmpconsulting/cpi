from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    
    merged_packing_ids = fields.Many2many(
        comodel_name='stock.picking',
        relation='merged_picking_sale_order_rel',
        column1='order_id',
        column2='picking_id',
        string='Merged Pircking',
        copy=False
    )

    merged_picking_count = fields.Integer(
        string='Merged Picking Count', compute='_compute_merged_picking_count', copy=False
    )

    @api.depends('merged_packing_ids')
    def _compute_merged_picking_count(self):
        for rec in self:
            rec.merged_picking_count = len(rec.merged_packing_ids)
    
    def action_view_merged_picking(self):
        picking_view = {
            'name': _(' Merged Delivery'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'stock.picking',
            'domain': [('id', 'in', self.merged_packing_ids.ids)],
        }

        if len(self.merged_packing_ids.ids) == 1:
            picking_view['view_mode'] = 'form'
            picking_view['res_id'] = self.merged_packing_ids[0].id

        return picking_view

    