from odoo import models, fields, api

class OutstandingReport(models.Model):
    _name = 'outstanding.report'

    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    due_date = fields.Date(required=True, default=fields.Date.today)
    vendors = fields.Many2one('res.partner', string='Vendor', required=True)
    order_line_ids = fields.One2many('outstanding.report.line', 'order_id', string='Order Lines')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    def action_submit(self):
        print('action_submit')
        return self.env.ref('outstanding_report.outstanding_purchase_order_report_action').report_action(self)

class OutstandingReportLine(models.Model):
    _name = 'outstanding.report.line'
    _description = 'Outstanding Report Line'

    order_id = fields.Many2one('outstanding.report', string='Order')
    reference_order = fields.Many2one('purchase.order', string='Reference Order')
    supplier = fields.Many2one('res.partner', string='Supplier')
    order_date = fields.Date(string='Order Date')
    total = fields.Float(string='Total')
        

    @api.onchange('reference_order')
    def _onchange_reference_order(self):
        if self.reference_order:
            self.supplier = self.reference_order.partner_id.id
            self.order_date = self.reference_order.date_order
            self.total = self.reference_order.amount_total