def multiply_events_recursion(events):
    if not events:
        return 0
    
    current_event, remaining_events = events[0], events[1:]

    option_1 = current_event + multiply_events_recursion(remaining_events)
    print("option_1 -> after", option_1)

    option_2 = multiply_events_recursion(remaining_events)

    print("option_2", option_2)
    return max(option_1, option_2)



if __name__ == "__main__":
   test = [2, 3, 2, 1, 6]
   multiply_events_recursion(test)
