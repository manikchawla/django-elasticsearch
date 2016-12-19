from model_mommy import mommy
from django.core.management.base import BaseCommand
from core.models import University, Course, Student

class Command(BaseCommand):
    help = "My shiny new management command"

    def handle(self, *args, **options):
        print('lala')
        self.make_universities()
        self.make_courses()

    def make_universities(self):
        university_names = (
            'MIT', 'MGU', 'CalTech', 'KPI', 'DPI', 'PSTU'
            )
        self.universities = []
        for name in university_names:
            uni = mommy.make(University, name=name)
            self.universities.append(uni)

    def make_courses(self):
        template_options = ['CS%s0%s', 'MATH%s0%s', 'CHEM%s0%s', 'PHYS%s0%s']
        self.courses = []
        for num in range(1, 4):
            for course_num in range(1, 4):
                for template in template_options:
                    name = template % (course_num, num)
                    course = mommy.make(Course, name=name)
                    print(course.name)
                    self.courses.append(course)