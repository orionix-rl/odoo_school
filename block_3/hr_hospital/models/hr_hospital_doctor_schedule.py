from odoo import api, fields, models
from odoo.exceptions import ValidationError


class DoctorSchedule(models.Model):
    _name = 'doctor.schedule'
    _description = 'Doctor Schedule'

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
        required=True,
    )

    day_of_week = fields.Selection(
        selection=[
            ('mon', 'Monday'),
            ('tue', 'Tuesday'),
            ('wed', 'Wednesday'),
            ('thu', 'Thursday'),
            ('fri', 'Friday'),
            ('sat', 'Saturday'),
            ('sun', 'Sunday'),
        ]
    )

    date = fields.Date()

    time_from = fields.Float(string='Start Time')

    time_to = fields.Float(string='End Time')

    schedule_type = fields.Selection(
        selection=[
            ('workday', 'Work Day'),
            ('vacation', 'Vacation'),
            ('sick', 'Sick Leave'),
            ('conference', 'Conference'),
        ],
        string='Type',
    )

    note = fields.Char(string='Notes')
