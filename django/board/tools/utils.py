# request.method : http method 가져오기


def get_client_ip(request):
    ip = request.META.get("REMOTE_ADDR")  # request.META['REMOTE_ADDR']
    return ip
