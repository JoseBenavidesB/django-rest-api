from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.http.response import JsonResponse
import json
from .models import Projects
# Create your views here.
class ProjectView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):

        if(id>0):
            project = list(Projects.objects.filter(id=id).values())
            
            if len(project) > 0:
                data = {
                    'message':'ok',
                    'project':project
                }
            else: data = { 'message': 'There is not any project'}
            
        else:
            projects = list(Projects.objects.values())

            if len(projects) > 0:
                data = {
                    'message':'ok',
                    'projects':projects
                }
            else: data = { 'message': 'There is not any project'}

        return JsonResponse(data)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        #print(jd)
        Projects.objects.create(title=jd['title'], description=jd['description'], image_url=jd['url'])
        data = { 'message':'ok'}
        return JsonResponse(data)

    def put(self, request, id):
        jd = json.loads(request.body)
        if(id):
            projects = list(Projects.objects.filter(id=id).values())
            
            if len(projects) > 0:
                project = Projects.objects.get(id=id)
                project.title = jd['title']
                project.description = jd['description']
                project.image_url = jd['url']
                project.save()
                data= {'message':'ok'}
            else: data = { 'message': 'There is not any project with the ID' + id}
            
        else: data = { 'message': 'There is any ID'}

        return JsonResponse(data)

    def delete(self, request, id):
        project = list(Projects.objects.filter(id=id).values())
        if len(project) > 0:
                Projects.objects.get(id=id).delete()
                data= {'message':'ok'}
        else: data = { 'message': 'There is not any project with the ID' + id}
        return JsonResponse(data)