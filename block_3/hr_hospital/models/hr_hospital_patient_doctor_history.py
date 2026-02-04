from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PatientDoctorHistory(models.Model):
    _name = 'patient.doctor.history'
    _description = 'Patient Doctor History'
    _order = 'date_from desc, id desc'

    patient_id = fields.Many2one(
        comodel_name='hr.hospital.patient',
        string='Patient',
        required=True,
    )

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Doctor',
        required=True,
    )

    date_from = fields.Date(
        string='Assignment Date',
        required=True,
        default=fields.Date.today(),
    )

    date_to = fields.Date(
        string='Change Date',
    )

    change_reason = fields.Text(
        string='Change Reason',
    )

    active = fields.Boolean(
        default=True,
    )

    @api.constrains('date_from', 'date_to')
    def _check_dates(self):
        for rec in self:
            if rec.date_to and rec.date_to < rec.date_from:
                raise ValidationError("Change Date cannot be earlier than Assignment Date.")

    @api.constrains('active', 'date_to')
    def _check_active_consistency(self):
        for rec in self:
            if rec.active and rec.date_to:
                raise ValidationError("Active history record must not have a Change Date.")
