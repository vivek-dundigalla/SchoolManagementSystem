from odoo import models, fields

class Attendance(models.Model):
    _name = 'academic.attendance'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "month"# ✅ Add this


    # class_name = fields.Selection([
    #     ('class one', 'Class One'),
    #     ('class two', 'Class Two'),
    #     ('class three', 'clas Three')
    # ], string='Class')
    month=fields.Selection([("January","January"),
                            ("Febraury","Febraury"),
                            ("March","March"),
                            ("April","April"),
                            ("May","May"),
                            ("June","June"),
                            ("July","July"),
                            ("August","August"),
                            ("September","September"),
                            ("October","October"),
                            ("November","November"),
                            ("December","December")],string="Month")
    year=fields.Selection([("1","2019"),("2","2020"),("3","2021"),("4","2022"),("5","2023"),("6","2024"),("7","2025")],string="Year")
    class2=fields.Many2one("academic.class","Class")
    section = fields.Selection(
        [("A","A"),("B", "B"),("C","C")] ,string ="Section")

    def take_attendance(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Attendance',
            'res_model': 'academic.takeattendance',
            'view_mode': 'form',
            'target': 'new',

        }

    # def filter_syllabus(self):
    #     domain = []
    #     if self.class_namess:
    #         domain.append(('class_names', '=', self.class_names))
    #     if self.section:
    #         domain.append(('section', '=', self.section))

    def filter_attendance(self):
        # Check if 'default_class_name' is in the context
        class_namess = self.env.context.get('default_class_namess')
        domain = []
        if class_namess:
            domain.append(('class2', '=', class_namess))  # Filter by class_name in 'academic.subject'

        return {
        'type': 'ir.actions.act_window',
        'name': 'Filtered Attendance',
        'res_model': 'academic.takeattendance',
        'view_mode': 'list',
        'domain': domain,
        'target': 'current',
    }