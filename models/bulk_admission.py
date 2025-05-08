from odoo import models, fields, api



class bulkAdmissiom(models.Model):
    _name = "users.bulk"

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

    def bulk_student_admission(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Bulk Student Admission',
            'res_model': 'users.bulk',  # replace with your actual model name
            'view_mode': 'form',
            'target': 'current',  # use 'current' if you want full screen instead of popup
            'context': {
                'default_student_id': self.id  # optional: set default field values
            }
        }

    def single_student_admission(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Single Sudent Admission',
            'res_model': 'school.admission',  # replace with your actual model name
            'view_mode': 'form',
            'target': 'current',  # use 'current' if you want full screen instead of popup
            'context': {
                'default_student_id': self.id  # optional: set default field values
            }
        }