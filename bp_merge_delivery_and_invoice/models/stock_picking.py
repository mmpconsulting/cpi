from odoo import models, fields, api, _
from odoo.exceptions import UserError
from pprint import pprint

class StockPicking(models.Model):
    _inherit = 'stock.picking'
    
    merged_sale_ids = fields.Many2many(
        comodel_name='sale.order',
        relation='merged_picking_sale_order_rel',
        column1='picking_id',
        column2='order_id',
        string='Merged Sale Order'
    )
    is_merged_picking = fields.Boolean(string='Merged Delivery', default=False)
    
    is_merged_picking = fields.Boolean(string='Merged Delivery', default=False)
    is_merge_invoice_created = fields.Boolean(string='Invoice Created', default=False)
    invoice_merge_count = fields.Integer(string="Invoice Count",compute='_compute_invoice_merge_count', inverse='_inverse_field' )
    invoice_merge_ids = fields.Many2many(
        comodel_name='account.move',
        relation='merged_stock_picking_account_move_rel',
        column1='picking_id',
        column2='account_move_id',
        string='Invoices'
    )
    
    def _inverse_field(self):
        pass
    
    @api.depends('invoice_merge_ids')
    def _compute_invoice_merge_count(self):
        for rec in self:
            if rec.invoice_merge_ids:
                rec.invoice_merge_count = len(rec.invoice_merge_ids)
    
    @api.depends("invoice_ids")
    def _compute_invoice_count(self):
        for order in self:
            order.invoice_count = len(order.invoice_ids.filtered(lambda x: x.state != 'cancel'))
            
    def action_view_merge_invoice(self):
        # return {
        #     'name': _(' Invoices'),
        #     'type': 'ir.actions.act_window',
        #     'view_id': self.env.ref('account.view_move_form').id,
        #     'view_mode': 'form',
        #     'res_model': 'account.move',
        #     'target': 'current',
        #     'domain':[('id', 'in', self.invoice_merge_ids.ids)],
        #     # 'res_id': self.invoice_merge_ids[0].id
        # }
        # self.ensure_one()
        form_view_name = "account.view_move_form"
        result = self.env["ir.actions.act_window"]._for_xml_id(
            "account.action_move_out_invoice_type"
        )
        # if len(self.invoice_ids) > 1:
        #show_invoices = self.invoice_merge_ids.filtered(lambda x: x.state not in ['cancel'])
        show_invoices = self.invoice_merge_ids
        # if len(self.invoice_merge_ids) > 1:
        if len(show_invoices) > 0:
            # result["domain"] = "[('id', 'in', %s),('state','!=','cancel')]" % self.invoice_ids.ids
            result["domain"] = "[('id', 'in', %s)]" % show_invoices.ids
            return result
        else:
            raise UserError('There is no invoice to show.')
        # else:
        #     form_view = self.env.ref(form_view_name)
        #     result["views"] = [(form_view.id, "form")]
        #     result["res_id"] = self.invoice_ids.id
        # return result

    def action_create_invoices(self):
        if self.is_merged_picking and len(self.merged_sale_ids) > 1:
            generated_invoices = []
            
            #sale_ids = self.move_ids_without_package.mapped('sale_line_id').mapped('order_id').filtered(lambda x : x.invoice_status == 'to invoice')
            sale_ids = self.move_ids_without_package.mapped('sale_line_id').mapped('order_id').filtered(lambda x : x.invoice_status in ['to invoice'])
            for sale in sale_ids:
            # for sale in self.merged_sale_ids:
                # generated_invoices.append(sale.action_invoice_create())
                # for inv in sale.action_invoice_create():
                for inv in sale._create_invoices():
                    generated_invoices.append(inv.id)

                self.write({
                    'is_merge_invoice_created': True,
                    # 'invoice_merge_count': 1
                })
                
            # merge invoices
            merge = self.env['invoice.merge'].create({
                'date_invoice' : fields.Date.today()
            })
            
            action = merge.with_context(active_ids=generated_invoices).merge_invoices()
            
            new_invoice_id = merge.new_invoice_id
            print("New invoice created for merge ................")
            print(new_invoice_id)
            new_inv = self.env['account.move'].search([('id','=',new_invoice_id)])
            
            # Trying to update the quantity based on Picking Slip
            # Edited by Santoso SA
            
            for line in new_inv.invoice_line_ids:                
                picking_line = self.move_lines.search([('product_id','=',line.product_id.id),('picking_id','=',self.id),('sale_line_id','=',line.sale_line_ids.id)])
                if picking_line:                    
                    line.quantity = picking_line.product_qty
                else:
                    line.unlink()
                    
            # tobe_merged_invoices = self.env['account.move'].search(
            #     [('id', 'in', generated_invoices)])
            # base_invoice = tobe_merged_invoices[0]
            # for inv in tobe_merged_invoices:
            #     if inv != base_invoice:
            #         for line in inv.invoice_line_ids:
            #             line.write({
            #                 'move_id': base_invoice.id
            #             })

            #         # unlink abandoned invoice
            #         inv.unlink()

            # # set picking for base_invoice
            # base_invoice.write({
            #     'base_picking_id': self.id
            # })

            # add created invoice to picking
            self.write({
                # 'invoice_merge_ids': [(4, new_invoice_id)]
                'invoice_merge_ids': [new_invoice_id]
            })
            
            return {
                'name': _(' Invoices'),
                'type': 'ir.actions.act_window',
                'view_id': self.env.ref('account.view_move_form').id,
                'view_mode': 'form',
                'res_model': 'account.move',
                'target': 'current',
                # 'domain':[('id', 'in', self.invoice_merge_ids.ids)],
                'res_id': new_invoice_id
            }
        
        else:
            #search sale 
            if self.merged_sale_ids:
                # self.merged_sale_ids.action_view_sale_advance_payment_inv()
                # create payment advance
                paym_adv = self.env['sale.advance.payment.inv'].create({
                    'sale_order_ids' : self.merged_sale_ids.ids
                })
                paym_adv._create_invoices(self.merged_sale_ids)
                return self.merged_sale_ids.action_view_invoice()                
            else:
                # get associated sale 
                if self.sale_id :
                    paym_adv = self.env['sale.advance.payment.inv'].create({
                    'sale_order_ids' : self.sale_id.ids
                    })
                    paym_adv._create_invoices(self.sale_id)
                    return self.sale_id.action_view_invoice()                
                


    # def button_validate(self):
    #     res = super().button_validate()
    #     # filtered merged_sale_ids
        
        
            
        
    #     return res
