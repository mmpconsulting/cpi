# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class addons\report_penerimaan(models.Model):
#     _name = 'addons\report_penerimaan.addons\report_penerimaan'
#     _description = 'addons\report_penerimaan.addons\report_penerimaan'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
