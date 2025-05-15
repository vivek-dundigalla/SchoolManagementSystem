from odoo import models, fields


from datetime import time

class AssigningStudentsToDrivers(models.Model):
    _name = 'transport.assignstudents'




    vh_model = fields.Many2one("transport.vechicle","Vechicle")
    section = fields.Selection(
        [("A", "A"), ("B", "B"), ("C", "C")], string="Section")
    student_class_number = fields.Many2one("school.admission",string="Class")
    student_name = fields.Many2one("school.student",string='Student')





    def action_save_students(self):

        return {'type': 'ir.actions.act_window_close'}


    def filter_students(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'transport.assignstudents',
            'view_mode': 'form',
            'target': 'current',

        }
