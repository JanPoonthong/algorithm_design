# Retrieve input value
n = int(input())
activities = []
for _ in range(n):
    activities.append(list(map(int, input().split())))

# Method 1
# Step 1: Sort activities by end time
activities = sorted(activities, key=lambda x: x[1])
print(activities)
# Step 2: Select the first activity
selected_activities = [activities[0]]
last_end_time = activities[0][1]

# Step 3: Iterate over the remaining activities
for i in range(1, len(activities)):
    if activities[i][0] >= last_end_time:
        selected_activities.append(activities[i])
        last_end_time = activities[i][1]

# Output the selected activities
print("Selected activities:", selected_activities)


# Method 2
busy = -1
count = 0
for act in activities:
    if act[0] > busy:
        count += 1
        busy = act[1]
print(count)
