I've wanted this algorithm for ages and couldn't find it. AI was surprisingly poor at helping me generate it.

It's just a simple interval calculator for people like me who can't run for a prolonged period of time but still want to set targets for 5k/10k runs, etc...

It's a hack and not robust, so crashes will happen with some parameters.

```
target_distance_metres = 5000
target_time_seconds = 1800
target_run_speed_kph = 12
target_walk_speed_kph = 6.5
max_walk_speed_kph = 7
max_run_speed_kph = 12
min_walking_interval_seconds = 45
```

```
Run for 0.25 km at 12 km/h (interval time: 76.38 seconds), cumulative time: 76.38 seconds
Walk for 0.08 km at 6.5 km/h (interval time: 45.00 seconds), cumulative time: 121.38 seconds
Run for 0.25 km at 12 km/h (interval time: 76.38 seconds), cumulative time: 197.77 seconds
Walk for 0.08 km at 6.5 km/h (interval time: 45.00 seconds), cumulative time: 242.77 seconds
...
```
