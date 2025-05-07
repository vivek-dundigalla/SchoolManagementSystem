from odoo import models, fields, api
# from datetime import date, datetime

class schooltransportdrivers(models.Model):
    _name = "school.drivers"

    driver_image = fields.Binary(string="Image")
    driver_s_no = fields.Integer(string="S.no")
    driver_name = fields.Many2one(comodel_name="res.partner", string="Driver Name", tracking=True, required=True)
    driver_email = fields.Char(string="Email", tracking=True, required=True)
    driver_number = fields.Char(string="Mobile Number")
    driver_vehicle_number = fields.Char(string="Vehicle Number")