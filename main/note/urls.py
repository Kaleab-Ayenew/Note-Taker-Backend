from django.urls import path, include
from note import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('my-notes/', views.NoteList.as_view(), name='note_list_url'),
    path('note-content/<int:pk>/', views.NoteContent.as_view(), name='note_content_url')
]

urlpatterns = format_suffix_patterns(urlpatterns)