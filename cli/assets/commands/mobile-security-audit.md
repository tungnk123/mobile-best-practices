---
description: Audit mobile app for security vulnerabilities and best practices
---

Perform a comprehensive security audit of my mobile application:

1. **Scan for Common Vulnerabilities**:
   - Check for hardcoded API keys, secrets, or credentials
   - Review data storage (SharedPreferences, UserDefaults, Keychain)
   - Verify SSL/TLS certificate pinning implementation
   - Check for sensitive data in logs or crash reports
   - Review authentication and session management
   - Check for root/jailbreak detection

2. **Review Against Security Best Practices**:
   - Use the mobile-best-practices skill to search security domain
   - Cross-reference findings with OWASP Mobile Top 10
   - Check platform-specific security guidelines

3. **Generate Security Report**:
   - List all vulnerabilities found (high/medium/low severity)
   - Provide remediation steps for each issue
   - Include code examples of secure implementations
   - Reference relevant documentation

Focus on $ARGUMENTS if provided, otherwise audit the entire project.
