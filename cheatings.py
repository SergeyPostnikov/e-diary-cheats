from django.core.exceptions import ObjectDoesNotExist
from datacenter.models import Mark, Chastisement, Schoolkid, Lesson, Commendation, Subject


def get_schoolkid(name):
    try:
        return Schoolkid.objects.filter(full_name__contains=name).get(id=1)
    except ObjectDoesNotExist as err:
        print(err)


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[3, 2])
    marks.update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(name, subject_title):
    try:
        student = Schoolkid.objects.filter(full_name__contains=name).get(id=1)
        subject = Subject.objects.filter(year_of_study=student.year_of_study, title=subject_title).get(id=1)
        lesson = Lesson.objects.filter(year_of_study=student.year_of_study, group_letter=student.group_letter, subject=subject).get(id=1)
        return Commendation.objects.create(text='Хвалю!', created=lesson.date, schoolkid=student, subject=lesson.subject, teacher=lesson.teacher)
    except ObjectDoesNotExist as err:
        print(err)
