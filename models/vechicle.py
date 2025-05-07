from odoo import models,fields,api


class Drivers(models.Model):
    _name = "transport.vechicle"
    _rec_name = "vh_model"

    number = fields.Integer(string="S.No")
    vh_number = fields.Char(string="Vechicle Number")
    vh_model = fields.Char(string="Vechicle Model")
    capacity = fields.Float(string="Capacity")
    route = fields.Char(string="Route")


    def action_create_vehicle(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Create Driver',
            'res_model': 'transport.vechicle',  # replace with your actual model name
            'view_mode': 'form',
            'target': 'new',  # use 'current' if you want full screen instead of popup
            'context': {
                'default_vehicle_id': self.id  # optional: set default field values
            }
        }



