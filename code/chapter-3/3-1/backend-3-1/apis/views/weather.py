
import json

from django.http import HttpResponse,JsonResponse, FileResponse

from thirdparty import juhe


def helloworld(request):
    print('request method: ', request.method)
    print('request META: ', request.META)
    print('request cookies: ', request.COOKIES)
    print('request QueryDict: ', request.GET)
    # return HttpResponse(content='Hello Django Response', status=201)
    m = {
        "message": "Hello Django Response"
    }
    return JsonResponse(data=m, safe=False, status=200)
    pass


def weather(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        data = juhe.weather(city)
        return JsonResponse(data=data, status=200)
    elif request.method == 'POST':
        received_body = request.body
        received_body = json.loads(received_body)
        cities = received_body.get('cities')
        response_data = []
        for city in cities:
            result = juhe.weather(city)
            result['city'] = city
            response_data.append(result)
        return JsonResponse(data=response_data, safe=False, status=200)
