# SSH Log Analyzer

A Python tool that scans Linux SSH authentication logs to detect brute-force attacks and flag possible account compromises.

## What it does

1. **Filters** the log for failed login attempts
2. **Extracts** the source IP address from each attempt
3. **Counts** failures per IP to spot brute-force behavior
4. **Correlates** failures with successful logins and raises an alert when an IP that failed 5+ times later gets in

## Why it matters

Failed logins alone are noise. Bots hit every internet-facing server constantly. The real red flag is **many failures followed by a success**, which means an attacker likely guessed the password. This tool surfaces that automatically.

## Example output

```
192.0.2.22 failed 1 times
203.0.113.45 failed 38 times
198.51.100.7 failed 6 times
198.51.100.200 failed 14 times
ALERT: possible break-in from 198.51.100.200
```

**Reading the results:**
- `192.0.2.22`: 1 failure, a user typo, not a threat
- `203.0.113.45`: 38 rapid failures across common usernames (admin, root, oracle), a password-guessing bot
- `198.51.100.7`: 6 failures spread over an hour, a slow attack designed to avoid detection
- `198.51.100.200`: 14 failures then a successful login, a **likely compromise**

## How to run

Requires Python 3. No extra packages needed.

```
python analyzer.py
```

Place an SSH auth log named `auth.log` in the same folder. The included `auth.log` is sample data with simulated attacks for testing.

## Scope

This is a **detection** tool. It analyzes logs after the fact and does not block attackers. Response steps would include blocking the IP at the firewall, resetting the compromised account's password, and terminating active sessions.

## Planned improvements

- Sort results by number of failures
- Accept any log file as a command-line argument
- Configurable alert threshold
- Export findings to a report file
