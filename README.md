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
    		else return complete with the csv file

1. store_status: store_id, timestamp_utc, status
2. menu hours:store_id, dayOfWeek(0=Monday, 6=Sunday), start_time_local, end_time_local
3. timezone :store_id, timezone_str

output format of get_report endpoint:
store_id, uptime_last_hour(in minutes), uptime_last_day(in hours), update_last_week(in hours), downtime_last_hour(in minutes), downtime_last_day(in hours), downtime_last_week(in hours) 

