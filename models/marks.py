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

    student_class_number = fields.Many2one("school.admission", store=True,string="Standard")

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

    # def filter_marks(self):
    #     domain = []
    #     if self.standard_name:
    #         domain.append(('standard_name', '=', self.standard_name))
    #     if self.sections:
    #         domain.append(('sections', '=', self.sections))
    #     if self.subject:
    #         domain.append(('subject', '=', self.subject))
    #
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Filtered Marks',
    #         'res_model': 'exam.marksdetails',
    #         'view_mode': 'list',
    #         'domain': domain,
    #         'target': 'current',
    #     }

    # marks.py

    # def filter_marks(self):
    #     domain = []
    #     if self.standard_name:
    #         domain.append(('marks_id.standard_name', '=', self.standard_name))
    #     if self.sections:
    #         domain.append(('marks_id.sections', '=', self.sections))
    #     if self.subject:
    #         domain.append(('marks_id.subject', '=', self.subject))
    #
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Filtered Marks',
    #         'res_model': 'exam.marksdetails',
    #         'view_mode': 'list,form',
    #         'domain': domain,
    #         'target': 'current',
    #         'context': {
    #             'default_marks_id': self.id
    #         }
    #     }

    def filter_marks(self):
        domain = []
        if self.student_class_number:
            domain.append(('student_class_number', '=', self.student_class_number))
        if self.sections:
            domain.append(('sections', '=', self.sections))
        if self.subject:
            domain.append(('marks_id.subject', '=', self.subject))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Marks',
            'res_model': 'exam.marksdetails',
            'view_mode': 'list,form',
            'domain': domain,
            'target': 'current',
        }


