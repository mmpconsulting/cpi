# -*- coding: utf-8 -*-

from odoo import models, fields, api


class lwh_karton(models.Model):
    _inherit = 'product.template'

    checkbox_karton = fields.Boolean(string="Karton Box")
    lenght_karton = fields.Float(string="Lenght Karton")
    width_karton = fields.Float(string="Width Karton")
    height_karton = fields.Float(string="Height Karton")
    jenis_karton = fields.Many2one('product.packaging', string="Jenis Karton", store=True)
    warna_karton = fields.Many2one('product.packaging', string="Warna Karton", store=True)
    isi_karton = fields.Integer(string="Isi Per Box")