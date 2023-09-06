from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import *




# Create your views here.

def allbooks (request):
    allbookobjects = Book.objects.all()
    
    #b = Book.objects.get(bookid__exact=1)
    #for bb in b: 
        #print(f"YOOOOOOOOOOOO {bb.image}")
    return render(request, 'bookmanagement/allbooks.html', {
        'allbooksobject':allbookobjects, 
    })
    
    
def detailedview (request, thisslug):
    b = Book.objects.get(slug=thisslug)
    if(request.user in b.borrowedby.all()):
        m = "Return"
    else:
        m = "Borrow"
    if(request.user in b.wishlist.all()):
        w = "Remove from Wishlist"
    else:
        w = "Wishlist It!"
    return render (request, 'bookmanagement/detailedpage.html', {
        'book': b,
        'msg' : m, 
        'wi' : w
    })
    



@login_required
def borrow_book(request, boid):
    book = get_object_or_404(Book, pk=boid)

    if book.stock > 0:
        book.stock -= 1
        book.save()

        book.borrowedby.add(request.user)
        book.save()

        return redirect('detailedview', book.slug)
    else:
        return render(request, 'autho/text.html', {
        'warning': "The Book Is Not Avaiable For Borrowing, Stock Out!"
    })


@login_required
def return_book(request, boid):
    book = get_object_or_404(Book, pk=boid)

    if request.user in book.borrowedby.all():
        book.stock += 1
        book.borrowedby.remove(request.user)
        book.save()

        return redirect('detailedview', book.slug)
    else:
        return render(request, 'autho/text.html', {
            'warning': "Hey Wait! You Didn't Borrow That Book in The First Place!"
        })
    
    
@login_required
def wishlist(request, boid):
    book = get_object_or_404(Book, pk=boid)

    if request.user in book.wishlist.all():
        #remove from wishlist
        book.wishlist.remove(request.user)
        return redirect('detailedview', book.slug)
        #return HttpResponse("Already WishListed")

    else:
        book.wishlist.add(request.user)
        return redirect('detailedview', book.slug)
        #return HttpResponse("Successfully Wishlisted!")
    


def search_books(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['bookname']
            book = Book.objects.filter(bookname__icontains=title)
        else:
            book = []
    else:
        form = BookSearchForm()
        book = []

    return render(request, 'bookmanagement/book_search.html', {'form': form, 'books': book})


# def cate (request, catename): #not working 
#     a = Book.objects.all()
#     b = Book.objects.filter(cat=catename)
#     return render(request, 'bookmanagement/cat.html', {'book': b, 'c': catename})
