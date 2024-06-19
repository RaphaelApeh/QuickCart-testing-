from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q 

from .forms import ItemForm,CommentForm
from .models import Item,Category,Comment

@login_required
def formView(request):
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.author = request.user
            item.save()
            return redirect('detail', pk=item.id)
    return render(request,'core/new.html',{'form':form})


def homeView(request):
    item = Item.objects.all()
    category = Category.objects.all()
    query = request.GET.get('query','')
    print(query)
    if query:
      item = item.filter(Q(name__icontains=query)| Q(discription__icontains=query))
      print(item)
    item_count = item.count()
    category_count = category.count()
    return render(request,'core/home.html',{'item':item,'category':category,'item_count':item_count,
                            'category_count': category_count,
                            'guery':query,            
                                            })

@login_required
def user_detail(request):
    item = Item.objects.filter(author=request.user)
    return render(request,'core/user_detail.html',{'item':item})

@login_required
def updateView(request,pk):
    item = get_object_or_404(Item,pk=pk)
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('detail',pk=item.id)
    else:
     form = ItemForm(instance=item) 
    if item.author != request.user :
        return redirect('home')  
    return render(request,'core/update.html',{'form':form})

@login_required
def deleteView(request,pk):
    item = Item.objects.get(id=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid:
           item.delete()
           return redirect('home')
    if item.author != request.user :
        return redirect('home')
    return render(request,'core/delete.html',{'form': item,'obj': item })


@login_required
def detailView(request,pk):
    item = Item.objects.get(id=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.item = item.name
            comment.save()
    comment = Comment.objects.filter(item=pk)
    return render(request,'core/detail.html',{'item':item,'form':form,'comment':comment})


def category_view(request,pk):
    categories = Category.objects.filter(id=pk)

    return render(request,'core/home.html',{'categories':categories})
