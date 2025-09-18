from odoo import models, fields

class Subject(models.Model):
    _name = "school.management.subject"
    _description = "Subject Data"

    name = fields.Char(string="Subject Name", required=True)

