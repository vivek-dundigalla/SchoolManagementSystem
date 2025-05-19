from odoo import models, fields

class SubjectLines(models.Model):
    _name = 'academic.subjectlines'

    # class_name = fields.Selection([
    #     ("Class Ten", "Class Ten"),
    #     ("Class Nine", "Class Nine"),
    #     ("Class Eight", "Class Eight"),
    #     ("Class Seven", "Class Seven"),
    #     ("Class Six", "Class Six"),
    #     ("Class Five", "Class Five"),
    #     ("Class Four", "Class Four"),
    #     ("Class Three", "Class Three"),
    #     ("Class Two", "Class Two"),
    #     ("Class One", "Class One")
    # ], string='Class')
    class_names=fields.Many2one("academic.class","Class")

    subject_ids = fields.Many2many('academic.subject', string='Subjects')

    def action_save_subject(self):
        return {'type': 'ir.actions.act_window_close'}

    def filter_subject(self):
        domain = []
        if self.class_names:  # Filter subjects based on the selected class_name
            domain.append(('standard_names', '=', self.class_name))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Subjects',
            'res_model': 'academic.subjectlines.line',
            'view_mode': 'list,form',
            'domain': domain,  # Show filtered subjects for the selected class
            'target': 'current',
        }

    def default_get(self, fields):
        res = super().default_get(fields)
        if 'default_class_names' in self.env.context:
            res['class_names'] = self.env.context['default_class_names']
        return res
