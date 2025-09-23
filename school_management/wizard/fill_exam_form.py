from odoo import models, fields


class FillExamForm(models.TransientModel):
    _name = "student.fill.exam.form.wizard"
    _description = "Wizard for Filling Exam Form"

    student_id = fields.Many2one('school.management.student', string="Student")
    subject_id = fields.Many2one('school.management.subject', string="Subject")
    marks = fields.Integer(string="Marks (out of 100)", default=100)

    def action_confirm(self):
        self.env['student.management.result'].create({
            'student_id': self.student_id.id,
            'subject_id': self.subject_id.id,
            'marks': self.marks,
        })
