from odoo import models, fields

class Routine(models.Model):
    _name = 'academic.routine'

    class_name = fields.Selection([
        ('class one', 'Class One'),
        ('class two', 'Class Two'),
        ('class three', 'clas Three')
    ], string='Class')
    section = fields.Selection([
        ('a', 'A'),
        ('b', 'B'),
        ('c', 'C')
    ], string='Section')

    def add_routine(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'academic.timetable',
            'view_mode': 'form',
            'target': 'new',

        }

    def filter_routine(self):
        domain = []
        if self.class_name:
            domain.append(('class_name', '=', self.class_name))
        if self.section:
            domain.append(('section', '=', self.section))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Routines',
            'res_model': 'academic.timetable',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }
