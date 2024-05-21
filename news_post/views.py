# views.py in your app
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from author.models import NewsPostAuthor

from category.models import Category

from news_post.models import NewsPost


@csrf_exempt
def create_news_post(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        content = data.get('content')
        author_id = int(data.get('author'))
        category_id = int(data.get('categories'))

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
        news_post.save()
        return JsonResponse({'message': 'News post created successfully'}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def update_news_post(request):
    if request.method == 'POST':
        data = request.POST
        post_id = int(data.get('post_id'))
        title = data.get('title')
        content = data.get('content')
        author_id = int(data.get('author'))
        category_id = int(data.get('categories'))

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

        NewsPost.objects.filter(id=post_id).update(title=title,
                                                   content=content,
                                                   author_id=author_id,
                                                   categories_id=category_id
                                                   )
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
                news_post_dict['post_categories'] = i.categories.name if i.categories.name else ''
                news_post_dict['post_author'] = i.author.user.name if i.author.user.name else ''
                news_post_dict['post_created_date'] = i.created_date
                news_post_list.append(news_post_dict)

        return JsonResponse({'news_post_list': news_post_list}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
