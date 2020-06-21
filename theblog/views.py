from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .form import PostForm, WalgarPostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

def PassView(request):
    return render(request, 'password.html')
    
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked=True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering= ['-post_date', '-id']


class WalgarHomeView(ListView):
    model = Post
    template_name = 'w_home.html'
    ordering= ['-post_date', '-id']

    

def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    if Category.objects.all() != 'walgar':
        return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
    else:
        return render(request, 'add_post.html')
    ordering= ['-post_date']

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    if cats != 'walgar':
        return render(request, 'categories.html', {'cats':cats.title(),'category_posts':category_posts})
    else:
        return render(request, 'add_post.html')



class ArticleDetails(DetailView):
    model=Post
    template_name='article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(ArticleDetails, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes=stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class WalgarAddPostView(CreateView):
    model = Post
    form_class = WalgarPostForm
    template_name = 'w_add_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditPostForm
    template_name='update_post.html'

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url = reverse_lazy('home')

class WalgarUpdatePostView(UpdateView):
    model=Post
    form_class=WalgarPostForm
    template_name='w_update_post.html'

class WalgarDeletePostView(DeleteView):
    model=Post
    template_name='w_delete_post.html'
    success_url = reverse_lazy('w_home')