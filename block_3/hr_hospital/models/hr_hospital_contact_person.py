from odoo import models, fields


class HRHContactPerson(models.Model):
    _name = 'hr.hospital.contact.person'
    _description = 'Contact Person'
    _inherit = ["hr.hospital.abstract.person"]
