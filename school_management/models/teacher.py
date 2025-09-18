from odoo import models, fields


class Teacher(models.Model):
    _name = 'school.management.teacher'
    _description = 'School Teacher'

    name = fields.Char(string="Name", required=True)
    subject = fields.Char(string="Subject", required=True)
    phone_no = fields.Integer(string="Phone Number")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'),('female', 'Female'),('others', 'Others')], string="Gender")

    student_ids = fields.Many2many('school.management.student',string="Students")
    user_id = fields.Many2one('res.users', string="Related User")
    subject_ids = fields.Many2many('school.management.subject', string="Subjects")
