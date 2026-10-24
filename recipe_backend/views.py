from django.http import JsonResponse


def api_test(request):
    return JsonResponse(
        {"message": "Connected to the Django backend!", "status": "success"}
    )
