from . models import Category


def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)


#context context_processors oluşturmanın avantajı projenin her yerinden çağrılabilmesi
    #kesinlikle dictionary döndürmesi gerekiyor !!!
    #settings.py dosyasında templates bölümünde context_processors altına yolunu belirtmeyi unutma,
    #yolu : category (app) -> context_processors(.py yazılmıyor) -> menu_links == şeklinde yaz
    # ==> 'category.context_processors.menu_links',
