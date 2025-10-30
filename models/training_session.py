from odoo import models, fields

class TrainingSession(models.Model):
    _name = 'training.session'
    _description = 'Session de formation'

    name = fields.Char(string='Nom de la session', required=True)
    start_date = fields.Date(string='Date de début', required=True)
    end_date = fields.Date(string='Date de fin', required=True)
    seats = fields.Integer(string='Nombre de palces limite', required=True)