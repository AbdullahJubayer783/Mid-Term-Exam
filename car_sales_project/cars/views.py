from django.shortcuts import render, redirect
from django.views.generic import DetailView
from . import models
from . import forms
from user.models import History
# Create your views here.
def deatils(request , id):
    return render(request, 'details.html')


class DetailsCarView(DetailView):
    model = models.Car
    template_name = 'details.html'
    # context_object_name = 'car'
    pk_url_kwarg = 'id'

    def post(self,request,*args ,**kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args ,**kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

# Buy Now Button
def buy_now(request, id):
    car = models.Car.objects.get(pk=id)
    if car.quantity > 0:
            history = History(name=car.name, brand=car.brand.name, quantity=1, user=request.user)
            history.save()
            car.quantity -= 1
            car.save()
    return redirect('profile')