from odoo import models, fields

class TrainingCourse(models.Model):

    levels = [("beginner", "Débutant"),
              ("intermediate", "Intermédiaire"),
              ("advanced", "Avancé")
            ]
    
    _name = "training.course"
    _description = "Formation"

    name = fields.Char(string = "Titre de la formation", required=True)
    description = fields.Text(string="Descripmtion")
    duration = fields.Integer(string="Durée en heures ")
    level = fields.Selection(levels, string="Niveau", default='beginner')