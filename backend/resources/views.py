from django.http.response import JsonResponse

from resources.models import Resource


def resources(request):
    if request.method == 'GET':
        return JsonResponse(Resource.objects.all())
    elif request.method == 'POST':
        Resource().save()


def resource(request, resource_id):
    if request.method == 'GET':
        return JsonResponse(Resource.objects.all())
    elif request.method == 'POST':
        Resource.objects.get(pk=resource_id).save()
    elif request.method == 'DELETE':
        Resource.objects.get(pk=resource_id).delete()
