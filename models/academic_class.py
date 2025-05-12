from odoo import models,fields,api


class Class(models.Model):
    _name = "academic.class"
    _rec_name = "class_name"

    class_name= fields.Char(string="Name", tracking=True)
    section = fields.Char(string="Section")
