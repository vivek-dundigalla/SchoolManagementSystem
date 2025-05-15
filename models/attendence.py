from odoo import models, fields

class Promotion(models.Model):
    _name = 'academic.attendence'

    month = fields.Selection([
        ("January","January")
        ("february", "february")
        ("March", "March")
        ("April", "April")
        ("May", "May")
        ("June", "June")
        ("July", "July")
        ("August", "August")
        ("September", "September")
        ("October", "October")
        ("November", "November")
        ("December", "December")
    ])
    year = fields.Selection([
        ("2019", "2019")
        ("2020", "2020")
        ("2021", "2021")
        ("2022", "2022")
        ("2023", "2023")
        ("2024", "2024")
    ])
    class_name = fields.Many2one("academic.class",string="Class")



    section = fields.Selection(
        [("a","A"),("b", "B"),("c","C")] ,string ="section")


    def take_attendance(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Take Attendance',
            'res_model': 'academic.atendance',
            'view_mode': 'form',
            'target': 'new',

        }

    def filter_attendance(self):
        domain = []
        if self.class_name:
            domain.append(('class_name', '=', self.class_name.id))
        # if self.class_name1:
        #     domain.append(('class_name1', '=', self.class_name1))
        # if self.current_session:
        #     domain.append(('current_session', '=', self.current_session))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Attendance',
            'res_model': 'academic.attendance',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }
