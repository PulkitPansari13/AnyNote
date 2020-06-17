from django.urls import path, re_path
from notes_app import views

app_name = 'notes_app'

urlpatterns =[
    path('mynotes/',views.NoteListView.as_view(),name='list_note'),
    re_path(r'^mynotes/newnote/$',views.NoteCreateView.as_view(),name='create_note'),
    re_path(r'^mynotes/(?P<pk>\d+)/$',views.NoteDetailView.as_view(),name='detail_note'),
    re_path(r'^mynotes/(?P<pk>\d+)/edit/$',views.NoteEditView.as_view(),name='note_update'),
    re_path(r'^mynotes/(?P<pk>\d+)/delete/$',views.NoteDeleteView.as_view(),name='note_delete'),
]
