let timerInterval;
let isRunning = false;
let totalSeconds = 0;

/**
 * Updates the timer button display to show the formatted time.
 * Formats minutes and seconds to always display two digits (e.g., 05:03).
 */
function updateTimerDisplay() {
    const timerButton = document.getElementById('timerButton');
    const minutes = Math.floor(totalSeconds / 60);
    const seconds = totalSeconds % 60;
    const formattedMinutes = minutes < 10 ? `0${minutes}` : minutes;
    const formattedSeconds = seconds < 10 ? `0${seconds}` : seconds;
    timerButton.textContent = `${formattedMinutes}:${formattedSeconds}`;
}

/**
 * Starts the timer by incrementing totalSeconds every second
 * and updates the timer display accordingly.
 */
function startTimer() {
    timerInterval = setInterval(() => {
        totalSeconds++;
        updateTimerDisplay();
    }, 1000);
}

/**
 * Stops the timer by clearing the timer interval.
 */
function stopTimer() {
    clearInterval(timerInterval);
}

/**
 * Toggles the timer on and off.
 * Also applies a blur effect to number cells while the timer is running.
 */
function toggleTimer() {
    const timerButton = document.getElementById('timerButton');
    isRunning ? stopTimer() : startTimer();

     // Adds a blur effect to number cells when the timer is running
    Array.from(document.getElementsByClassName("number-cell")).forEach((el) => {
        el.style.filter = isRunning ? "blur(15px)" : null;
    })
    isRunning = !isRunning;
}

document.addEventListener('DOMContentLoaded', () => {
    let selectedNumber = null;

    /**
     * Adds event listeners to the number buttons (1-9) to select a number.
     * Highlights the selected number.
     */
    document.querySelectorAll('.number-container button').forEach(button => {
        button.addEventListener('click', () => {
            selectedNumber = button.textContent;
            document.querySelectorAll('.number-container button').forEach(b => b.style.backgroundColor = '');
            button.style.backgroundColor = '#3D717E';
        });
    });

/**
 * Adds event listeners to the hint button.
 * Fills the next empty cell with the correct number (the "hint").
 */
    document.querySelectorAll('.hint button').forEach(button => {
    button.addEventListener('click', () => {
    cells = document.querySelectorAll('.number-cell');
    for (let i = 0; i < cells.length; i++) {
        cell = cells[i];

        // Only fill cells that are not part of the original puzzle and are currently empty
        if (!cell.classList.contains('number-cell-origin') && !cell.classList.contains('number-cell-selector')) {
            if (cell.textContent === "") {
                cell.textContent = cell.getAttribute("data-origin");
                break;
            }
        }
    }
    });
});

    /**
     * Adds event listeners to the sudoku grid cells.
     * When a cell is clicked, it is filled with the selected number, if correct.
     * If incorrect, a mistake counter increases and updates the mistake display.
     */
    document.querySelectorAll('.number-cell').forEach(cell => {
        if (!cell.classList.contains('number-cell-origin') && !cell.classList.contains('number-cell-selector')) {
            cell.addEventListener('click', () => {
                if (selectedNumber !== null) {
                    originNumber = cell.getAttribute("data-origin");

                    // Correct guess: fill the cell with the selected number
                    if (selectedNumber == originNumber) {
                        cell.textContent = selectedNumber;
                    } else {
                        // Incorrect guess: increment mistake counter
                        mistakeButton = document.querySelector('.mistake .menu-button');
                        mistakes = parseInt(mistakeButton.getAttribute("data-mistakes"));
                        mistakes += 1;
                        mistakeButton.setAttribute('data-mistakes', mistakes);
                        mistakeButton.textContent = `${mistakes} Mistakes`;
                    }
                }
            });
        }
    });
});