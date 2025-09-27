from odoo import fields, models

class Seminar(models.Model):
    _name = 'seminar.seminar'
    _description = 'Seminario'

    name = fields.Char(string='Nombre del Seminario', required=True)
    date = fields.Date(string='Fecha del Seminario', required=True)
    location = fields.Char(string='Ubicación')
    description = fields.Html(string='Descripción Detallada')
    registration_ids = fields.One2many('seminar.registration', 'seminar_id', string='Inscripciones')