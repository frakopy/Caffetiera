from .models import Link


def ctx_dic(request):
    dict_links = {}
    links = Link.objects.all()
    for link in links:
        dict_links[link.key] = link.url
    return dict_links
