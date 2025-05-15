from odoo import models, fields

from datetime import time


class TakeAttendance(models.Model):
    _name = 'academic.takeattendance'

    date = fields.Date(string="Date")

    class_name = fields.Many2one("academic.class",string="Promoting From")
    section = fields.Selection([
        ("A", "A"),
        ("B", "B"),
        ("C", "C")
    ], string="Section")

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




