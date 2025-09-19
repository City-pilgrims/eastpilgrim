from django.shortcuts import render, get_object_or_404
from preachapp.models import Content


def weekly_preaching_list(request):
    contents = Content.objects.prefetch_related('blocks').order_by('-created_at')
    for content in contents:
        content.first_image = content.blocks.filter(block_type='image').first()
    return render(request, 'preachapp/weekly_preaching_list.html', {'contents': contents})


def weekly_preaching_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    return render(request, 'preachapp/weekly_preaching_detail.html', {'content': content})


def intro_images(request):
    return render(request, "preachapp/intro.html")