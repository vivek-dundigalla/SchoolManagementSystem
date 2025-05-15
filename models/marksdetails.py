from odoo import models, fields,api


from datetime import time

class SyllabusDetails(models.Model):
    _name = 'exam.marksdetails'




    name = fields.Many2one("school.student", string='Student Name' ,domain=[('student_class_number1','!=',False)])

    marks_id = fields.Many2one("exam.marks", string="Marks Reference")  # Add this line

    marks = fields.Integer(string="Marks")
    # grade_point = fields.Char(related="marks_id.grade_point",string='Grade Point')
    grade = fields.Char(string="Grade", compute="_compute_grade", store=True)
    grade_point = fields.Float(string="Grade Point", compute="_compute_grade", store=True)
    comment = fields.Char(string="Comment")
    # student_class_number = fields.Selection(related='name.student_class_number', store=True)
    student_class_number1 = fields.Many2one("academic.class","Class",related="name.student_class_number1",store=True)
    # student_section_ABC = fields.Selection(related='student_name.student_section_ABC', store=True)
    sections = fields.Selection([
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    ], string="Section",store=True)
    #
    # def action_save_marks(self):
    #
    #     return {'type': 'ir.actions.act_window_close'}
    def action_save_marks(self):
        vals = {
            'name': self.name.id,
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

    @api.depends('marks')
    def _compute_grade(self):
        for rec in self:
            grade_obj = self.env['exam.grades'].search([
                ('from_marks', '<=', rec.marks),
                ('upto_marks', '>=', rec.marks)
            ], limit=1)

            rec.grade = grade_obj.grade if grade_obj else ''
            rec.grade_point = grade_obj.grade_point if grade_obj else 0.0