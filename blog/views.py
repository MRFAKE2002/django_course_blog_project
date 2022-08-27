from django.views import generic
from django.urls import reverse_lazy

from .models import BlogPost
from .forms import BlogPostForm

class HomePostListView(generic.ListView):
    template_name = 'blog/home_post_list.html'
    context_object_name = 'all_post'
    
    def get_queryset(self):
        return BlogPost.objects.filter(status= 'pub').order_by('-date_time_modified')
    
#___________________________________________________________________________________________________________________________________________

class DetailPostListView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/detail_post_list.html'
    context_object_name = 'post'

#___________________________________________________________________________________________________________________________________________

class CreateBlogPost(generic.CreateView):
    form_class = BlogPostForm
    template_name = 'blog/create_new_post.html'
    #get_absolute_url

#___________________________________________________________________________________________________________________________________________
    
class UpdatePostView(generic.UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/create_new_post.html'

#___________________________________________________________________________________________________________________________________________

class DeletePostListView(generic.DeleteView):
    model = BlogPost
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('home_page')

#___________________________________________________________________________________________________________________________________________

# from django.shortcuts import render, redirect
# from django.shortcuts import get_object_or_404

# def home_post_list_view(request):
#     context = {
#         'all_post' : BlogPost.objects.filter(status= 'pub').order_by('-date_time_modified') 
#     }
#     return render(request, 'blog/home_post_list.html', context)

# def detail_post_list_view(request, pk):
#     context = {
#         'post' : get_object_or_404(BlogPost, pk=pk), 
#     }
#     return render(request, 'blog/detail_post_list.html', context)

# def create_new_post_view(request):
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home_page')
#     else:
#         form = BlogPostForm()
    
#     return render(request, 'blog/create_new_post.html', {'form': form})

# def update_post_view(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
#     form = BlogPostForm(request.POST or None, instance=post)
    
#     if form.is_valid():
#         form.save()
#         return redirect('home_page')

#     return render(request, 'blog/create_new_post.html', {'form': form})

# def delete_post_view(request, pk):
#     post = get_object_or_404(BlogPost, pk=pk)
    
#     if request.method == 'POST':
#         post.delete()
#         return redirect('home_page')
    
#     return render(request, 'blog/delete_post.html', {'post': post})
