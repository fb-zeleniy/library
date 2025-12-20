from django.db.models import Avg
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from .models import Book,Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='accounts:register')
def book_list(request):
    books = Book.objects.all()
    return render(request, "library/book_list.html", {"books": books})


@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)


    if request.method == 'POST':

        form = ReviewForm(request.POST)
        if form.is_valid():

            review = form.save(commit=False)
            review.book = book
            review.user = request.user

            try:
                review.save()
            except:

                pass

            return redirect('library:book_detail', pk=book.pk)


    else:

        has_reviewed = Review.objects.filter(book=book, user=request.user).exists()


        if not has_reviewed:
            form = ReviewForm()
        else:
            form = None


    reviews = book.reviews.all()
    average_rating = book.reviews.aggregate(Avg('rating'))['rating__avg']

    context = {
        'book': book,
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
        'has_reviewed': has_reviewed,
    }
    return render(request, 'library/book_detail.html', context)