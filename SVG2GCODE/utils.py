from datetime import datetime as dt

def timer(t, label):
    duration = dt.now() - t
    duration = duration.total_seconds()
    print("{} took {}".format(label, duration))
    return duration