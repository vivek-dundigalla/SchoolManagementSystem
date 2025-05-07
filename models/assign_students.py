from odoo import models,fields,api

from datetime import date


class AssignStudents(models.Model):
    _name = "transport.assign"

    vechicle = fields.Many2one(comodel_name="transport.vechicle" ,string="Vechicle")
    assigned_date= fields.Date(string="Assigned date")

    def action_assign(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Assign students',
            'res_model': 'transport.assign',  # replace with your actual model name
            'view_mode': 'form',
            'target': 'new',  # use 'current' if you want full screen instead of popup
            'context': {
                'default_vehicle_id': self.id  # optional: set default field values
            }
        }