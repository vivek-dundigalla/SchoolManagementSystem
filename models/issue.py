from odoo import models, fields


from datetime import time

class Issue(models.Model):
    _name = 'back.issue'




    date = fields.Date(string='Issue Date')
    name = fields.Char(string="student")
    student_class_number = fields.Selection([
        ("Class Ten", "Class Ten"),
        ("Class Nine", "Class Nine"),
        ("Class Eight", "Class Eight"),
        ("Class Seven", "Class Seven"),
        ("Class Six", "Class Six"),
        ("Class Five", "Class Five"),
        ("Class Four", "Class Four"),
        ("Class Three", "Class Three"),
        ("Class Two", "Class Two"),
        ("Class One", "Class One")
    ], string="Class", tracking=True)
    book_name =fields.Char(string="Book")

    def action_save_book_issue(self):

        return {'type': 'ir.actions.act_window_close'}


    def filter_issue(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'back.issue',
            'view_mode': 'form',
            'target': 'current',

        }
