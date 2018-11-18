n=int(input("Enter the number of processess: "))
processes=[]
for i in range(0,n):
     processes.insert(i,i+1)
burst_time=list(map(int, input("Enter the burst time of the processes comma separated: ").split(",")))
priority=list(map(int, input("Enter the priority of the processes comma separated: ").split(",")))
turnaround_time=[]
waiting_t=[]
 
for i in range(0,len(priority)-1):
    for j in range(0,len(priority)-i-1):
        if(priority[j]>priority[j+1]):
            temp=priority[j]
            priority[j]=priority[j+1]
            priority[j+1]=temp
            temp=burst_time[j]
            burst_time[j]=burst_time[j+1]
            burst_time[j+1]=temp
            temp=processes[j]
            processes[j]=processes[j+1]
            processes[j+1]=temp
waiting_t.insert(0,0)
turnaround_time.insert(0,burst_time[0])
for i in range(1,len(processes)):
     waiting_t.insert(i,waiting_t[i-1]+burst_time[i-1])
     turnaround_time.insert(i,waiting_t[i]+burst_time[i])
 

avg_turn_t=0
avg_wait_t=0
for i in range(0,len(processes)):
     avg_wait_t=avg_wait_t+waiting_t[i]
     avg_turn_t=avg_turn_t+turnaround_time[i]
     avg_wait_t=float(avg_wait_t)/n
     avg_wait_t=float(avg_turn_t)/n
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
     print(str(processes[i])+"\t\t"+str(burst_time[i])+"\t\t"+str(waiting_t[i])+"\t\t"+str(turnaround_time[i]))
     print("\n")
print("Average Waiting time is: "+str(avg_wait_t))
print("Average Turn Around Time is: "+str(avg_turn_t))