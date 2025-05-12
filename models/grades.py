from odoo import models,fields,api

from datetime import date

class Grades(models.Model):
    _name = "exam.grades"


    grade = fields.Char(string="Grade")
    grade_point = fields.Float(string="Grade Point", tracking=True)
    mark_from = fields.Date(string="Mark From")
    mark_upto= fields.Date(string="Mark Upto")
