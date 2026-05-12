# Job Scheduling using Greedy Algorithm

def job_scheduling(jobs):

    # Sort jobs according to profit (descending)
    jobs.sort(key=lambda x: x[2], reverse=True)

    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)

    # Create slots
    slots = [-1] * max_deadline

    total_profit = 0

    print("\nSelected Jobs:")

    # Traverse all jobs
    for job in jobs:

        job_id = job[0]
        deadline = job[1]
        profit = job[2]

        # Check slots backward
        for i in range(deadline - 1, -1, -1):

            if slots[i] == -1:

                slots[i] = job_id
                total_profit += profit

                print(job_id, "Profit:", profit)

                break

    print("\nTotal Profit:", total_profit)


# Taking Input from User
n = int(input("Enter number of jobs: "))

jobs = []

print("Enter Job Details:")
print("Format: JobID Deadline Profit")

for i in range(n):
    job_id = input("Enter Job ID: ")
    deadline = int(input("Enter Deadline: "))
    profit = int(input("Enter Profit: "))

    jobs.append((job_id, deadline, profit))

# Function Call
job_scheduling(jobs)


"""""""
Enter number of jobs: 5

Enter Job Details:
Format: JobID Deadline Profit

Enter Job ID: J1
Enter Deadline: 2
Enter Profit: 100

Enter Job ID: J2
Enter Deadline: 1
Enter Profit: 19

Enter Job ID: J3
Enter Deadline: 2
Enter Profit: 27

Enter Job ID: J4
Enter Deadline: 1
Enter Profit: 25

Enter Job ID: J5
Enter Deadline: 3
Enter Profit: 15



Selected Jobs:
J1 Profit: 100
J3 Profit: 27
J5 Profit: 15

Total Profit: 142

"""""""
