from odoo import models,fields,api


class Librarian(models.Model):
    _name = "users.librarian"
    _rec_name = "librarian_name"

    librarian_id= fields.Integer(string="ID", tracking=True)
    librarian_image = fields.Binary(string="Image")
    librarian_name = fields.Char( string="Librarian Name", tracking=True)
    email = fields.Char(string="Email")
    phone_number = fields.Char(string="Phone Number")
