from odoo import _, api, fields, models

class HrDepartment(models.Model):
    _inherit = 'hr.department'
    
    code = fields.Char('Code')
    