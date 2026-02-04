from odoo import models, fields, api


class HRHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit'

    status = fields.Selection(
        selection=[
            ('planned', 'Planned'),
            ('done', 'Done'),
            ('cancelled', 'Cancelled'),
            ('no_show', "No show up"),
        ],
        default='planned',
        required=True,
    )

    planned_datetime = fields.Datetime(string='Planned Date & Time', required=True)
    actual_datetime = fields.Datetime(string='Actual Date & Time')

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
        required=True,
    )

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
        required=True,
    )

    visit_type = fields.Selection(
        selection=[
            ('primary', 'Primary'),
            ('followup', 'Followup'),
            ('preventive', 'Preventive'),
            ('urgent', 'Urgent'),
        ],
        default='primary',
        required=True,
    )

    diagnosis_ids = fields.One2many(
        comodel_name='hr.hospital.visit.diagnosis',
        inverse_name='visit_id',
        string='Diagnoses',
    )

    recommendations = fields.Html()

    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Currency',
        required=True,
    )

    amount = fields.Monetary(
        string='Visit Cost',
        currency_field='currency_id',
    )

    @api.onchange('status')
    def _onchange_state(self):
        if self.state != 'done':
            self.actual_datetime = False
