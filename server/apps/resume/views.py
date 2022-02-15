from django.views.generic import ListView

from apps.resume.models import Character, ContactInfo, Skill, Education, Certificate, Job, Project, SocialNetwork


class ResumeListView(ListView):
    model = Character
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        kwargs['contact_info'] = ContactInfo.objects.all().first()
        kwargs['skills'] = Skill.objects.all()
        kwargs['education'] = Education.objects.all()
        kwargs['certificates'] = Certificate.objects.all()
        kwargs['jobs'] = Job.objects.all().order_by('date_for')
        kwargs['projects'] = Project.objects.all()
        kwargs['social_networks'] = SocialNetwork.objects.all()
        return super(ResumeListView, self).get_context_data(**kwargs)
