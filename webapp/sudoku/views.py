from django.http import JsonResponse

from .puzzle import make_new_puzzle, remove_numbers_from_puzzle

from django.shortcuts import render


def puzzle(request):
    """
    Generates a new Sudoku puzzle and returns it as a JSON response.

    Args:
        request (HttpRequest): The Django HTTP request object.

    Returns:
        JsonResponse: A response containing the number of attempts and the generated puzzle.
    """
    n_attempts, puzzle =  make_new_puzzle()

    output = {
        'n_attempts': n_attempts,
        'puzzle' : puzzle
    }

    return JsonResponse(output)


def home(request):
    """
    Displays the home page with a new Sudoku puzzle.

    Args:
        request (HttpRequest): The Django HTTP request object.

    Returns:
        HttpResponse: Renders the template with the generated Sudoku puzzle and its difficulty level.
    """
    n_attempts, sudoku_puzzle = make_new_puzzle()
    level = request.GET.get('level', 'easy')
    sudoku_puzzle_with_holes = remove_numbers_from_puzzle(sudoku_puzzle, level)
    sudoku_puzzles = [[(x, y) for x, y in zip(a_row, b_row)] for a_row, b_row in zip(sudoku_puzzle, sudoku_puzzle_with_holes)]

    context = {
        'sudoku_puzzle': sudoku_puzzle,
        'n_attempts': n_attempts, 
        'sudoku_puzzle_with_holes': sudoku_puzzle_with_holes,
        'sudoku_puzzles': sudoku_puzzles,
        'level': level,
    }
    
    return render(request, 'sudoku/home.html', context)
