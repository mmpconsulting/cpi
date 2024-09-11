from odoo import models, fields, api

class OutstandingReport(models.Model):
    _name = 'outstanding.report'

    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    due_date = fields.Date(required=True, default=fields.Date.today)
    vendors = fields.Many2many('res.partner', string='Vendors')
    order_line_ids = fields.One2many('outstanding.report.line', 'order_id', string='Order Lines')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    @api.onchange('date', 'due_date', 'vendors')
    def _onchange_date_due_date(self):
        if self.date and self.due_date:
            self.order_line_ids = [(5, 0, 0)]
            
            orders = self.env['purchase.order'].search([
                ('date_order', '>=', self.date),
                ('date_order', '<=', self.due_date),
            ])
            
            if self.vendors:
                orders = orders.filtered(lambda r: r.partner_id.id in self.vendors.ids)
            
            order_lines = []
            for order in orders:
                order_lines.append((0, 0, {
                    'reference_order': order.id,
                    'supplier': order.partner_id.id,
                    'order_date': order.date_order,
                    'total': order.amount_total,
                }))

            self.order_line_ids = order_lines

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

    @api.onchange('')
    def _onchange_reference_order(self):
        if self.reference_order:
            self.supplier = self.reference_order.partner_id.id
            self.order_date = self.reference_order.date_order
            self.total = self.reference_order.amount_total

class OutstandingReportSo(models.Model):
    _name = 'outstanding.report.so'

    date = fields.Date(string='Date', required=True, default=fields.Date.today)
    due_date = fields.Date(required=True, default=fields.Date.today)
    vendors = fields.Many2many('res.partner', string='Vendors')
    order_line_ids = fields.One2many('outstanding.report.line.so', 'order_id', string='Order Lines')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)

    @api.onchange('date', 'due_date', 'vendors')
    def _onchange_date_due_date(self):
        if self.date and self.due_date:
            self.order_line_ids = [(5, 0, 0)]
            
            orders = self.env['sale.order'].search([
                ('date_order', '>=', self.date),
                ('date_order', '<=', self.due_date),
            ])
            
            if self.vendors:
                orders = orders.filtered(lambda r: r.partner_id.id in self.vendors.ids)
            
            order_lines = []
            for order in orders:
                order_lines.append((0, 0, {
                    'reference_order': order.id,
                    'supplier': order.partner_id.id,
                    'order_date': order.date_order,
                    'total': order.amount_total,
                }))

            self.order_line_ids = order_lines

    def action_submit(self):
        print('action_submit')
        return self.env.ref('outstanding_report.outstanding_purchase_order_report_action').report_action(self)

class OutstandingReportLine(models.Model):
    _name = 'outstanding.report.line.so'
    _description = 'Outstanding Report Line Sale Order'

    order_id = fields.Many2one('outstanding.report.so', string='Order')
    reference_order = fields.Many2one('sale.order', string='Reference Order')
    supplier = fields.Many2one('res.partner', string='Supplier')
    order_date = fields.Date(string='Order Date')
    total = fields.Float(string='Total')

    @api.onchange('')
    def _onchange_reference_order(self):
        if self.reference_order:
            self.supplier = self.reference_order.partner_id.id
            self.order_date = self.reference_order.date_order
            self.total = self.reference_order.amount_total