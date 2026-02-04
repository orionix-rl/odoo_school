from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HRHDoctor(models.Model):
    _name = 'hr.hospital.doctor'
    _description = 'Doctor'
    _inherit = ["hr.hospital.abstract.person"]

    visit_ids = fields.One2many(
        comodel_name='hr.hospital.visit',
        inverse_name='doctor_id',
        string='Visits'
    )

    user_id = fields.Many2one(
        comodel_name='res.users',
        string='User',
    )

    specialty_id = fields.Many2one(
        comodel_name='hr.hospital.doctor.specialty',
        string='Specialty',
    )

    is_intern = fields.Boolean(string='Intern')

    mentor_id = fields.Many2one(
        comodel_name='hr.hospital.doctor',
        string='Mentor',
    )

    license_number = fields.Char(
        required=True,
        copy=False,
    )

    license_date = fields.Date(string='License Issue Date')

    experience_years = fields.Integer(
        string='Experience (Years)',
        compute='_compute_experience_years',
        readonly=True,
    )

    rating = fields.Float(
        digits=(3, 2),
        default=0,
    )

    schedule_ids = fields.One2many(
        comodel_name='hr.hospital.doctor.schedule',
        inverse_name='doctor_id',
        string='Schedule',
    )

    education_country_id = fields.Many2one(
        comodel_name='res.country',
        string='Education Country',
    )

    @api.depends('license_date')
    def _compute_experience_years(self):
        today = fields.Date.today()
        for rec in self:
            if not rec.license_date:
                rec.experience_years = 0
                continue
            d = rec.license_date
            years = today.year - d.year
            if (today.month, today.day) < (d.month, d.day):
                years -= 1
            rec.experience_years = max(years, 0)

    @api.onchange('is_intern')
    def _onchange_is_intern(self):
        if not self.is_intern:
            self.mentor_id = False

    @api.constrains('is_intern', 'mentor_id')
    def _check_mentor_for_interns_only(self):
        for rec in self:
            if not rec.is_intern and rec.mentor_id:
                raise ValidationError("Mentor Doctor can be set only for interns.")

    @api.constrains('rating')
    def _check_rating_range(self):
        for rec in self:
            if rec.rating is not False and (rec.rating < 0.0 or rec.rating > 5.0):
                raise ValidationError("Rating must be between 0.00 and 5.00.")
