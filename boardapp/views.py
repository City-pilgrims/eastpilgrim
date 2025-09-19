from django.shortcuts import render, get_object_or_404

# Create your views here.
from boardapp.models import Board


def BoardList(request):
    board_contents = Board.objects.all().order_by('-created_at')
    return render(request, 'boardapp/board_list.html',{'board_contents': board_contents})

def BoardDetail(request, pk):

    board_contents = get_object_or_404(Board, pk=pk)

    return render(request, 'boardapp/board_detail.html', {'board_contents': board_contents})

