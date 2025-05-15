from odoo import models, fields,api

class AssignStudents(models.Model):
    _name = 'transport.assign'

    # class_name = fields.Selection([
    #     ('class one', 'Class One'),
    #     ('class two', 'Class Two'),
    #     ('class three', 'clas Three')
    # ], string='Class')

    category =fields.Selection([('driver','Driver'),('class','Class'),('vechicle','Vechicle')])
    vh_model = fields.Many2one('transport.vehicle', string="Vehicle")
    student_class_number = fields.Many2one('school.admission', string="Class")
    driver_name = fields.Many2one('school.drivers', string="Driver")

    show_vehicle = fields.Boolean(compute="_compute_visibility")
    show_class = fields.Boolean(compute="_compute_visibility")
    show_driver = fields.Boolean(compute="_compute_visibility")

    @api.depends('category')
    def _compute_visibility(self):
        for rec in self:
            rec.show_vehicle = rec.category == 'vehicle'
            rec.show_class = rec.category == 'class'
            rec.show_driver = rec.category == 'driver'

    def assign_student(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Assign Student',
            'res_model': 'transport.assignstudents',
            'view_mode': 'form',
            'target': 'new',

        }



    # def filter_subject(self):
    #     domain = []
    #     if self.standard_name:
    #         domain.append(('standard_name', '=', self.standard_name))
    #
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Filtered Subjects',
    #         'res_model': 'academic.subjectlines',
    #         'view_mode': 'list',
    #         'domain': domain,
    #         'target': 'current',
    #     }
