from odoo import models, fields


from datetime import time

class SubjectLines(models.Model):
    _name = 'academic.subjectlines'



    class_name = fields.Selection([
        ('class one', 'Class One'),
        ('class two', 'Class Two'),
        ('class three', 'clas Three')
    ], string='Class')
    name = fields.Char(string="Subject Name", required=True)



    def action_save_subject(self):

        return {'type': 'ir.actions.act_window_close'}


    def filter_subject(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'academic.subjectlines',
            'view_mode': 'form',
            'target': 'current',

        }
