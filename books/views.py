from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Book, Admin  # Ensure the Admin model is imported
from rest_framework import generics, status
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def library_home(request):
    return HttpResponse("<h1>Welcome to the Library Home</h1>")

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class StudentBookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@method_decorator(csrf_exempt, name='dispatch')
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_dashboard(request):
    return JsonResponse({"message": "Welcome Admin!"})

@api_view(['POST'])
def create_admin(request):
    try:
        # Ensure the Admin model exists and handles unique emails
        if Admin.objects.filter(email=request.data['email']).exists():
            return Response({"error": "Admin already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        admin = Admin.objects.create(**request.data)
        return Response({"message": "Admin created successfully"}, status=status.HTTP_201_CREATED)
    
    except ValidationError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
