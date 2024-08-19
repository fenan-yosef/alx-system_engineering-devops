Postmortem: Outage of the "InstantChat" Messaging Service
Issue Summary
Duration:
The outage occurred on August 12, 2024, from 14:30 UTC to 15:15 UTC (45 minutes).
Impact:
The "InstantChat" messaging service experienced a complete outage, preventing 90% of users from sending or receiving messages. Additionally, 100% of users were unable to log in during this time. Approximately 1.2 million users were affected globally.
Root Cause:
A misconfiguration in the database connection pool settings caused the primary database cluster to become overwhelmed, leading to a cascading failure across the entire service.

Timeline
14:30 UTC - Issue detected: Automated monitoring systems flagged a spike in database query latency.
14:32 UTC - Initial investigation began: The DevOps team noticed that the primary database cluster was showing increased load and latency.
14:35 UTC - Incident escalated: The issue was escalated to the on-call database administrator (DBA).
14:40 UTC - Misleading path: The DBA initially suspected a DDoS attack due to the sudden spike in load and began analysing network traffic.
14:45 UTC - Further investigation: After ruling out DDoS, the team began checking application logs and found frequent database connection timeouts.
14:50 UTC - Root cause identified: The team discovered a recent configuration change in the database connection pool settings that reduced the maximum number of connections.
15:00 UTC - Resolution initiated: The connection pool settings were reverted to previous values.
15:10 UTC - Service recovery: The database cluster gradually returned to normal operation, and the messaging service began processing messages again.
15:15 UTC - Full service restored: All users could log in and send/receive messages without issues.

Root Cause and Resolution
Root Cause: The outage was caused by an incorrect change in the configuration of the database connection pool settings. Specifically, the maximum number of connections allowed per application instance was reduced from 100 to 10 during a routine configuration update. This reduction was intended to alleviate pressure on the database during peak hours, but it inadvertently led to the database being unable to handle the incoming connections from all active application instances. The sudden reduction in available connections caused a bottleneck, leading to increased query latency and eventual timeouts. This overwhelmed the primary database cluster, which in turn caused a complete service outage.
Resolution: Upon identifying the root cause, the team reverted the database connection pool settings to their original values. This allowed the database to once again handle the required number of connections, relieving the bottleneck and restoring normal operation. Additionally, the team manually restarted the affected database nodes to ensure a full recovery. The service was fully restored within 45 minutes of the initial outage.

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
