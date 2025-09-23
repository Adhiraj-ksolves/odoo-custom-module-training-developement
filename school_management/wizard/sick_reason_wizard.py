from odoo import models, fields, api


class SickReasonWizard(models.TransientModel):
    _name = "student.sick.reason.wizard"
    _description = "Wizard for Sick Reason"

    sick_reason = fields.Text(string="Sick Reason")
    sick_date = fields.Date(string="Sick Date", default=fields.Date.today)
    guardian_contact = fields.Char(string="Guardian Contact")
    notes = fields.Text(string="Additional Notes")

    def action_confirm_reason(self):
        student_id = self.env.context.get('active_id')
        if student_id:
            student = self.env['school.management.student'].browse(student_id)
            student.sick_reason = self.sick_reason
            student.state = 'sick'

        return {'type': 'ir.actions.act_window_close'}
