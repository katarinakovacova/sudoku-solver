from django.http import JsonResponse

from sudoku.puzzle import make_new_puzzle


def puzzle(request):
    n_attempts, puzzle =  make_new_puzzle()

    output = {
        'n_attempts': n_attempts,
        'puzzle' : puzzle
    }

    return JsonResponse(output)
