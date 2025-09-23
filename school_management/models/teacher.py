from odoo import api, models, fields


class Teacher(models.Model):
    _name = 'school.management.teacher'
    _description = 'School Teacher'

    name = fields.Char(string="Name")
    subject = fields.Char(string="Subject")
    phone_no = fields.Integer(string="Phone Number")
    age = fields.Integer(string="Age")
    gender = fields.Selection([('male', 'Male'),('female', 'Female'),('others', 'Others')], string="Gender")
    male_count = fields.Integer(string="MALE COUNT", compute="_count_gender")
    female_count = fields.Integer(string="FEMALE COUNT", compute="_count_gender")
    state = fields.Selection([('active', 'Active'),('on_leave', 'On Leave'),('retired', 'Retired'),], string="Status", default='active')

    student_ids = fields.Many2many('school.management.student',string="Students")
    user_id = fields.Many2one('res.users', string="Related User")
    subject_ids = fields.Many2many('school.management.subject', string="Subjects")


    @api.depends('student_ids.gender')
    def _count_gender(self):
        for teacher in self:
            male_students = teacher.student_ids.filtered(lambda s: s.gender == 'male')
            female_students = teacher.student_ids.filtered(lambda s: s.gender == 'female')
            teacher.male_count = len(male_students)
            teacher.female_count = len(female_students)
            print(teacher.male_count, teacher.female_count)


