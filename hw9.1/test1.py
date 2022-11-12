import pyterm_progress_bar
import time

progress_bar = pyterm_progress_bar.ProgressBar(
    name='Progress',  # Default
    char='#'  # Default
)
progress_bar.start()

for i in range (0, 6):
    time.sleep(2)
    # Do stuff
    progress_bar.update((i+1)/5)  # between 0 and 1 inclusive.