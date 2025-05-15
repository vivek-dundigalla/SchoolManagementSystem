from odoo import models, fields

from datetime import time


class ManagePromotion(models.Model):
    _name = 'exam.managepromotion'

    image = fields.Binary(string="Image")
    name = fields.Many2one("school.student", "STUDENT NAME")
    section = fields.Selection([
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    ], string="Section")
    class_name = fields.Many2one("academic.class",string="Promoting From")

    status = fields.Selection([
        ('promoted', 'Promoted'),
        ('failed', 'Failed'),
    ], string='status')

    def action_save_promotion(self):
        return {'type': 'ir.actions.act_window_close'}

    def manage_promotion(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'filter',
            'res_model': 'exam.managepromotion',
            'view_mode': 'form',
            'target': 'current',

        }




