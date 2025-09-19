# preachapp/admin.py
from django.contrib import admin
from .models import Content, ContentBlock


class ContentBlockInline(admin.TabularInline):
    model = ContentBlock
    extra = 1
    ordering = ('order',)
    fields = ('block_type', 'text', 'image', 'order')  # 필드 순서 지정
    classes = ('collapse',)  # 접을 수 있는 섹션으로 만들기


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('title',)
    inlines = [ContentBlockInline]
    readonly_fields = ('created_at',)  # 생성일은 읽기 전용

    def save_model(self, request, obj, form, change):
        if not obj.author_id:
            obj.author = request.user
        super().save_model(request, obj, form, change)