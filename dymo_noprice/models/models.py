# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dymo_noprice(models.Model):
#     _name = 'dymo_noprice.dymo_noprice'
#     _description = 'dymo_noprice.dymo_noprice'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
