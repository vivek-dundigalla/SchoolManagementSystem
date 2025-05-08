from odoo import models,fields,api


class Accountant(models.Model):
    _name = "users.accountant"
    _rec_name = "accountant_name"

    accountant_id= fields.Integer(string="ID", tracking=True)
    accountant_image = fields.Binary(string="Image")
    accountant_name = fields.Char( string="Accountant Name", tracking=True)
    email = fields.Char(string="Email")
    phone_number = fields.Char(string="Phone Number")
