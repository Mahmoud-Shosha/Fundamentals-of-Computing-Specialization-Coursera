# template for "Stopwatch: The Game"
import simplegui

# define global variables
timer_state = False
second_tenths = 0
total_stops = 0
success_stops = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    second_tenths = t % 10
    total_seconds = t // 10
    seconds = total_seconds % 60
    total_minutes = total_seconds // 60
    minutes = total_minutes % 60
    if len(str(seconds)) < 2:
        seconds = '0' + str(seconds)

    return str(minutes) + ':' + str(seconds) + '.' + str(second_tenths)

# define event handlers for buttons; "Start", "Stop", "Reset"


def start():
    global timer_state
    timer.start()
    timer_state = True


def stop():
    global total_stops, success_stops, timer_state
    timer.stop()
    if timer_state:
        timer_state = False
        total_stops += 1
        if second_tenths % 10 == 0:
            success_stops += 1


def restart():
    global second_tenths, total_stops, success_stops, timer_state
    timer.stop()
    timer_state = False
    second_tenths = 0
    total_stops = 0
    success_stops = 0


# define event handler for timer with 0.1 sec interval
def increase_time():
    global second_tenths
    second_tenths += 1


# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(format(second_tenths)), [120, 130], 50, "white")
    score = str(success_stops) + '/' + str(total_stops)
    canvas.draw_text(score, [288, 38], 40, "red")


# create frame
frame = simplegui.create_frame("StopWatch", 350, 220)
timer = simplegui.create_timer(100, increase_time)


# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Restart", restart, 100)


# start frame
frame.start()


# Please remember to review the grading rubric
