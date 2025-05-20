from odoo import models, fields,api

class AssignStudents(models.Model):
    _name = 'transport.assign'
    _rec_name = "category"

    category =fields.Selection([('driver','Driver'),('class','Class'),('vehicle','Vehicle')])
    # vh_model = fields.Many2one('transport.vehicle', string="Vehicle")

    vehicle_model = fields.Many2one('transport.vehiclemodel', string="Vehicle Model")
    student_class_number = fields.Many2one('academic.class', string="Class")
    driver_names_id = fields.Many2one('school.drivers', string="Driver")

    # show_vehicle = fields.Boolean(compute="_compute_visibility")
    # show_class = fields.Boolean(compute="_compute_visibility")
    # show_driver = fields.Boolean(compute="_compute_visibility")


    # @api.depends('category')
    # def _compute_visibility(self):
    #     for rec in self:
    #         rec.show_vehicle = rec.category == 'Vehicle'
    #         rec.show_class = rec.category == 'Class'
    #         rec.show_driver = rec.category == 'Driver'

    def assign_student(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Assign Student',
            'res_model': 'transport.assignstudents',
            'view_mode': 'form',
            'target': 'new',

        }

    def filter(self):
        domain = []
        if self.category == 'vehicle' and self.vehicle_model:
            domain.append(('vehicle_model', '=', self.vehicle_model.id))
        elif self.category == 'class' and self.student_class_number:
            domain.append(('student_class_number', '=', self.student_class_number.id))
        elif self.category == 'driver' and self.driver_names_id:
            domain.append(('driver_names_id', '=', self.driver_names_id.id))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Students',
            'res_model': 'transport.assignstudents',
            'view_mode': 'list',
            'domain': domain,
            'target': 'current',
        }
    # def filter(self):
    #     for rec in self:
    #         return {
    #             'type': 'ir.actions.act_window',
    #             'name':"ASSIGNED STUDENTS",
    #             'res_model': 'transport.assignstudents',
    #             'view_mode': 'list',
    #             'domain': [('vehicle_model', '=', rec.vehicle_model.id),('student_class_number', '=', rec.student_class_number.id),('driver_names_id','=',rec.driver_names_id.id)],
    #             'target': 'new',
    #         }



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
