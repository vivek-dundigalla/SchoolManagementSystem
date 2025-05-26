from odoo import models, fields, api
from datetime import datetime


class SchoolDashboard(models.Model):
    _name = 'school.dashboard'
    _description = 'School Dashboard'

    GROUP_SELECTION = [
        ('student', 'Students'),
        ('attendance', 'Attendance'),
        ('teacher', 'Teachers'),
        ('parent', 'Parents'),
        ('driver', 'Drivers'),
        ('event', 'Events'),
    ]

    name = fields.Char(string='Group Name', readonly=True)
    group_type = fields.Selection(GROUP_SELECTION, required=True, readonly=True)
    count = fields.Integer(string='Count', compute="_compute_count", store=True)

    student_count = fields.Integer("Total Students", compute="_compute_counts", store=True)
    teacher_count = fields.Integer("Total Teachers", compute="_compute_counts", store=True)
    parent_count = fields.Integer("Total Parents", compute="_compute_counts", store=True)
    driver_count = fields.Integer("Total Drivers", compute="_compute_counts", store=True)

    upcoming_event_ids = fields.Text(string="Upcoming Events", compute="_compute_upcoming_event_ids")

    upcoming_events_display = fields.Html(string="Upcoming Events", compute='_compute_upcoming_events')
    upcoming_event_list = fields.Text(compute='_compute_upcoming_event_list')

    # Total present and absent counts
    count = fields.Integer("Count", compute="_compute_count", store=True)
    present_count = fields.Integer("Total Present", compute="_compute_attendance_counts", store=True)
    absent_count = fields.Integer("Total Absent", compute="_compute_attendance_counts", store=True)

    @api.depends('group_type')
    def _compute_count(self):
        for record in self:
            if record.group_type == 'student':
                record.count = self.env['school.student'].search_count([])
            elif record.group_type == 'teacher':
                record.count = self.env['hr.employee'].search_count([])
            elif record.group_type == 'parent':
                record.count = self.env['users.parents'].search_count([])
            elif record.group_type == 'driver':
                record.count = self.env['school.drivers'].search_count([])
            elif record.group_type == 'event':
                record.count = self.env['users.events'].search_count([('from_date', '>=', fields.Datetime.now())])

    @api.depends()
    def _compute_counts(self):
        for record in self:
            record.student_count = self.env['school.student'].search_count([])
            record.teacher_count = self.env['hr.employee'].search_count([])
            record.parent_count = self.env['users.parents'].search_count([])
            record.driver_count = self.env['school.drivers'].search_count([])

    # @api.depends()
    # def _compute_upcoming_events(self):
    #     for record in self:
    #         today = datetime.today().date()
    #         events = self.env['users.events'].search([
    #             ('from_date', '>=', today)
    #         ], order='from_date asc', limit=5)
    #         record.upcoming_event_ids = events

    @api.depends('group_type')
    def _compute_upcoming_events(self):
        for rec in self:
            if rec.group_type == 'event':
                events = self.env['users.events'].search(
                    [('from_date', '>=', fields.Datetime.now())],
                    order='from_date asc', limit=5
                )
                html = "<ul>"
                for event in events:
                    html += f"<li>{event.event_name} - {event.from_date.strftime('%m/%d/%Y %H:%M')}</li>"
                html += "</ul>" if events else "<p>No upcoming events</p>"
                rec.upcoming_events_display = html
            else:
                rec.upcoming_events_display = ""


    @api.depends('group_type')
    def _compute_upcoming_event_list(self):
        for rec in self:
            if rec.group_type == 'event':
                events = self.env['users.events'].search(
                    [('from_date', '>=', fields.Datetime.now())],
                    order='from_date asc',
                    limit=5
                )
                lines = []
                for event in events:
                    date_str = fields.Datetime.to_string(event.from_date)
                    lines.append(f"{event.event_name} - {date_str}")
                rec.upcoming_event_list = '\n'.join(lines)
            else:
                rec.upcoming_event_list = ''

    @api.depends()
    def _compute_upcoming_event_ids(self):
        for rec in self:
            upcoming_events = self.env['users.events'].search([
                ('from_date', '>=', fields.Datetime.now())
            ], order='from_date asc', limit=5)
            formatted = "\n".join(
                f"{e.event_name} - {e.from_date.strftime('%d-%m-%Y %H:%M')}"
                for e in upcoming_events
            )
            rec.upcoming_event_ids = formatted

    @api.depends('group_type')
    def _compute_attendance_counts(self):
        for rec in self:
            if rec.group_type == 'attendance':
                present = self.env['academic.takeattendance'].search_count([('attendance', '=', 'Present')])
                absent = self.env['academic.takeattendance'].search_count([('attendance', '=', 'Absent')])
                rec.present_count = present
                rec.absent_count = absent
            else:
                rec.present_count = 0
                rec.absent_count = 0



    @api.depends('group_type')
    def _compute_attendance_counts(self):
        for rec in self:
            if rec.group_type == 'attendance':
                rec.present_count = self.env['academic.takeattendance'].search_count([('attendance', '=', 'Present')])
                rec.absent_count = self.env['academic.takeattendance'].search_count([('attendance', '=', 'Absent')])
            else:
                rec.present_count = 0
                rec.absent_count = 0

