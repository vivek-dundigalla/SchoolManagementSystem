from odoo import models, fields



class SchoolSettings(models.Model):
    _name = 'school.settings'

    school_name = fields.Char(string="School Name")
    phone = fields.Integer(string='Phone Number')
    address=fields.Char(string="Address")

    def update_settings(self):
        return {'type': 'ir.actions.act_window_close'}
