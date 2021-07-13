from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from MyApp.models import Book, Review
from django.http import Http404
#from django.contrib.auth.mixins import LoginRequiredMixin

# For Generic Views (less code is better)
from django.views import generic
from django.core.files.storage import FileSystemStorage
from MyApp.form import ReviewForm

class BookListView(generic.ListView):
    # template_name = "MyApp/index.html"
    # context_object_name = "books"
    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book
    # template_name = ""
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = context["book"].review_set.order_by("-created_at")
        context["author"] = context["book"].author.all()
        context["form"] = ReviewForm()
        return context



def author(request, author):
    books = Book.objects.filter(author__name = author)
    context = {"book_list" : books}
    return render(request, "MyApp/book_list.html", context)
    


def review(request, id):
    if request.user.is_authenticated:
        newReview = Review(book_id = id, user = request.user)
        form = ReviewForm(request.POST, request.FILES, instance = newReview)
        if form.is_valid():
            form.save()
            
    return redirect(f'/MyApp/{id}/')


"""
# Create your views here.

    def index(request):
        dbData = Book.objects.all()
        context = {"books" : dbData}
        return render(request, "MyApp/index.html", context) 


    def show(request, id):
        singleBook = get_object_or_404(Book, pk = id)
        reviews = Review.objects.filter(book_id = id).order_by('-created_at')
        context = {"book" : singleBook, "reviews" : reviews}
        return render(request, "MyApp/show.html", context)


    def review(request, id):
        userReviewInput = request.POST['review']
        newReview = Review(body = userReviewInput, book_id = id)
        newReview.save()
        return redirect('/book')      """