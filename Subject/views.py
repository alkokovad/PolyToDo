from django.shortcuts import render
from django.views import View


class SubjectView(View):
    template_name = 'Subject/subject.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
