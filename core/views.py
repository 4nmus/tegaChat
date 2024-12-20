from django.shortcuts import render
from .models import Message
from django.views.generic import CreateView
import hashlib
import time
# Create your views here.


def main(request):
    return render(request, 'core/main.html')

class ShowMessages(CreateView):
    model = Message
    template_name = "core/main.html"
    context_object_name = "messages"
    fields = ['text']

    def get_context_data(self, **kwargs):
        ctx = super(ShowMessages, self).get_context_data(**kwargs)
        ctx['title'] = "Main page"
        ctx['messages'] = Message.objects.all().order_by('-date')
        return ctx
    def form_valid(self, form):
        user_id = GetSession(self.request)
        if not user_id:
            user_id = SetSession(self.request)
        form.instance.rand_id = hashlib.sha256(user_id.encode('utf-8')).hexdigest()[:9]
        return super().form_valid(form)


def SetSession(request):
    #user id based on current time with hash
    user_id = hashlib.sha256(f"{time.time()}".encode('utf-8')).hexdigest()[:9]
    request.session['user_id'] = user_id
    return user_id
def GetSession(request):
    user_id = request.session.get('user_id')
    return user_id