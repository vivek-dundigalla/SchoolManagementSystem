from odoo import models, fields

class Syllabus(models.Model):
    _name = 'academic.syllabus'

    class_name = fields.Selection([
        ('class one', 'Class One'),
        ('class two', 'Class Two'),
        ('class three', 'clas Three')
    ], string='Class')

    section = fields.Selection(
        [("A","A"),("B", "B"),("C","C")] ,string ="Section")

    def create_syllabus(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Syllabus',
            'res_model': 'academic.syllabusdetails',
            'view_mode': 'form',
            'target': 'new',

        }

    def filter_syllabus(self):
        domain = []
        if self.class_name:
            domain.append(('class_name', '=', self.class_name))
        if self.section:
            domain.append(('section', '=', self.section))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Syllabus',
            'res_model': 'academic.syllabusdetails',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }
