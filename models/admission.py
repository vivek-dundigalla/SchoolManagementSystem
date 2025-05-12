

from odoo import models, fields, api



class admissions(models.Model):
    _name = "school.admission"

    student_name = fields.Many2one(comodel_name="res.partner", string="Student Name", tracking=True)
    student_email = fields.Char(string="Email", tracking=True)
    student_password = fields.Char(string="Password", password=True)
    parent = fields.Many2one(comodel_name="res.partner", string="Parent", tracking=True)
    # student_class = fields.Selection([("Class Ten", "Class Ten"), ("Class Nine", "Class Nine"), ("Class Eight", "Class Eight"), ("Class Seven", "Class Seven"), ("Class Six", "Class Six"), ("Class Five", "Class Five"), ("Class Four", "Class Four"), ("Class Three", "Class Three"), ("Class Two", "Class Two"), ("Class One", "Class one")], "Class" , tracking=True,)
    student_class_number = fields.Selection([
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

    student_section_ABC = fields.Selection([
        ("A", "A"),
        ("B", "B"),
        ("C", "C")], "Section" , tracking=True,)

    student_dob = fields.Datetime(string="Date of Birth", tracking=True)
    student_gender = fields.Selection([("male", "Male"), ("female", "Female")], "Gender" , tracking=True,)
    student_blood_group = fields.Selection([("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"), ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")], "Blood group" , tracking=True,)
    student_address = fields.Char(string="Address")
    student_number = fields.Char(string="Mobile Number")
    student_image = fields.Binary(string="Student Profile Image")


    def single_student_admission(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Create Driver',
            'res_model': 'school.admission',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_student_id': self.id
            }
        }

    def bulk_student_admission(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bulk Student Admission',
            'res_model': 'users.bulk',
            'view_mode': 'form',
            'target': 'current',
            'context': {
                'default_student_id': self.id
            }
        }