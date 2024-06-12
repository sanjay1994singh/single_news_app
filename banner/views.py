from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Banner, BannerImage


@csrf_exempt
def banner(request):
    if request.method == 'GET':
        banner_list = []
        banner = Banner.objects.all()
        if banner:
            for i in banner:
                banner_dict = {}
                banner_dict['id'] = i.id
                banner_dict['banner_code'] = i.banner_code
                banner_dict['banner_title'] = i.banner_title
                banner_image = BannerImage.objects.filter(banner__banner_code=i.banner_code).values('img')
                if banner_image:
                    banner_dict['banner_image'] = list(banner_image)
                else:
                    banner_dict['banner_image'] = []
                banner_list.append(banner_dict)
        return JsonResponse({'banner_list': banner_list}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
