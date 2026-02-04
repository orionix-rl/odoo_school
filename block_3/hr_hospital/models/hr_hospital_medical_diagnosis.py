from odoo import api, fields, models
from odoo.exceptions import ValidationError


class MedicalDiagnosis(models.Model):
    _name = 'hr.hospital.medical.diagnosis'
    _description = 'Medical Diagnosis'

    visit_id = fields.Many2one(
        comodel_name='hr.hospital.visit',
        string='Visit',
        ondelete='cascade',
    )

    disease_id = fields.Many2one(
        comodel_name='hr.hospital.disease',
        string='Disease',
    )

    description = fields.Text()

    treatment_html = fields.Html(
        string='Prescribed Treatment'
    )

    severity = fields.Selection(
        selection=[
            ('mild', 'Mild'),
            ('moderate', 'Moderate'),
            ('severe', 'Severe'),
            ('critical', 'Critical'),
        ],
    )

    approved = fields.Boolean(
        default=False,
    )

    approved_by_doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Approved By',
        readonly=True,
    )

    approval_datetime = fields.Datetime(
        string='Approval Date',
        readonly=True,
        copy=False,
    )
