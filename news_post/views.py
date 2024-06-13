# views.py in your app
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from author.models import NewsPostAuthor

from category.models import Category

from news_post.models import NewsPost

from banner.models import Banner, BannerImage


@csrf_exempt
def create_news_post(request):
    if request.method == 'POST':
        data = request.POST
        data1 = request.FILES
        title = data.get('title')
        content = data.get('content')
        author_id = int(data.get('author'))
        category_id = int(data.get('categories'))
        image = data1.get('image')
        if not title:
            return JsonResponse({'error': 'Title is required'}, status=400)

        if not content:
            return JsonResponse({'error': 'Content is required'}, status=400)

        if not author_id:
            return JsonResponse({'error': 'Author is required'}, status=400)

        if not category_id:
            return JsonResponse({'error': 'Categories is required'}, status=400)

        try:
            obj_author = NewsPostAuthor.objects.get(user_id=author_id)
            author_id = obj_author.id
        except NewsPostAuthor.DoesNotExist:
            return JsonResponse({'error': 'Author does not exist'}, status=404)

        try:
            obj_category = Category.objects.get(pk=category_id)
            category_id = obj_category.id
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category does not exist'}, status=404)

        # Create the news post
        news_post = NewsPost.objects.create(title=title,
                                            content=content,
                                            author_id=author_id,
                                            categories_id=category_id
                                            )
        if news_post:
            news_post.image = image
            news_post.save()
        return JsonResponse({'message': 'News post created successfully'}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def update_news_post(request):
    if request.method == 'POST':
        data = request.POST
        data1 = request.FILES
        post_id = int(data.get('post_id'))
        title = data.get('title')
        content = data.get('content')
        author_id = int(data.get('author'))
        category_id = int(data.get('categories'))
        image = data1.get('image')

        if not title:
            return JsonResponse({'error': 'Title is required'}, status=400)

        if not post_id:
            return JsonResponse({'error': 'Post id is required'}, status=400)

        if not content:
            return JsonResponse({'error': 'Content is required'}, status=400)

        if not author_id:
            return JsonResponse({'error': 'Author is required'}, status=400)

        if not category_id:
            return JsonResponse({'error': 'Categories is required'}, status=400)

        try:
            obj_author = NewsPostAuthor.objects.get(user_id=author_id)
            author_id = obj_author.id
        except NewsPostAuthor.DoesNotExist:
            return JsonResponse({'error': 'Author does not exist'}, status=404)

        try:
            obj_category = Category.objects.get(pk=category_id)
            category_id = obj_category.id
        except Category.DoesNotExist:
            return JsonResponse({'error': 'Category does not exist'}, status=404)

        news_post = NewsPost.objects.filter(id=post_id).update(title=title,
                                                               content=content,
                                                               author_id=author_id,
                                                               categories_id=category_id
                                                               )

        if news_post:
            if image:
                news_post.image = image
                news_post.save()
        return JsonResponse({'message': 'News post updated successfully'}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def list_news_post(request):
    if request.method == 'GET':
        news_post = NewsPost.objects.all().order_by('-id')[:7]
        news_post_list = []
        if news_post:
            for i in news_post:
                news_post_dict = {}
                news_post_dict['post_id'] = i.id
                news_post_dict['post_title'] = i.title
                news_post_dict['post_content'] = i.content
                news_post_dict['image'] = request.build_absolute_uri(i.image.url) if i.image else ''
                news_post_dict['post_categories'] = i.categories.name if i.categories.name else ''
                news_post_dict['post_author'] = i.author.user.name if i.author.user.name else ''
                news_post_dict['post_created_date'] = i.created_date
                news_post_list.append(news_post_dict)

        banner = Banner.objects.all()
        banner_list = []
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
        context = {
            'news_post_list': news_post_list,
            'banner_list': banner_list,
        }
        return JsonResponse(context, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def view_news_post(request):
    if request.method == 'GET':
        data = request.GET
        post_id = int(data.get('post_id'))
        i = NewsPost.objects.get(id=post_id)
        news_post_dict = {}
        news_post_dict['post_id'] = i.id
        news_post_dict['post_title'] = i.title
        news_post_dict['post_content'] = i.content
        news_post_dict['image'] = request.build_absolute_uri(i.image.url) if i.image else ''
        news_post_dict['post_categories'] = i.categories.name if i.categories.name else ''
        news_post_dict['post_author'] = i.author.user.name if i.author.user.name else ''
        news_post_dict['post_created_date'] = i.created_date

        return JsonResponse({'news_post_dict': news_post_dict}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
