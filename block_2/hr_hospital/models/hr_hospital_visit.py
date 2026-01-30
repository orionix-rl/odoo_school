from odoo import models, fields

class HRHVisit(models.Model):
    _name = 'hr.hospital.visit'
    _description = 'Visit'

    date = fields.Date()
    time = fields.Float()

    doctor_id = fields.Many2one(
        comodel_name = 'hr.hospital.doctor',
        string = 'Doctor'
    )

    patient_id = fields.Many2one(
        comodel_name = 'hr.hospital.patient',
        string = 'Patient'
    )

    disease_ids = fields.Many2many(
        comodel_name = 'hr.hospital.disease',
        relation='hr_hospital_visit_disease_rel',
        string = 'Disease'
    )

    note = fields.Text()
