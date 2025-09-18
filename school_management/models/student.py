from odoo import api, models, fields
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "school.management.student"
    _description = "Student Data"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    roll_no = fields.Integer(string="Roll Number")
    gender = fields.Selection([('male', 'Male'),('female', 'Female'),('others', 'Others')], string="Gender")
    section = fields.Char(string="Section")
    father_name = fields.Char(string="Father Name")
    unique_student = fields.Char(string="Student ID",default="New")

    teacher_ids = fields.Many2many("school.management.teacher",string="Teachers")
    class_id = fields.Many2one("school.management.clas", string="Class")
    subject_ids = fields.Many2many('school.management.subject',compute='_compute_automatic_subject_according_to_teacher',string="Subjects")

    @api.depends('teacher_ids.subject_ids')
    def _compute_automatic_subject_according_to_teacher(self):
        for student in self:
            subjects = student.teacher_ids.mapped('subject_ids')
            # name = student.name
            # print("Subject are: ", subjects, name)
            student.subject_ids = subjects

    @api.onchange('class_id')
    def _change_section(self):
        for student in self:
            if student.class_id.name == 'IT':
                student.section = 'IT-1'
            elif student.class_id.name == 'CS':
                student.section = 'CS-1'
            else:
                student.section = 'Not Assigned'
            print("Your Record are: ",student.class_id,student.class_id.name,student.section)

    @api.constrains('age')
    def _validate_age(self):
        for student in self:
            if student.age < 18:
                raise ValidationError('Age not appropriate, Must be 18+!')


    _sql_constraints = [
        ('unique_name', 'unique(roll_no)', 'Roll_No already Exist')
    ]
