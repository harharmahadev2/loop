#trigger report generations
Loop Delivery Intelligence API

Target:
Monitoring of restros if online or not
Details of when store got inactive

Curr timestamp is the max timestamp. Since data is static


APIS
Trigger Report
-> no input
-> report id in output used for polling report status
Get Report endpoint 
-> input : report id
-> return status ‘running’ if report  is not complete
        `			else return complete with the csv file
