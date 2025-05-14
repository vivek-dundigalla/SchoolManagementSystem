from odoo import models, fields

class Subject(models.Model):
    _name = 'academic.subject'

    # class_name = fields.Selection([
    #     ('class one', 'Class One'),
    #     ('class two', 'Class Two'),
    #     ('class three', 'clas Three')
    # ], string='Class')

    standard_name=fields.Char(string="Class Name")

    def add_subject(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Subject',
            'res_model': 'academic.subjectlines',
            'view_mode': 'form',
            'target': 'new',

        }



    def filter_subject(self):
        domain = []
        if self.standard_name:
            domain.append(('standard_name', '=', self.standard_name))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Subjects',
            'res_model': 'academic.subjectlines',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }
