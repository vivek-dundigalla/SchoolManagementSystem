from odoo import models, fields

class Routine(models.Model):
    _name = 'academic.routine'

    # class_name = fields.Selection([
    #     ('class one', 'Class One'),
    #     ('class two', 'Class Two'),
    #     ('class three', 'clas Three')
    # ], string='Class')
    class_number1=fields.Many2one("academic.class","Class")
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

    # def filter_routine(self):
    #     domain = []
    #     if self.class_name:
    #         domain.append(('class_name', '=', self.class_name))
    #     if self.section:
    #         domain.append(('section', '=', self.section))

    # def filter_routine(self):
    #     class_names = self.env.context.get('default_class_namess')
    #     domain = []
    #     if class_namess:
    #         domain.append(('class_number1', '=', class_namess))  # Filter by class_name in 'academic.subject'


    def filter_routine(self):
        # Check if 'default_class_name' is in the context
        class_id = self.env.context.get('default_class_id')
        domain = []
        if class_id:
            domain.append(('class_id', '=', class_id))  # Filter by class_name in 'academic.subject'

        return {
        'type': 'ir.actions.act_window',
        'name': 'Filtered Routines',
        'res_model': 'academic.timetable',
        'view_mode': 'list',
        'domain': domain,
        'target': 'current',
    }
