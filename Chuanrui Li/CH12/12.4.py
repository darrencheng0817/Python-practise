#How would you load test a webpage without using any test tools?


# To perform load testing, we must first identify the performance-critical scenarios and the metrics which fulfill our performance objectives. Typical criteria include:
# » response time
# » throughput -> # of jobs can be done per unit time
# » resource utilization
# » maximum load that the system can bear.

-> simulate concurrent users by creating thousands of virtual users. This also can test the 
operating capacity

-> for each user, we would programmatically measure response time, data I/O, etc.
In C, there is time function. Record the sending data time and receiving data time








