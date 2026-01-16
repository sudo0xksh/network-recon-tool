# 🌐 Network Recon Tool

**Network Recon Tool** is a Python-based CLI utility designed to perform
basic network reconnaissance on one or multiple targets.

It follows a simple recon workflow:
1. Ping the target
2. Resolve DNS information
3. Trace the network path
4. Scan open ports

No automation magic — just clear steps and raw output.

---

## 🧠 What Is This Tool?

This tool helps beginners understand how **network reconnaissance actually works**
by chaining commonly used commands in the correct order.

It supports:
- Single target scanning
- Multiple target scanning via a `.txt` file

Each target is processed independently.

---

## 🚀 Features

- Accepts a single domain or IP as input
- Supports multiple targets from a text file
- Validates target format before scanning
- Performs:
  - `ping`
  - `nslookup`
  - `tracert`
  - `nmap`
- Skips unreachable or invalid targets
- Displays raw command output directly in terminal

---

## 🧪 Usage

### ▶️ Single Target

```bash
python network_scanner.py google.com
