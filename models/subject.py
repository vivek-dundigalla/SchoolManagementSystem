from odoo import models, fields

class Subject(models.Model):
    _name = 'academic.subject'
    _description = 'Subject'

    name = fields.Char(string="Subject Name", required=True)
    standard = fields.Selection([
        ('class one', 'Class One'),
        ('class two', 'Class Two'),
        ('class three', 'clas Three')
    ], string='Standard')

    def add_subject(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'academic.subjectlines',
            'view_mode': 'form',
            'target': 'new',

        }

    def filter_subject(self):
        domain = []
        if self.class_name:
            domain.append(('class_name', '=', self.class_name))


        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Subjects',
            'res_model': 'academic.subjectlines',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }