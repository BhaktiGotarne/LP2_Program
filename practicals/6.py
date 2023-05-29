# Jobs, Profit, Slot
profit = [15,27,10,100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2,3,3,3,4] 
profitNJobs = list(zip(profit,jobs,deadline))
profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
slot = []
for _ in range(len(jobs)):
    slot.append(0)

profit = 0
ans = []

for i in range(len(jobs)): 
    ans.append('null')

for i in range(len(jobs)):
        job = profitNJobs[i]
        #check if slot is occupied
        for j in range(job[2], 0, -1):
            if slot[j] == 0:
                ans[j] = job[1]
                profit += job[0]
                slot[j] = 1
                break
         
print("Jobs scheduled buddy:", ans[1:])
print(profit)




# The code you provided is implementing a greedy algorithm to schedule jobs based on their profit and deadline. Here's how it works:

# The code initializes the profit, jobs, and deadlines as lists.
# The profitNJobs list is created by combining the profit, job, and deadline lists using the zip function. Each element in profitNJobs contains the profit, job name, and deadline for a specific job.
# The profitNJobs list is sorted in descending order based on the profit using the sorted function and a lambda function as the sorting key.
# The slot list is initialized with zeros, indicating that no slots are occupied initially.
# The profit and ans variables are initialized to zero and an empty list, respectively.
# The first loop initializes the ans list with 'null' values, indicating that no jobs are scheduled yet.
# The second loop iterates over each job in the sorted profitNJobs list.
# For each job, the code checks if there is an available slot starting from the job's deadline and going backwards.
# If an available slot is found, the job is scheduled in that slot by updating the ans list with the job name, increasing the profit by the job's profit, marking the slot as occupied in the slot list, and breaking the loop.
# Finally, the code prints the scheduled jobs (excluding the first 'null' value in the ans list) and the total profit.
# It's important to note that this code assumes that the number of slots available is equal to the highest deadline among the jobs. Additionally, if multiple jobs have the same profit, the one with the earliest deadline will be scheduled first.

# If you have any further questions, please let me know!