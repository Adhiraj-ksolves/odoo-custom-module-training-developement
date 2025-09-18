from odoo import models, fields

class Fees(models.Model):
    _name = "school.management.fees"
    _description = "Fees data"
    _rec_name = "student_id"

    student_id = fields.Many2one('school.management.student', string="Student", required=True)
    amount = fields.Float(string="Amount", required=True)
    due_date = fields.Date(string="Due Date")
    paid = fields.Boolean(string="Paid", default=False)


