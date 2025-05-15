from odoo import models, fields

class Promotion(models.Model):
    _name = 'exam.promotion'

    class_name = fields.Many2one("academic.class",string="Promoting From")
    class_name1 = fields.Many2one("academic.class",string="Promoting To")



    current_session = fields.Selection(
        [("2020","2020"),("2021", "2021"),("2022","2022")] ,string ="current_session")

    next_session = fields.Selection(
        [("2020", "2020"), ("2021", "2021"), ("2022", "2022")], string="next_session")

    def promoting_students(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Promotion',
            'res_model': 'exam.managepromotion',
            'view_mode': 'form',
            'target': 'new',

        }

    def manage_promotion(self):
        domain = []
        if self.class_name:
            domain.append(('class_name', '=', self.class_name.id))
        # if self.class_name1:
        #     domain.append(('class_name1', '=', self.class_name1))
        # if self.current_session:
        #     domain.append(('current_session', '=', self.current_session))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Students',
            'res_model': 'exam.managepromotion',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }
