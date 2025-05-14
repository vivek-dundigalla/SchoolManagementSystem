from odoo import models,fields,api


class Class(models.Model):
    _name = "academic.class"
    _rec_name = "class_names"

    class_names= fields.Selection([
        ("Class Ten", "Class Ten"),
        ("Class Nine", "Class Nine"),
        ("Class Eight", "Class Eight"),
        ("Class Seven", "Class Seven"),
        ("Class Six", "Class Six"),
        ("Class Five", "Class Five"),
        ("Class Four", "Class Four"),
        ("Class Three", "Class Three"),
        ("Class Two", "Class Two"),
        ("Class One", "Class One")
    ], string="Class",  tracking=True)
    section = fields.Char(string="Section")
