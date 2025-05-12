from odoo import models, fields

class StudentFeeManager(models.Model):
    _name = 'accounting.fee'

    class_name = fields.Selection([
        ('class one', 'Class One'),
        ('class two', 'Class Two'),
        ('class three', 'clas Three')
    ], string='Class')
    date = fields.Date( string='Date')
    status = fields.Selection(
        [("All status","All Status"),("paid", "Paid"),("unpaid","Unpaid")] ,string ="status")

    def add_single_invoice(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Single invoice',
            'res_model': 'accounting.feemanager',
            'view_mode': 'form',
            'target': 'new',

        }

    def filter_invoice(self):
        domain = []
        if self.class_name:
            domain.append(('class_name', '=', self.class_name))
        if self.date:
            domain.append(('date', '=', self.date))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Routines',
            'res_model': 'accounting.feemanager',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }
