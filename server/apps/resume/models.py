from django.db import models


class ContactInfo(models.Model):
    class Meta:
        verbose_name = 'контактные данные'

    name = models.CharField('имя', max_length=64)
    surname = models.CharField('фамилия', max_length=64)
    address = models.CharField('адрес', max_length=255, default='')
    phone = models.CharField('телефон', max_length=15)
    email = models.EmailField('email', max_length=64)
    photo = models.ImageField('фото', upload_to='photo')
    description = models.TextField('описание', max_length=2048, null=True, blank=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    class Meta:
        verbose_name = 'характер'
        verbose_name_plural = 'характер'

    name = models.CharField('характер', max_length=255)
    description = models.TextField('описание', max_length=512)

    def __str__(self):
        return self.name


class Skill(models.Model):
    class Meta:
        verbose_name = 'навык'
        verbose_name_plural = 'навыки'

    name = models.CharField('навык', max_length=255)
    description = models.TextField('описание', max_length=512)
    score = models.PositiveSmallIntegerField('оценка навыка', default=50)
    icon = models.CharField('иконка Font Awesome', max_length=64, default='fab fa-check-square-o')

    def __str__(self):
        return self.name


class Education(models.Model):
    class Meta:
        verbose_name = 'образование'

    name = models.CharField('учебное заведение', max_length=255)
    degree = models.CharField('ученая степень', max_length=255)
    specialization = models.CharField('специализаия', max_length=255)
    gpa = models.DecimalField('средний балл', max_digits=4, decimal_places=2, default='5.00')
    date_for = models.DateField('дата начала обучения')
    date_to = models.DateField('дата окончания обучения')

    def __str__(self):
        return self.name


class Certificate(models.Model):
    class Meta:
        verbose_name = 'сертификат'
        verbose_name_plural = 'сертификаты'

    name = models.CharField('сертификат', max_length=255)
    score = models.PositiveSmallIntegerField('оценка', default=50)
    image = models.ImageField('изображение', upload_to='certifications',  null=True, blank=True)
    date = models.DateField('дата получения')
    url = models.URLField('ссылка на сертификат', max_length=255, default='https://')

    def __str__(self):
        return self.name


class Job(models.Model):
    class Meta:
        verbose_name = 'место работы'

    organisation = models.CharField('организация', max_length=255)
    position = models.TextField('должность', max_length=255)
    description = models.TextField('описание', max_length=2048)
    date_for = models.DateField('дата начала работы')
    date_to = models.DateField('дата окончания работы', null=True, blank=True)

    def __str__(self):
        return self.position


class Project(models.Model):
    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'

    name = models.CharField('проект', max_length=255)
    description = models.TextField('описание', max_length=512)
    image = models.ImageField('изображение', upload_to='projects/', null=True, blank=True)
    url = models.URLField('ссылка', max_length=255, default='https://')

    def __str__(self):
        return self.name


class SocialNetwork(models.Model):
    class Meta:
        verbose_name = 'соцсеть'
        verbose_name_plural = 'соцсети'

    name = models.CharField('соцсеть', max_length=100)
    icon = models.CharField('иконка Font Awesome', max_length=50, default='fa fa-check-square-o')
    url = models.URLField('ссылка', max_length=255, default='https://')

    def __str__(self):
        return self.name
