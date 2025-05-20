from odoo import models, fields

class StudentFeeManager(models.Model):
    _name = 'accounting.fee'


    class_names=fields.Many2one("academic.class","Class")
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

    def add_mass_invoice(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Mass invoice',
            'res_model': 'accounting.massinvoice',
            'view_mode': 'form',
            'target': 'new',

        }


    def filter_invoice(self):
            class_name1 = self.env.context.get('default_class_name1')
            domain = []
            if class_name1:
                domain.append(('class_names', '=', class_name1))

            return {
             'type': 'ir.actions.act_window',
            'name': 'Filtered Routines',
            'res_model': 'accounting.feemanager',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }
