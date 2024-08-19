Postmortem: The Day InstantChat Took a "Lunch Break"

Issue Summary
Duration:
On August 12, 2024, from 14:30 UTC to 15:15 UTC, InstantChat decided to take an unplanned 45-minute "lunch break."

Impact:
During this time, 90% of users were left in the digital equivalent of an awkward silence—unable to send or receive messages. Everyone was also locked out, with 100% of users unable to log in. So, around 1.2 million people globally found themselves on an unexpected "social media detox."

Root Cause:
The root cause? A well-intentioned but misguided configuration change that throttled our database connection pool. Picture a crowded cafeteria with only one lunch lady serving—chaos ensued.

Timeline
14:30 UTC - Detection: Our monitoring system screamed for help, reporting that our database was moving slower than a snail on vacation.
14:32 UTC - Initial Investigation: The DevOps team realized something was seriously wrong with the database cluster—it was under more pressure than a Monday morning.
14:35 UTC - Escalation: The on-call DBA was summoned like a superhero to the scene.
14:40 UTC - The DDoS Decoy: Suspecting an attack, the team chased a red herring, thinking we were under a DDoS siege. Spoiler alert: We weren't.
14:45 UTC - Course Correction: Application logs revealed the real culprit—database connection timeouts.
14:50 UTC - Eureka Moment: The team discovered that our database connection pool had been unintentionally starved. It was like trying to squeeze a river through a straw.
15:00 UTC - Fixing the Faucet: The team reverted the connection pool settings, allowing the database to breathe again.
15:10 UTC - Recovery: Like magic, the database started catching up, and messages began to flow.
15:15 UTC - All Clear: Full service was restored, and users were once again free to chat about their cat videos and weekend plans.
Root Cause and Resolution
Root Cause:
Our database connection pool settings were the villain of this story. During a routine configuration update, someone thought it would be smart to reduce the maximum number of connections from 100 to 10. Imagine a busy coffee shop suddenly reducing their baristas from 10 to 1—chaos! The reduced connection capacity couldn't handle the demand, leading to delays, timeouts, and ultimately, a full-blown outage.

Resolution:
Once we identified the bottleneck, we promptly reverted the connection pool settings back to 100 connections. With the database now able to handle the traffic, everything returned to normal. We also gave the database nodes a gentle reboot, ensuring they were refreshed and ready to go.

Corrective and Preventative Measures
Improvements Needed:
Configuration Change Validation: Implement stricter validation and testing processes for configuration changes, especially those affecting critical components like the database.
Monitoring Enhancements: Improve monitoring to detect configuration-related issues more effectively before they lead to outages.
Incident Response Training: Conduct regular incident response drills to ensure rapid identification and resolution of similar issues in the future.
Specific Tasks:
Patch Connection Pool Settings: Review and update the configuration management system to prevent unauthorized or incorrect changes to critical settings.
Add Monitoring Alerts: Implement detailed monitoring on database connection pool metrics, with specific alerts for sudden changes in connection usage.
Automated Rollback Mechanism: Develop an automated rollback mechanism for database configuration changes that can quickly revert to a stable state if issues are detected.
Incident Documentation: Document this incident in the internal knowledge base and use it as a case study for future training sessions.
