from odoo import models, fields, api
from datetime import date, datetime


class admissions(models.Model):
    _name = "school.admissions"

    student_name = fields.Many2one(comodel_name="res.partner", string="Student Name", tracking=True, required=True)
    student_email = fields.Char(string="Email", tracking=True, required=True)
    student_password = fields.Char(string="Password", tracking=True, required=True)
    parent = fields.Many2one(comodel_name="res.partner", string="Parent", tracking=True, required=True)
    student_class = fields.Many2one(comodel_name="res.partner", string="Class", tracking=True, required=True)
    student_section = fields.Many2one(comodel_name="res.partner", string="Section", tracking=True, required=True)
    student_dob = fields.Datetime(string="Date of Birth", tracking=True, required=True)
    student_gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender" , tracking=True,)
    student_blood_group = fields.Selection([("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")], "Blood group" , tracking=True,)
    student_address = fields.Char(string="Address")
    student_number = fields.Char(string="Mobile Number")
    student_image = fields.Binary(string="Image")
