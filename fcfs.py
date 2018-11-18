cnt=int(input("Enter the number of process: "))
burst_time=[]
burst_time=list(map(int, input("Enter the burst time of the processes comma separated: ").split(",")))
wait_t=[]
avg_wait_t=0
turnarround_time=[]
avg_turn_t=0
wait_t.insert(0,0)
turnarround_time.insert(0,burst_time[0])
for i in range(1,len(burst_time)):
    wait_t.insert(i,wait_t[i-1]+burst_time[i-1])
    turnarround_time.insert(i,wait_t[i]+burst_time[i])
    avg_wait_t+=wait_t[i]
    avg_turn_t+=turnarround_time[i]
avg_wait_t=float(avg_wait_t)/cnt
avg_turn_t=float(avg_turn_t)/cnt
print("\n")
print("Process\t  Burst Time\tWaiting Time\tTurn Around Time")
for i in range(0,cnt):
    print(str(i)+"\t\t"+str(burst_time[i])+"\t\t"+str(wait_t[i])+"\t\t"+str(turnarround_time[i]))
print("\n")
print("Average Waiting time is: "+str(avg_wait_t))
print("Average Turn Arount Time is: "+str(avg_turn_t))
