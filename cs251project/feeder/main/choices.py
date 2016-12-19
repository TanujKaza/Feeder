from django.contrib.auth.models import User

SEMESTER_CHOICES = (
    ('Autumn', 'Autumn'),
    ('Spring', 'Spring'),
    ('Summer', 'Summer')
)

DURATION_CHOICES = (
    ('Full', 'Full'),
    ('Half', 'Half'),
    ('Summer', 'Summer')
)

DEPARTMENT_CHOICES = (
    ('Aerospace Engineering', 'Aerospace Engineering'),
    ('Biosciences and Bioengineering', 'Biosciences and Bioengineering'),
    ('Chemical Engineering', 'Chemical Engineering'),
    ('Chemistry', 'Chemistry'),
    ('Civil Engineering', 'Civil Engineering'),
    ('Computer Science & Engineering', 'Computer Science & Engineering'),
    ('Earth Sciences', 'Earth Sciences'),
    ('Electrical Engineering', 'Electrical Engineering'),
    ('Energy Science and Engineering', 'Energy Science and Engineering'),
    ('Humanities & Social Science', 'Humanities & Social Science'),
    ('Industrial Design Centre', 'Industrial Design Centre'),
    ('Mathematics', 'Mathematics'),
    ('Mechanical Engineering', 'Mechanical Engineering'),
    ('Metallurgical Engineering & Materials Science', 'Metallurgical Engineering & Materials Science'),
    ('Physics', 'Physics')
)

users = User.objects.all()
INSTRUCTOR_CHOICES = []
for user in users:
    INSTRUCTOR_CHOICES.append((user.id,user.username))

