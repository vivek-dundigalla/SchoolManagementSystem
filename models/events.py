from odoo import models,fields,api
from datetime import date

class Events(models.Model):
    _name = "users.events"
    _rec_name = "event_name"

    upcoming_event_ids = fields.One2many(
        'users.events',
        compute='_compute_upcoming_events',
        string='Upcoming Events',
        store=False,
        readonly=True
    )

    event_image = fields.Binary(string="Photo")
    event_name = fields.Char( string="Event Title", tracking=True)
    from_date = fields.Datetime(string="Start")
    end_date= fields.Datetime(string="End")
    color = fields.Char(string="Color", size=7)

    def _compute_color_int(self):
        color_map = {
            '#f44336': 1,  # red
            '#e91e63': 2,  # pink
            '#9c27b0': 3,  # purple
            '#673ab7': 4,  # deep purple
            '#3f51b5': 5,  # indigo
            '#2196f3': 6,  # blue
            '#03a9f4': 7,  # light blue
            '#00bcd4': 8,  # cyan
            '#009688': 9,  # teal
            '#4caf50': 10,  # green
        }
        for event in self:
            event.color_int = color_map.get(event.color, 0)

