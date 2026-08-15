# Security vulnerability scanner (for container) report.

This docker image and packages are not pinned to any version, as such the repository doesn't change and the vulnerabilities present are based on the build time.

To help give users and idea of what the latest dockerhub build/images looks like, this report is produced.

The scanner uses [Grype](https://github.com/anchore/grype/) within a [Github Scan Action](https://github.com/anchore/scan-action) 

---
08-15-2026 17:04:59
---
````
NAME           INSTALLED   TYPE  VULNERABILITY   SEVERITY  EPSS         RISK  
python3        3.14.7-r1   apk   CVE-2026-15308  High      0.6% (47th)  0.5   
python3        3.14.7-r1   apk   CVE-2025-15367  Medium    0.3% (24th)  0.2   
busybox        1.37.0-r31  apk   CVE-2025-60876  Medium    0.3% (21st)  0.2   
busybox-binsh  1.37.0-r31  apk   CVE-2025-60876  Medium    0.3% (21st)  0.2   
ssl_client     1.37.0-r31  apk   CVE-2025-60876  Medium    0.3% (21st)  0.2   
python3        3.14.7-r1   apk   CVE-2026-4360   Medium    0.3% (20th)  0.1   
````
