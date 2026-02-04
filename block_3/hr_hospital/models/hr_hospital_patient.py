from odoo import models, fields


class HRHPatient(models.Model):
    _name = 'hr.hospital.patient'
    _description = 'Patient'
    _inherit = ["hr.hospital.abstract.person"]

    doctor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Main Doctor',
    )

    passport_data = fields.Char(size=10)

    contact_person_id = fields.Many2one(
        comodel_name='hr.hospital.contact.person',
        string='Contact Person',
    )

    blood_group = fields.Selection(
        selection=[
            ('O_I_pos', 'O(I) Rh+'),
            ('O_I_neg', 'O(I) Rh-'),
            ('A_II_pos', 'A(II) Rh+'),
            ('A_II_neg', 'A(II) Rh-'),
            ('B_III_pos', 'B(III) Rh+'),
            ('B_III_neg', 'B(III) Rh-'),
            ('AB_IV_pos', 'AB(IV) Rh+'),
            ('AB_IV_neg', 'AB(IV) Rh-'),
        ],
    )

    allergies = fields.Text()

    insurance_company_id = fields.Many2one(
        comodel_name='res.partner',
        string='Insurance Company',
        domain=[('is_company', '=', True)],
        ondelete='restrict',
    )

    insurance_policy_number = fields.Char()

    doctor_history_ids = fields.One2many(
        comodel_name='hr.hospital.patient.doctor.history',
        inverse_name='patient_id',
        string='Doctor History',
    )
