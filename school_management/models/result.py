from odoo import api, models, fields


class StudentExamResult(models.Model):
    _name = "student.management.result"
    _description = "Student Exam Result"

    subject_id = fields.Many2one("school.management.subject", string="Subject")
    marks = fields.Integer(string="Marks out of 100")
    student_id = fields.Many2one("school.management.student", string="Student")
