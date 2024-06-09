### Postmortem: The Great Login Fiasco

#### Issue Summary
- **Duration**: Our login service was MIA for 2 hours, from 10:00 AM to 12:00 PM (UTC) on June 7, 2024.
- **Impact**: Users were locked out, unable to log in. Approximately 60% of our user base (around 12,000 users) were affected, experiencing either timeouts or error messages. It was like everyone forgot their keys at home.
- **Root Cause**: A sneaky database query decided to throw a tantrum, causing a deadlock that froze the login process.


#### Timeline
- **10:05 AM**: 🚨 **Alert**: Monitoring system starts screaming about failed login attempts.
- **10:10 AM**: 🕵️‍♂️ **First Response**: On-call engineer dives into the logs, notices a spike in database query times.
- **10:20 AM**: 🌐 **Network Blame**: Initially thought to be a network issue. Network team is looped in.
- **10:35 AM**: ❌ **False Lead**: Network team reports all clear. Time to rethink.
- **10:50 AM**: 🔍 **Wild Goose Chase**: Investigate potential memory leaks in the application server, but hit a dead end.
- **11:05 AM**: 📈 **Database Team Called**: Escalate to the database team for a closer look.
- **11:20 AM**: 🥨 **Deadlock Found**: Database team uncovers the problematic query causing the deadlock.
- **11:30 AM**: 🛠 **Temporary Fix**: Restart affected database nodes to clear the deadlock.
- **11:45 AM**: ⚡ **Hotfix Applied**: Optimized query deployed, restoring normal operation.
- **12:00 PM**: ✅ **Resolution Confirmed**: Monitoring confirms everything is back to normal.

#### Root Cause and Resolution
- **Root Cause**: The issue stemmed from an overzealous SQL query in our authentication service that locked multiple rows in the users table, leading to a deadlock. This essentially caused the login service to hit a traffic jam.
- **Resolution**: First, the database team cleared the deadlock by restarting the affected nodes. Then, they rolled out a hotfix with an optimized query that handled locks more efficiently, ensuring no more deadlocks.

#### Corrective and Preventative Measures
- **Improvements**:
  - Strengthen our SQL query optimization process during code reviews.
  - Enhance our database performance monitoring to catch issues early.
  - Implement robust deadlock detection and automated resolution tools.
  
- **Tasks**:
  1. **Optimize SQL Queries**: Conduct a detailed review and optimization of all critical queries in the authentication service.
  2. **Enhance Monitoring**: Deploy advanced monitoring tools to track query performance and detect deadlocks in real-time.
  3. **Automated Deadlock Resolution**: Develop scripts that can automatically detect and resolve deadlocks.
  4. **Code Review Updates**: Update the code review checklist to include SQL query optimization and deadlock prevention.
  5. **Load Testing**: Conduct load testing to simulate high-concurrency scenarios and identify potential performance bottlenecks.
  6. **Database Indexing**: Review and improve indexing strategies for all critical database tables.

By addressing these tasks, we aim to prevent similar incidents in the future and ensure a smoother, more reliable login experience for our users.

---
