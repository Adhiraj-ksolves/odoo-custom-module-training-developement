from odoo import models, fields

class SchoolClass(models.Model):
    _name = "school.management.clas"
    _description = "Class data"

    name = fields.Char(string="Name", required=True)
    section = fields.Char(string="Section")
    teacher_ids = fields.Many2one('school.management.teacher', string="Teacher")

    student_ids = fields.One2many('school.management.student', 'class_id', string="Students")

