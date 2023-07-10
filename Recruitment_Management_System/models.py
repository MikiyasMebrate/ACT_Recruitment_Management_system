from django.db import models
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


#Candidate
gender_list = [
    ('male', 'Male'),
    ('female', 'Female'),
]

class Candidate(models.Model):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=gender_list)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=40)
    phone1 = PhoneNumberField()
    phone2 = PhoneNumberField(blank = True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='Candidate/photo', null=True, blank=True)
    resume = models.FileField(upload_to='Candidate/Resume', null=True, blank=True)
    about = models.TextField()
    skill = models.ManyToManyField("Skill") 
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

education_status_list = [
    ('highschool', 'High School'),
    ('Certificate', 'Certificate'),
    ('diploma', 'Diploma'),
    ('bachelor-degree', "Bachelor's degree"),
    ('Master-degree', "Master's Degree"),
    ('doctorate', "Doctorate"),
    ('other', 'Other')
]
class Education(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    education_status = models.CharField(
        max_length=40, choices=education_status_list)
    field_of_study = models.CharField(max_length=40)
    education_period_start = models.DateField()
    education_period_end = models.DateField()

    def __str__(self) -> str:
        return self.institution_name

class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(max_length=40)
    work_time_line_start =models.DateField()
    work_time_line_end = models.DateField()
    job_title = models.CharField(max_length=50)
    reference_phone = PhoneNumberField()
    reference_name = models.CharField(max_length=40)
    reference_email = models.CharField(max_length=40)
    reference_job_title = models.CharField(max_length=40)
    responsibility = models.TextField()

    def __str__(self) -> str:
        return self.company_name

class Skill(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']
   
    def __str__(self) -> str:
        return self.title
    
class Social_media(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    link = models.CharField(max_length=70, null=True, blank=True)
    candidate = models.ForeignKey(
        Candidate, on_delete=models.CASCADE)  # Related With Candidate

    def __str__(self) -> str:
        return self.name

class Bookmarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobs = models.ForeignKey('Job_Posting', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.jobs


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Job_Type(models.Model):
    type = models.CharField(max_length=20)  # Full Time, Part Time, Freelance

    def __str__(self) -> str:
        return self.type

class Job_Posting(models.Model):
    title = models.CharField(max_length=50)
    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True)  # Related With Department
    description = models.TextField()  # HTML Editor
    experience = models.IntegerField()
    location = models.CharField(max_length=50)
    salary_range = models.CharField(max_length=20)
    # Related With Job_Type
    type = models.ForeignKey(Job_Type, on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateField()

    def __str__(self) -> str:
        return self.title

application_status = [
    ('new', 'new'),
    ('in_review', 'in review'),
    ('rejected', 'rejected'),
    ('hired', 'hired')
]

class Application(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.SET_NULL, null=True)  # Related with Candidate
    # Related with Job_Post
    job = models.ForeignKey(Job_Posting, on_delete=models.SET_NULL, null=True)
    date_applied = models.DateField(auto_now_add=True)
    # Select Option from application_status
    status = models.CharField(max_length=15, choices=application_status)

    def __str__(self) -> str:
        return self.candidate+" "+self.job

interview_status = [
    ('scheduled', 'scheduled'),
    ('completed', 'completed'),
    ('canceled', 'canceled'),
]

interview_type = [
    ('phone', 'phone'),
    ('in-person', 'in-person'),
    ('video', 'video')
]

class Interviews(models.Model):
    candidate = models.ForeignKey(
        Candidate, on_delete=models.SET_NULL, null=True)  # Related Wih Candidate
    # Related with Job_Post
    job = models.ForeignKey(Job_Posting, on_delete=models.SET_NULL, null=True)
    interviewer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)  # Related with User
    date_schedule = models.DateField()
    time_schedule = models.TimeField()
    status = models.CharField(max_length=15, choices=interview_status)
    # feedback
    type = models.CharField(max_length=15, choices=interview_type)

    def __str__(self) -> str:
        return self.candidate + " Interviewer: " + self.interviewer

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    candidate = models.ForeignKey(
        Candidate, on_delete=models.SET_NULL, null=True)
    content = models.TextField()  # HTML Editor
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.candidate
