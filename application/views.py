from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Categories, Notes  # , OrderDetail
from .forms import SignUpForm, EditUserAccountForm, EditCategoriesForm, EditNotesForm
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request, 'index.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('application:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


def user_account(request):
    if request.method == 'POST':
        form = EditUserAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('application:user_account')
    else:
        form = EditUserAccountForm(
            initial={
                'email': request.user.email,
                'image': request.user.image
            }
        )
    return render(request, 'user_account.html', context={'form': form})


def create_category(request):
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['user'] = request.user.id
        form = EditCategoriesForm(request_data)
        if form.is_valid():
            order = form.save()
            # return redirect('create_order_detail', id=order.id)
            return redirect('application:show_categories', page=1)
    else:
        form = EditCategoriesForm()
    return render(request, 'create_category.html', context={'form': form})


def delete_category(request, id):
    Categories.objects.filter(id=id).filter(user=request.user.id).delete()
    return redirect('application:show_categories', page=1)


def edit_category(request, id):
    category = Categories.objects.filter(user=request.user.id).get(pk=id)

    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['user'] = request.user.id
        form = EditCategoriesForm(request_data)
        if form.is_valid():
            Categories.objects.filter(pk=id).filter(user=request.user.id).update(name=request_data['name'])
            return redirect('application:show_categories', page=1)
    else:
        form = EditCategoriesForm(instance=category)

    return render(request, 'edit_category.html', {'form': category})


def show_categories(request, page=1):
    categories_per_page = 10
    categories = Categories.objects.filter(user=request.user.id).order_by('name').all()
    paginator = Paginator(categories, categories_per_page)
    paginated_categories = paginator.get_page(page)
    context = {
        'categories': paginated_categories
    }
    return render(request, 'show_categories.html', context=context)


def show_notes(request, category):
    notes = Notes.objects.filter(user=request.user.id).filter(category=category).order_by('name').all()
    category_obj = Categories.objects.get(pk=category)
    context = {
        'notes': notes,
        'category': category_obj
    }
    return render(request, 'show_notes.html', context=context)


def create_note(request, category):
    if request.method == 'POST':
        request_data = request.POST.copy()
        request_data['user'] = request.user
        request_data['category_id'] = category
        request_data['category'] = category
        form = EditNotesForm(request_data)
        form.category = category
        if form.is_valid():
            # form.save()
            Notes.objects.get_or_create(name=request_data['name'], text=request_data['text'], user=request_data['user'], category_id=category)
            notes = Notes.objects.filter(user=request.user.id).filter(category=category).order_by('name').all()
            category_obj = Categories.objects.get(pk=category)
            context = {
                'notes': notes,
                'category': category_obj
            }
            return render(request, 'show_notes.html', context=context)
    else:
        form = EditNotesForm()

    form.category = category
    return render(request, 'create_note.html', context={'form': form})


""""
def show_order(request, id):
    order_details = OrderDetail.objects.filter(order=id).all()
    context = {
        'order_details': order_details
    }
    return render(request, 'show_order.html', context=context)
"""
