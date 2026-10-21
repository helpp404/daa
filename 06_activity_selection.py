"""
EXPERIMENT 6: ACTIVITY SELECTION PROBLEM (GREEDY STRATEGY)
THEORY: Pick the MAXIMUM number of non-overlapping activities.
Greedy trick: always pick the activity with the earliest FINISH time.
It leaves as much time as possible for future activities.

ALGORITHM (simple English):
1. Sort all activities by increasing finish time.
2. Select the first activity.
3. For every next activity, compare start with last selected finish.
4. If start >= last finish, select it. Continue till end.

TIME COMPLEXITY:
Best: O(n) -- Python sort can detect already sorted finish times; scan O(n).
Worst: O(n log n) -- Sorting dominates the O(n) greedy scan.
Space: O(n) -- Sorted copy and selected activities.

VIVA:
Q1. Why earliest finish? A. It saves maximum time for later tasks.
Q2. Is greedy optimal here? A. Yes, for unweighted activity selection.
Q3. Can two activities touch? A. Yes, next start >= previous finish.
"""


def activity_selection(activities):
    # Each activity = (name, start, finish)
    activities = sorted(activities, key=lambda a: a[2])
    selected = []
    last_finish = float('-inf')
    for name, start, finish in activities:
        if start >= last_finish:
            selected.append((name, start, finish))
            last_finish = finish
    return selected


if __name__ == "__main__":
    activities = [
        ('A1', 1, 2), ('A2', 3, 4), ('A3', 0, 6),
        ('A4', 5, 7), ('A5', 8, 9), ('A6', 5, 9),
    ]
    print('Selected activities:')
    for activity in activity_selection(activities):
        print(activity)
