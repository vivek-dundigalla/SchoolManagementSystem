from odoo import models, fields,api

class AssignStudents(models.Model):
    _name = 'transport.assign'

    # class_name = fields.Selection([
    #     ('class one', 'Class One'),
    #     ('class two', 'Class Two'),
    #     ('class three', 'clas Three')
    # ], string='Class')

    category =fields.Selection([('driver','Driver'),('class','Class'),('vehicle','Vehicle')],string='category')
    vh_model = fields.Many2one('transport.vechicle', string="Vehicle")
    student_class_number = fields.Many2one('academic.class', string="Class")
    driver_name = fields.Many2one('school.drivers', string="Driver")



    #
    # @api.onchange('category')
    # def onchange(self):
    #     for rec in self:
    #         if rec.category=='driver':



    def assign_student(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Assign Student',
            'res_model': 'transport.assignstudents',
            'view_mode': 'form',
            'target': 'new',

        }



    # def filter(self):
    #     domain = []
    #     if self.vh_model:
    #         domain.append(('vh_model', '=', self.vh_model.id))
    #     if self.student_class_number:
    #         domain.append(('student_class_number', '=', self.student_class_number.id))
    #     if self.driver_name:
    #         domain.append(('driver_name', '=', self.driver_name.id))
    #
    #     return {
    #         'type': 'ir.actions.act_window',
    #         'name': 'Filtered list',
    #         'res_model': 'transport.assignstudents',
    #         'view_mode': 'list',
    #         'domain': domain,
    #         'target': 'current',
    #     }

    def filter(self):
        for rec in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Filtered Marks',
                'res_model': 'transport.assignstudents',
                'view_mode': 'list,form',
                'domain': [('vh_model', '=', rec.vh_model.id),('student_class_number', '=', rec.student_class_number.id),('driver_name', '=', rec.driver_name.id)],
                'target': 'new',
            }

