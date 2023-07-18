from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from froala_editor.fields import FroalaField
from Account.models import CustomUser
#Candidate
gender_list = [
    ('male', 'Male'),
    ('female', 'Female'),
]

class Candidate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=gender_list)
    date_of_birth = models.DateField()
    email = models.EmailField(max_length=40)
    phone1 = PhoneNumberField()
    phone2 = PhoneNumberField(blank = True)
    address = models.CharField(max_length=100)
    linked_in = models.URLField(blank=True, null=True)
    git_hub = models.URLField(blank=True, null=True)
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    photo = models.ImageField(upload_to='Candidate/photo', null=True, blank=True)
    resume = models.FileField(upload_to='Candidate/Resume', null=True, blank=True)
    about = models.TextField()
    skill = models.ManyToManyField("Skill", blank=False) 
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
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=100)
    education_status = models.CharField(
        max_length=40, choices=education_status_list)
    field_of_study = models.CharField(max_length=40)
    education_period_start = models.DateField()
    education_period_end = models.DateField()

    def __str__(self) -> str:
        return self.institution_name

class Experience(models.Model):
    candidate = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    company_name = models.CharField(max_length=40)
    work_time_line_start =models.DateField()
    work_time_line_end = models.DateField()
    job_title = models.CharField(max_length=50)
    reference_phone = PhoneNumberField()
    reference_name = models.CharField(max_length=40)
    reference_email = models.CharField(max_length=40)
    reference_job_title = models.CharField(max_length=40)
    responsibility = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.company_name

class Skill(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']
   
    def __str__(self) -> str:
        return self.title
    
class Bookmarks(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    jobs = models.ForeignKey('Job_Posting', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.jobs



class Sector(models.Model):
    name = models.CharField(max_length=50)

    def count_job_post(self) :
        count = Job_Posting.objects.filter(sector_id = self.id).count()
        return count

    def __str__(self) -> str:
        return self.name

class Job_Type(models.Model):
    type = models.CharField(max_length=20)  # Full Time, Part Time, Freelance

    def __str__(self) -> str:
        return self.type


job_type = [
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('freelance', 'Freelance'),
    ('internship', 'Internship'),
    ('seasonal ','seasonal'),
    ('contract', 'Contract'),
    ('remote', 'Remote'),
]



class Job_Posting(models.Model):
    title = models.CharField(max_length=50)
    sector = models.ForeignKey(Sector, on_delete=models.SET_NULL, null=True)  # Related With Sector
    description = FroalaField()
    vacancies = models.IntegerField()
    experience = models.CharField(max_length=20)
    skills = models.ManyToManyField(Skill)
    location = models.CharField(max_length=200)
    salary_range_start = models.FloatField()
    salary_range_final = models.FloatField()
    type = models.CharField( choices=job_type, max_length=30)
    job_status = models.BooleanField(default=False)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateField()
  
    class Meta:
        ordering = ['-date_posted','-date_closed']

    def count_applicant(self) -> int:
        applicant = Application.objects.filter(job__id = self.id).count()
        return applicant

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

job_status_interview = [
    ('rejected', 'Rejected'),
    ('hired', 'hired'),
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
    interviewer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)  # Related with User
    date_schedule = models.DateField()
    time_schedule = models.TimeField()
    status = models.CharField(max_length=15, choices=interview_status)
    job_status = models.CharField(max_length=25, choices=job_status_interview)
    # feedback
    type = models.CharField(max_length=15, choices=interview_type)

    def __str__(self) -> str:
        return self.candidate + " Interviewer: " + self.interviewer

class Notes(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    candidate = models.ForeignKey(
        Candidate, on_delete=models.SET_NULL, null=True)
    content = models.TextField()  # HTML Editor
    date_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.candidate
