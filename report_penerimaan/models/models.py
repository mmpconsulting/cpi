# -*- coding: utf-8 -*-

from odoo import models, fields, api


class report_penerimaan(models.Model):
    _inherit = 'stock.picking'

    no_sj = fields.Char(string='No Surat Jalan', required=False)

class report_penerimaan(models.Model):
    _inherit = 'stock.move'

    notes = fields.Char(string='Keterangan', required=False)
