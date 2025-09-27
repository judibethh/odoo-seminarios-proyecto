from odoo import fields, models

class Registration(models.Model):
    _name = 'seminar.registration'
    _description = 'Inscripción a Seminario'

    seminar_id = fields.Many2one('seminar.seminar', string='Seminario', required=True)
    contact_id = fields.Many2one('res.partner', string='Contacto', required=True)
    registration_date = fields.Datetime(string='Fecha de Inscripción', default=fields.Datetime.now)
    attended = fields.Boolean(string='Asistió', default=False)