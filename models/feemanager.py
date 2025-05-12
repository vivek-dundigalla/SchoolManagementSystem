from odoo import models, fields


from datetime import time

class FeeManager(models.Model):
    _name = 'accounting.feemanager'




    class_name = fields.Selection([
        ('class one', 'Class One'),
        ('class two', 'Class Two'),
        ('class three', 'clas Three')
    ], string='Class')
    date =fields.Date(string="date")
    student = fields.Char(string="Student")

    invoice_title = fields.Char( string='Invoice Title')
    total_amount = fields.Integer(string="Total_amount")
    paid_amount = fields.Integer(string='Paid Amount')
    status = fields.Selection(
        [("All status", "All Status"), ("paid", "Paid"), ("unpaid", "Unpaid")], string="status")


    def action_save_invoice(self):

        return {'type': 'ir.actions.act_window_close'}


    def filter_invoice(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'accounting.feemanager',
            'view_mode': 'form',
            'target': 'current',

        }
