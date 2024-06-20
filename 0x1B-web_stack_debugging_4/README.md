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
