from odoo import models, fields


from datetime import time

class SyllabusDetails(models.Model):
    _name = 'exam.marksdetails'




    student_name = fields.Many2one("school.admission", string='Student Name')

    marks_id = fields.Many2one("exam.marks", string="Marks Reference")  # Add this line

    marks = fields.Integer(string="Marks")
    grade_point = fields.Char(string='Grade Point')
    comment = fields.Char(string="Comment")
    student_class_number = fields.Selection(related='student_name.student_class_number', store=True)
    # student_section_ABC = fields.Selection(related='student_name.student_section_ABC', store=True)
    sections = fields.Selection([
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    ], string="Section")
    #
    # def action_save_marks(self):
    #
    #     return {'type': 'ir.actions.act_window_close'}
    def action_save_marks(self):
        vals = {
            'student_name': self.student_name.id,
            'marks': self.marks,
            'grade_point': self.grade_point,
            'comment': self.comment,
            'marks_id': self.marks_id.id,  # assuming marks_id is passed via context
        }
        self.env['exam.marksdetails'].create(vals)

        return {'type': 'ir.actions.act_window_close'}

    def filter_marks(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'exam.marksdetails',
            'view_mode': 'form',
            'target': 'current',

        }
