from odoo import models,fields,api


class Parents(models.Model):
    _name = "users.parents"
    _rec_name = "parent_name"

    parent_id= fields.Integer(string="ID", tracking=True)
    parent_image = fields.Binary(string="Image")
    parent_name = fields.Char( string="Parent Name", tracking=True)
    email = fields.Char(string="Email")
    phone_number = fields.Char(string="Phone Number")
