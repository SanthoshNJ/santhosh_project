from django.urls import path
from .views import (
    admin_dashboard, create_admin,
    BookListCreateView, BookDetailView, StudentBookListView, 
    book_list, library_home
)

urlpatterns = [

    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('student-books/', StudentBookListView.as_view(), name='student-book-list'),
    
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('create-admin/', create_admin, name='create_admin'),
    
    path('library/', book_list, name='library-books'),
    path('library/home/', library_home, name='library-home'),
    
    # Default Homepage
    path('', library_home, name='library-home'),
]
