def add_time(start, duration, day=None):
    # Days of the week for indexing
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert start time to 24-hour format
    if period == "PM" and start_hour != 12:
        start_hour += 12
    if period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Add time
    end_minute = start_minute + duration_minute
    end_hour = start_hour + duration_hour + end_minute // 60
    end_minute %= 60

    # Calculate days later
    days_later = end_hour // 24
    end_hour %= 24

    # Convert back to 12-hour format
    end_period = "AM"
    if end_hour >= 12:
        end_period = "PM"
    if end_hour == 0:
        final_hour = 12
    elif end_hour > 12:
        final_hour = end_hour - 12
    else:
        final_hour = end_hour

    # Format minutes
    final_minute = f"{end_minute:02}"

    # Format day if provided
    new_day = ""
    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + days_later) % 7
        new_day = f", {days_of_week[new_day_index]}"

    # Format day suffix
    if days_later == 1:
        day_suffix = " (next day)"
    elif days_later > 1:
        day_suffix = f" ({days_later} days later)"
    else:
        day_suffix = ""

    # Final time string
    new_time = f"{final_hour}:{final_minute} {end_period}{new_day}{day_suffix}"
    return new_time
