# A class to represent a job
class Job:
    def __init__(self, id, profit, deadline):
        self.id = id
        self.profit = profit
        self.deadline = deadline

# Function to schedule jobs to maximize profit
def job_sequencing_with_deadlines(jobs):
    # Sort jobs based on descending profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find the maximum deadline
    max_deadline = max(job.deadline for job in jobs)

    # Create an array to keep track of free time slots
    slots = [-1] * max_deadline  # -1 indicates the slot is free

    # To keep track of the maximum profit
    total_profit = 0
    selected_jobs = []

    # Iterate over each job
    for job in jobs:
        # Find a slot for this job, starting from the last possible slot
        for slot in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[slot] == -1:  # If the slot is free
                slots[slot] = job.id  # Assign the job to this slot
                total_profit += job.profit  # Add the job's profit to total
                selected_jobs.append(job.id)  # Add the job ID to the result
                break

    return selected_jobs, total_profit

jobs = [
    Job(1, 35, 3),
    Job(2, 30, 4),
    Job(3, 25, 4),
    Job(4,20,2),
    Job(5,15,3),
    Job(6,12,1),
    Job(7,5,2)
]

selected_jobs, total_profit = job_sequencing_with_deadlines(jobs)

print("Selected Jobs:", selected_jobs)
print("Total Profit:", total_profit)
