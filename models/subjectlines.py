from odoo import models, fields


from datetime import time

class StudentLines(models.Model):
    _name = 'academic.subjectlines'




    class_name = fields.Selection([
        ('class one', 'Class One'),
        ('class two', 'Class Two'),
        ('class three', 'clas Three')
    ], string='Class')
    # subject = fields.Selection([
    #     ('Telugu', 'Telugu'),
    #     ('HIndi', 'Hindi')], string="Subject")
    concept_id =fields.One2many("academic.subjectlines.line","concept", string="concept")



    def action_save_subject(self):

        return {'type': 'ir.actions.act_window_close'}


    def filter_subject(self):

        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'academic.subjectlines',
            'view_mode': 'form',
            'target': 'current',

        }

class SubjectLines(models.Model):
    _name = "academic.subjectlines.line"

    subject = fields.Char("Subject")
    concept =fields.Many2one("academic.subjectlines",string="concept")