# 0x0A. Configuration Management

## Background Context

During my tenure at SlideShare, I worked on an auto-remediation tool called **Skynet**. This tool was responsible for monitoring, scaling, and fixing our cloud infrastructure. One of the key components I used was a parallel job-execution system called **MCollective**. With MCollective, I could execute commands on one or multiple servers simultaneously. By applying filters (such as server hostname or other metadata), I could target specific sets of servers. However, a bug in my code led to unexpected consequences.

Here's what happened:

1. **Nil Filter Issue**: At some point, a bug caused my code to send `nil` as an argument to MCollective's filter method.
2. **Termination Action**: Unfortunately, the action I sent was to terminate the selected servers.

The result? Chaos ensued. I initiated a parallel job-execution, expecting routine maintenance. Instead, I inadvertently shut down **75% of our conversion infrastructure servers** at SlideShare. Users were unable to convert their PDFs, PowerPoint presentations, and videos. Not ideal!

## Puppet to the Rescue

Thankfully, we had Puppet in place. Within an hour, we restored our infrastructure to normal operation. Imagine the alternative: manual server launches, configurations, code imports, process startups, and bug fixes. Puppet saved the day!

While writing Puppet code for your infrastructure requires an initial investment of time and effort, it's undoubtedly a **must-have** for long-term stability.

---

**Resources:**

- Intro to Configuration Management
- Puppet resource type: file
- Puppet’s Declarative Language: Modeling

---


