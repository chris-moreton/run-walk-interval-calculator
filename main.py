def calculate_optimal_intervals(target_distance_metres, target_time_seconds, target_run_speed_kph,
                                target_walk_speed_kph, min_walking_interval_seconds):
    intervals = []
    current_run_speed_kph = target_run_speed_kph
    current_walk_speed_kph = target_walk_speed_kph

    # Calculate time to walk the target distance at the current walk speed
    walk_time_seconds = ((target_distance_metres / current_walk_speed_kph) / 1000) * 3600
    print(f"Walk time: {walk_time_seconds:.2f} seconds")

    if (walk_time_seconds <= target_time_seconds):
        print("Walking the whole distance")
        return [("Walk", target_distance_metres / 1000, current_walk_speed_kph)]

    # Calculate time to run the target distance at the current run speed
    run_time_seconds = ((target_distance_metres / current_run_speed_kph) / 1000) * 3600
    print(f"Run time: {run_time_seconds:.2f} seconds")

    # How much spare time do we have after running the target distance?
    spare_time_seconds = target_time_seconds - run_time_seconds
    print(f"Spare time: {spare_time_seconds:.2f} seconds")

    if spare_time_seconds <= 0:
        print("Not enough time to run the whole distance")
        return [("Run", target_distance_metres / 1000, current_run_speed_kph)]

    walk_interval_seconds = 1
    reduced_run_distance_metres = target_distance_metres
    while spare_time_seconds > 0:
        walk_speed_mps = current_walk_speed_kph * 1000 / 3600
        run_speed_mps = current_run_speed_kph * 1000 / 3600

        print("Walk time: ", walk_interval_seconds)

        # Calculate distance covered in walking interval accurately
        walk_distance_metres = walk_interval_seconds * walk_speed_mps
        print(f"Walk distance: {walk_distance_metres:.2f} metres")

        # Calculate how many metres need to be run, considering the correct walk distance
        remaining_distance_metres = target_distance_metres - walk_distance_metres
        print(f"Remaining distance: {remaining_distance_metres:.2f} metres")

        # Calculate time to run the remaining distance accurately
        remaining_run_time_seconds = remaining_distance_metres / run_speed_mps
        print(f"Remaining run time: {remaining_run_time_seconds:.2f} seconds")

        # Calculate total time with walk interval accurately
        total_time_with_walk = remaining_run_time_seconds + walk_interval_seconds
        print(f"Total time with walk: {total_time_with_walk:.2f} seconds")

        # Update spare time seconds based on accurate total time calculation
        spare_time_seconds = target_time_seconds - total_time_with_walk
        print(f"Spare time: {spare_time_seconds:.2f} seconds")

        if spare_time_seconds >= 0:
            # Update run distance and time
            reduced_run_distance_metres = remaining_distance_metres
            walk_interval_seconds += 1
        else:
            # Correctly adjust walk_interval_seconds if the last increment made the total time exceed the target time
            walk_interval_seconds = max(0, walk_interval_seconds - 1)  # Ensure it doesn't go negative
            break

    print(f"Final walk interval seconds: {walk_interval_seconds} seconds")

    # How many walking intervals of min_walking_interval_seconds can we fit into walk_interval_seconds?
    walk_intervals = walk_interval_seconds // min_walking_interval_seconds
    running_intervals = walk_intervals + 1
    print(f"Walk intervals: {walk_intervals}, Running intervals: {running_intervals}")
    running_interval_distance = reduced_run_distance_metres / running_intervals
    print(f"Running interval distance: {running_interval_distance} metres")

    # Add walking intervals
    for i in range(walk_intervals):
        intervals.append(("Run", running_interval_distance / 1000, current_run_speed_kph))
        intervals.append(("Walk", min_walking_interval_seconds * current_walk_speed_kph / 3600, current_walk_speed_kph))

    # Add the last running interval
    intervals.append(("Run", running_interval_distance / 1000, current_run_speed_kph))

    return intervals


# Example parameters
target_distance_metres = 5000
target_time_seconds = 2100
target_run_speed_kph = 12
target_walk_speed_kph = 5.5
max_walk_speed_kph = 7
max_run_speed_kph = 12
min_walking_interval_seconds = 45

intervals = calculate_optimal_intervals(target_distance_metres, target_time_seconds,
                                        target_run_speed_kph, target_walk_speed_kph, min_walking_interval_seconds)

cum_time = 0
for interval in intervals:
    # Convert speed from km/h to m/s
    speed_mps = interval[2] * 1000 / 3600
    # Calculate time in seconds for the interval
    time_seconds = (interval[1] * 1000) / speed_mps
    # Update cumulative time with the accurate interval time
    cum_time += time_seconds
    print(
        f"{interval[0]} for {interval[1]:.2f} km at {interval[2]} km/h (interval time: {time_seconds:.2f} seconds), cumulative time: {cum_time:.2f} seconds")
