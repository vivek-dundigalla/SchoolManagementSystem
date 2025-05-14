from odoo import models, fields

class SubjectLinesLine(models.Model):
    _name = "academic.subjectlines.line"

    subject = fields.Char("Subject")
    concept = fields.Many2one("academic.subjectlines", string="Concept")
    class_name = fields.Selection(related="concept.class_name", store=True, string="Class")
