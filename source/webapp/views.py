from django.shortcuts import render
from webapp.game import guess_numbers, secret_nums
# Create your views here.
history = {
    'result': '',
}
def index_view(request):
    if request.method == "GET":
        return render(request, "index.html")

    elif request.method == "POST":
        context = {
            'numbers': request.POST.get('numbers'),
            'result': '',
        }
        numbers_str = context['numbers'].split()
        context['result'] = guess_numbers(secret_nums, numbers_str)
        print(secret_nums)
        global history
        history['result'] += context['result']
        return render(request, 'index.html', context)
def history_view(request):
    if request.method == 'GET':
        global history
        return render(request, 'history.html', history)

