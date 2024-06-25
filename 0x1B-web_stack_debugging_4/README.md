<<<<<<< HEAD
In this web stack debugging project, I tackled performance issues with our Nginx web server setup using ApacheBench for benchmarking. Initially, we observed a high rate of failed requests during stress testing, indicating a problem with our server configuration under load.

Problem Identification:
Upon running ApacheBench with 2000 requests and 100 requests concurrently, we encountered 943 failed requests. These failures were primarily due to non-2xx responses, particularly HTTP 5xx errors. This indicated that our server was struggling to handle the load efficiently.

Steps Taken to Resolve Issues:
Debugging Process:

Reviewed the ApacheBench output to identify the nature of the failed requests.
Analyzed Nginx error logs (/var/log/nginx/error.log) to understand specific errors and server responses.
Configuration Adjustment:

Updated Nginx configuration files (/etc/nginx/nginx.conf and /etc/nginx/sites-enabled/default) to optimize server parameters such as worker processes, worker connections, and timeouts.
Deployment of Fixes:

Applied configuration changes using Puppet (puppet apply 0-the_sky_is_the_limit_not.pp) to ensure consistent and reproducible deployment across environments.
Verification and Benchmarking:

Re-ran ApacheBench to verify the effectiveness of the fixes.
Observed significant improvement: all 2000 requests completed successfully with zero failed requests.
Benchmark Results:
After implementing the fixes, the benchmark results showed:

Requests per second: Increased from 5664.01 to 6650.99, indicating improved server performance.
Time per request: Decreased from 17.655 ms to 15.035 ms, demonstrating faster response times under load.
Conclusion:
Through systematic debugging and configuration adjustments, we successfully resolved the performance issues with our Nginx web server. By leveraging ApacheBench for stress testing and monitoring Nginx logs for errors, we identified and rectified the root causes, ensuring our server can handle high loads without failing requests.

For future maintenance, continuous monitoring of server logs and periodic benchmarking will be essential to preemptively address any potential performance degradation or scalability challenges.


=======
Web Stack Debugging Task
In this task, we addressed performance issues with a web server setup featuring Nginx, which was experiencing a high number of failed requests under load.

Benchmarking with ApacheBench
We used ApacheBench to simulate HTTP requests to the server, initially making 2000 requests with a concurrency level of 100. The results showed that 943 requests failed.

Applying the Fix
To resolve this, we applied a Puppet configuration script, which successfully fixed the issue, resulting in 0 failed requests upon re-running the benchmark.

User Limit Issue
We also encountered an issue where the holberton user could not log in and open files due to too many open files. Applying another Puppet configuration script resolved this issue, allowing the holberton user to log in and open files without errors.

Repository Information
GitHub repository: alx-system_engineering-devops
Directory: 0x1B-web_stack_debugging_4
Files:
0-the_sky_is_the_limit_not.pp
1-user_limit.pp
>>>>>>> 5fd45968e92e28d7d212d1f557c013db0d42cead
