from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

valid_email_regex = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
valid_phone_regex = re.compile(r"^\+?\d{7,15}$")

class HRHPerson(models.AbstractModel):
    _name = "hr.hospital.abstract.person"
    _description = "Abstract Person"
    _inherit = ["image.mixin"]

    last_name = fields.Char(required=True)
    first_name = fields.Char(required=True)
    middle_name = fields.Char()

    phone = fields.Char()
    email = fields.Char()

    gender = fields.Selection(
        selection=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ],
        required=True,
    )

    birth_date = fields.Date(
        string="Date of birth",
        required=True,
    )

    age = fields.Integer(
        compute="_compute_age",
        store=True,
        readonly=True,
    )

    full_name = fields.Char(
        string="Повне ім'я",
        compute="_compute_full_name",
        store=True,
        readonly=True,
    )

    country_id = fields.Many2one(
        comodel_name="res.country",
        string="Country",
    )

    language_id = fields.Many2one(
        comodel_name="res.lang",
        string="Language",
    )

    @api.depends("last_name", "first_name", "middle_name")
    def _compute_full_name(self):
        for rec in self:
            parts = [rec.last_name, rec.first_name, rec.middle_name]
            rec.full_name = " ".join([p.strip() for p in parts if p and p.strip()])

    @api.depends("birth_date")
    def _compute_age(self):
        today = fields.Date.today()
        for rec in self:
            if not rec.birth_date:
                rec.age = 0
                continue
            b = rec.birth_date
            if isinstance(b, str):
                b = fields.Date.from_string(b)
            years = today.year - b.year
            if (today.month, today.day) < (b.month, b.day):
                years -= 1
            rec.age = max(years, 0)

    @api.constrains("email")
    def _check_email(self):
        for rec in self:
            if rec.email and not valid_email_regex.match(rec.email.strip()):
                raise ValidationError("Incorrect Email format: %s" % rec.email)

    @api.constrains("phone")
    def _check_phone(self):
        for rec in self:
            if rec.phone:
                p = rec.phone.strip().replace(" ", "").replace("-", "")
                if not valid_phone_regex.match(p):
                    raise ValidationError(
                        "Incorrect phone format (expected 7-15 digits, optional with '+'): %s"
                        % rec.phone
                    )
