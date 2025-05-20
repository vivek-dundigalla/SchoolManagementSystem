from odoo import models, fields, api

class send_exam_marks(models.Model):
    _name = "send.marks"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "exam"

    company_id = fields.Many2one(
        'res.company', string='Company',
        default=lambda self: self.env.company, readonly=True
    )

    exam = fields.Selection([
        ("First Term Exam", "First Term Exam"),
        ("Second Term Exam", "Second Term Exam"),
        ("Model Test Exam", "Model Test Exam"),
        ("Final Exam", "Final Exam"),
    ], string="Select a Exam",  tracking=True)

    select_class = fields.Many2one("academic.class", store=True,string="Select a Class")

    section_1 = fields.Selection([
        ("A","A"),
        ("B","B"),
        ("C","C")
    ], string="Select Section", tracking=True )

    receiver = fields.Selection([
        # ("Parent","Parent"),
        ("Student","Student")
    ], string="Select Receiver", tracking=True )

    parent = fields.Many2one(comodel_name="users.parents", string="Parents")
    student = fields.Many2one(comodel_name="school.student", string="students")
    marks = fields.Char(string="Marks",compute="get_marks")


    def send_marks(self):
        template = self.env.ref('SchoolManagementSystem.mail_template_receiver')
        if not template:
            return
        for record in self:
            template.send_mail(record.id, force_send=True)



    def get_marks(self):
        for rec in self:
            mark_details=self.env['exam.marksdetails'].search([('name','=',rec.student.id)])
            for i in mark_details:
                rec.marks = i.marks








