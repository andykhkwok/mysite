# blogging/urls.py

from django.urls import path
from blogging.views import stub_view, list_view, detail_view, add_model

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('addpost/', add_model, name="new_post")
]

# urlpatterns = [
    # path('', list_view, name="blog_index"),
    # path('posts/<int:post_id>/', detail_view, name="blog_detail"),
# ]

# urlpatterns = [
    # path('', stub_view, name="blog_index"),
    # path('posts/<int:post_id>/', stub_view, name="blog_detail"),
# ]
