from odoo import fields, models, api, _
from odoo.exceptions import UserError


class SetOpenWizard(models.TransientModel):
    _name = 'merge.delivery.order.wizard'

    name = fields.Char(string='Name', default="Merge Delivery Order")    
    picking_ids = fields.Many2many(
        comodel_name='stock.picking', 
        relation='merge_delivery_order_picking_rel',
        column1='wizard_id',
        column2='picking_id',
        string='Deliver Orders'
        )        
    # move_ids = fields.Many2many(
    #     comodel_name='stock.move',
    #     relation='merge_delivery_wizard_stock_move_rel',
    #     column1='wizard_id',
    #     column2='move_id',
    #     string='Delivery Orders',
    # )    
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner', 
    )
    order_date = fields.Date(string='Order Date', default=fields.Datetime.now)
    
    def action_get_picking(self):
        # get stock picking
        pickings = self.env['stock.picking'].search([
            ('partner_id','=',self.partner_id.id),
            ('state','in',['confirmed','assigned','waiting']),
            ])
        self.picking_ids = pickings

        # new_picking = pickings[0].copy()
        
        # # mapping moves to self.move_ids 
        # self.move_ids = pickings.mapped('move_ids')
        
        # action_view = self.env.ref('bp_merge_delivery_and_invoice.action_merge_delivery_order_wizard_new')
        # action_view['res_id'] = self.id
        
        # return action_view.read()[0]
    
        view = self.env.ref('bp_merge_delivery_and_invoice.merge_delivery_order_wizard_view_new')

        return {
            'view_type': 'form',
            'view_mode': 'form',
            'name': self.name,
            'res_model': 'merge.delivery.order.wizard',
            'res_id': self.id,
            'view_id': view.id,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
        
    def process_wizard(self):
        sorted_picking = self.picking_ids.sorted(key='id')

        base_picking = sorted_picking[0]
        to_merge_sale_ids = []
        new_origin = base_picking.origin

        for picking in self.picking_ids:
            # unreserve all picking
            picking.do_unreserve()

            # add merged sale order to base_picking
            to_merge_sale_ids.append((4, picking.sale_id.id))

            if picking.id != base_picking.id:
                # for move in picking.move_ids_without_package:
                for move in picking.move_ids:
                    move.write({
                        'picking_id': base_picking.id,
                        'group_id': base_picking.group_id.id
                    })

                # append origin
                new_origin = new_origin + '; ' + picking.origin

                # unlink abandened transfer
                picking.unlink()

        # add merged sale order to base_picking
        base_picking.write({
            'origin': new_origin,
            'merged_sale_ids': to_merge_sale_ids,
            'is_merged_picking': True
        })

        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'stock.picking',
            'res_id': base_picking.id
        }