from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Mark, Chastisement, Schoolkid, Lesson, Commendation, Subject


def get_schoolkid(name):
    try:
        return Schoolkid.objects.get(full_name__contains=name)
    except ObjectDoesNotExist:
        print(f'Ученика {name} не существует, проверьте правильность введённого имени')
    except MultipleObjectsReturned:
        print(f'Учеников с именем {name} больше чем один, попробуйте ввести ФИО')


def get_subject(schoolkid, subject_title):
    try:
        return Subject.objects.get(
            year_of_study=schoolkid.year_of_study, 
            title=subject_title.title())

    except ObjectDoesNotExist:
        print(f'Предмета {subject_title} для {schoolkid.year_of_study} класса не существует') 
        print('проверьте правильность введённого названия')
    except MultipleObjectsReturned:
        print(f'Предметов с названием {subject_title} больше чем один, попробуйте уточнить название')


def get_last_lesson(schoolkid, subject):
    lesson = Lesson.objects.filter(
        year_of_study=schoolkid.year_of_study, 
        group_letter=schoolkid.group_letter, 
        subject=subject).order_by('-date').first()
    if not lesson:
        print(f'Не найдены уроки по {subject.title}')
        return 
    return lesson


def fix_marks(schoolkid):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[3, 2])
    marks.update(points=5)


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(name, subject_title):
    student = get_schoolkid(name)
    subject = get_subject(schoolkid=student, subject_title=subject_title)    
    lesson = get_last_lesson(schoolkid=student, subject=subject)
    return Commendation.objects.create(
        text='Хвалю!', 
        created=lesson.date,
        schoolkid=student, 
        subject=lesson.subject, 
        teacher=lesson.teacher)
