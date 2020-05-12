from django.http.response import JsonResponse

from courses.models import Course


def courses(request):
    if request.method == 'GET':
        return JsonResponse(Course.objects.all())
    elif request.method == 'POST':
        Course().save()


def course(request, course_id):
    if request.method == 'GET':
        return JsonResponse(Course.objects.all())
    elif request.method == 'POST':
        Course.objects.get(pk=course_id).save()
    elif request.method == 'DELETE':
        Course.objects.get(pk=course_id).delete()
