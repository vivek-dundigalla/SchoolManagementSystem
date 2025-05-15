from odoo import models, fields

class Marks(models.Model):
    _name = 'exam.marks'

    # standard_name = fields.Selection([
    #     ('class one', 'Class One'),
    #     ('class two', 'Class Two'),
    #     ('class three', 'Class Three'),
    #     ('class four', 'Class Four'),
    #     ('class five', 'Class Five'),
    #     ('class six', 'Class Six'),
    #     ('class seven', 'Class Seven'),
    #     ('class Eight', 'Class Eight'),
    #     ('class nine', 'Class Nine'),
    #     ('class Ten ', 'Class Ten'),
    #
    # ], string='Class')


    student_class_number1 = fields.Many2one("academic.class", store=True,string="Standard")

    sections = fields.Selection(
        [("A","A"),("B", "B"),("C","C")] ,string ="Section")

    subject = fields.Selection(
        [("Telugu","Telugu"),("Hindi", "Hindi"),("English","English"),
         ("Maths","Maths"),("Physics","Physics"),("Biology","Biology"),("Social Studies","Social Studies")] ,string ="Subject")


    def allot_marks(self):
        return {
            'type': 'ir.actions.act_window',
            'name': ',Marks',
            'res_model': 'exam.marksdetails',
            'view_mode': 'form',
            'target': 'new',

        }

    def filter_marks(self):
        for rec in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Filtered Marks',
                'res_model': 'exam.marksdetails',
                'view_mode': 'list,form',
                'domain': [('student_class_number1','=',rec.student_class_number1.id)],
                'target': 'current',
            }


