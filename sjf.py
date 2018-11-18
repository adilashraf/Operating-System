n=int(input("Enter the number of process: "))

processes=[]
burst_time=[]     
for i in range(0,n):
    processes.insert(i,i+1)
    #print(processes[i])
burst_time=list(map(int, input("Enter the burst time of the processes comma separated: ").split(",")))
for i in range(0,len(burst_time)-1):  #applying bubble sort to sort process according to their burst time
    for j in range(0,len(burst_time)-i-1):
        if(burst_time[j]>burst_time[j+1]):
            temp=burst_time[j]
            burst_time[j]=burst_time[j+1]
            burst_time[j+1]=temp
            temp=processes[j]
            processes[j]=processes[j+1]
            processes[j+1]=temp
wait_t=[]    
avg_wt=0
turnarround_t=[] 
avg_turnarround_t=0 
wait_t.insert(0,0)
turnarround_t.insert(0,burst_time[0])
for i in range(1,len(burst_time)):  
    wait_t.insert(i,wait_t[i-1]+burst_time[i-1])
    turnarround_t.insert(i,wait_t[i]+burst_time[i])
    avg_wt+=wait_t[i]
    avg_turnarround_t+=turnarround_t[i]
avg_wt=float(avg_wt)/n
avg_t_around_t=float(avg_turnarround_t)/n
print("\n")
print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
for i in range(0,n):
    print(str(processes[i])+"\t\t"+str(burst_time[i])+"\t\t"+str(wait_t[i])+"\t\t"+str(turnarround_t[i]))
print("\n")
print("Average Waiting time is: "+str(avg_wt))
print("Average Turn Arount Time is: "+str(avg_turnarround_t))