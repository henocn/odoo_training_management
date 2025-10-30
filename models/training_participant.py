from odoo import fields, models


class TrainingParticipant(models.Model):
    _name = 'training.participant'
    _description = 'Participants'

    name = fields.Char(string="Nom et prénom", required=True)
    email = fields.Char(string="Email")
    contact = fields.Char(string="Contact")
    session_id = fields.Many2one('training.session', string="Session", ondelete='cascade')
    