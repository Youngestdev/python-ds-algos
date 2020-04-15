def optimal_task_assignment(arr):
    arr = sorted(arr)
    for i in range(len(arr)//2):
        print(arr[i], arr[~i])
