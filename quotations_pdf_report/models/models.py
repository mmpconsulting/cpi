# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_ids = fields.One2many('account.payment', 'sale_order_id', string='Payments')

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    quotation_report_id = fields.Many2one('quotation.report', string='Quotation Report Line')

class QuotationReport(models.Model):
    _name = 'quotation.report'

    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    due_date = fields.Date(required=True, default=fields.Date.today)
    customers = fields.Many2many('res.partner', string='Customer')
    order_line_ids = fields.One2many('quotation.report.line', 'order_id', string='Order Lines')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    payment_ids = fields.One2many('account.payment', 'quotation_report_id', string='Payments')

    @api.onchange('date', 'due_date', 'customers')
    def _onchange_date_due_date(self):
        if self.date and self.due_date:
            self.order_line_ids = [(5, 0, 0)]
            
            orders = self.env['sale.order'].search([
                ('date_order', '>=', self.date),
                ('date_order', '<=', self.due_date),
            ])
            
            if self.customers:
                orders = orders.filtered(lambda r: r.partner_id.id in self.customers.ids)
            
            order_lines = []
            for order in orders:
                order_lines.append((0, 0, {
                    'reference_order': order.id,
                    'customer': order.partner_id.id,
                    'order_date': order.date_order,
                    'total': order.amount_total,
                }))

            self.order_line_ids = order_lines

    def action_submit(self):
        return self.env.ref('quotations_pdf_report.quotation_report_do').report_action(self)

class QuotationReportLine(models.Model):
    _name = 'quotation.report.line'

    order_id = fields.Many2one('quotation.report', string='Order')
    reference_order = fields.Many2one('sale.order', string='Reference Order')
    customer = fields.Many2one('res.partner', string='Customer')
    order_date = fields.Date(string='Order Date')
    total = fields.Float(string='Total')

    @api.onchange('reference_order')
    def _onchange_reference_order(self):
        if self.reference_order:
            self.customer = self.reference_order.partner_id.id
            self.order_date = self.reference_order.date_order
            self.total = self.reference_order.amount_total