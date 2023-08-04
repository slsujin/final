from django.db import models
from datetime import datetime



# Create your models here.
class store(models.Model):
    gender_choice=(('M','Male'),('F','Female'))
    purpose_choice=(('enquiry','enquiry'),
             ('place order','place order'),
             ('return','return'),
             ('rating','rating'))

    materials_choice = (('book', 'Book'),
                      (' pen', 'Pen'),
                      ('pencil', 'Pencil'),
                      ('exam papper', 'Exam papper'),
                      ('chart papper', 'Chart papper'),
                      ('instrument box', 'Instrument box'))


    # department_choice=(('maths biology','Maths Biology'),
    #                    ('computer science,''Computer Science'),
    #                    ('commerce','Commerce'),
    #                    ('humanities','Humanities'),
    #                    ('electronics','Electronics'),
    #                    ('statstics','Statstics'))

    name=models.CharField(max_length=250)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=1,choices=gender_choice,default=None)
    phone=models.BigIntegerField(null=True)
    email=models.EmailField(default=None)
    address=models.TextField(max_length=250)
    department=models.CharField(max_length=20,null=True)
    course = models.CharField(max_length=20, null=True)
    purpose = models.CharField(max_length=20, choices=purpose_choice, default=None)
    materials=models.CharField(max_length=100,null=True)




    def __str__(self):
        return self.name








