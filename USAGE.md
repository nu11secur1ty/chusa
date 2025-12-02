==================================================== CHUSA SQL INJECTION
SCANNER UI - COMPLETE DOCUMENTATION
==================================================== Author:
nu11secur1ty Repository: https://github.com/nu11secur1ty/chusa Version:
2.0.0 ====================================================

■ OVERVIEW ● Professional web interface for CHUSA SQL injection scanner
● High-performance, responsive control panel ● Dual scan modes (URL &
File-based) ● Real-time terminal output with syntax highlighting ●
Memory-optimized for large file handling

■ FEATURES ✓ URL Mode (-u): Direct URL scanning ✓ File Mode (-r
exploit.txt): Burp/Proxy file scanning ✓ Aggressive Testing: --level=5
--risk=3 pre-configured ✓ Real-time Output: Live streaming with color
coding ✓ Gadget Management: Collapsible control panels ✓ Performance
Optimized: Virtual scrolling, batch updates ✓ Security Features: Input
validation, confirmation dialogs ✓ Responsive Design: Works on desktop &
mobile

■ INSTALLATION 1. Prerequisites: - Node.js 16+ OR Python 3.8+ - Chrome
90+, Firefox 88+, or Edge 90+ - 500MB free disk space

2.  Quick Start: git clone https://github.com/nu11secur1ty/chusa.git cd
    chusa

    # Node.js:

    npm install npm start

    # Python:

    pip install -r requirements.txt python server.py

    Open: http://localhost:8080

■ UI LAYOUT ┌─────────────────────────────────────┐ │ HEADER: Status &
Mode Indicators │ ├─────────────────────────────────────┤ │ 1. TARGET
CONFIGURATION │ │ • URL input field │ │ • Mode selector (URL/File) │ │ •
File upload (10MB max) │ │ • Parameter input for file mode │
├─────────────────────────────────────┤ │ 2. COMMAND BUTTONS │ │ • FULL
SCAN • DUMP │ │ • DUMP ALL • DATABASES │ │ • TABLES • COLUMNS │ │ •
USERS • OS SHELL │ │ • OS PWN │ │ • \[CTRL+C\] STOP SCAN │
├─────────────────────────────────────┤ │ 3. REAL-TIME TERMINAL │ │ •
Live output streaming │ │ • Color-coded messages │ │ • Auto-scroll │
└─────────────────────────────────────┘

■ SIDEBAR GADGETS • CHUSA CONTROLLER: Start/Stop/Restart/Test • ENGINE
STATUS: Threads, Active Scans, Uptime • ACTIVE PARAMETERS: Current scan
settings • PAYLOAD PRESETS: BEUS, TIMEBASED, UNION, ERROR • ENGINE
SETTINGS: Toggle aggressive/stealth/verbose • SCAN HISTORY: Previous
scan results • TEST TARGETS: Quick URL presets

■ SCAN MODES 1. URL MODE (-u): Enter: http://target.com/page.php?id=1
Command: python chusa.py -u "URL" --level=5 --risk=3

2.  FILE MODE (-r exploit.txt): Steps:
    1.  Capture request in Burp/Proxy
    2.  Save as exploit.txt
    3.  Upload via UI
    4.  Enter parameter name (e.g., "email")
    5.  Click any scan button Command: python chusa.py -r exploit.txt -p
        "parameter"

■ COMMAND REFERENCE
┌──────────────┬──────────────┬─────────────────────────────┬─────────┐
│ BUTTON │ COMMAND │ DESCRIPTION │ RISK │
├──────────────┼──────────────┼─────────────────────────────┼─────────┤
│ FULL SCAN │ --scan │ Comprehensive assessment │ CRITICAL│ │ DUMP │
--dump │ Extract table data │ HIGH │ │ DUMP ALL │ --dump-all │ Extract
all databases │ VERY HIGH│ │ DATABASES │ --dbs │ List databases │ MEDIUM
│ │ TABLES │ --tables │ List tables │ MEDIUM │ │ COLUMNS │ --columns │
Show table structure │ MEDIUM │ │ USERS │ --users │ Extract credentials
│ HIGH │ │ OS SHELL │ --os-shell │ Command execution │ CRITICAL│ │ OS
PWN │ --os-pwn │ System takeover │ CRITICAL│
└──────────────┴──────────────┴─────────────────────────────┴─────────┘

■ DEFAULT PARAMETERS • --level=5 • --risk=3 • --technique=BEUS • --batch
• --random-agent • --timeout=30 • --retries=3 • --tamper=space2comment

■ KEYBOARD SHORTCUTS • Ctrl+Enter → Start full scan • Ctrl+C → Stop
current scan • Ctrl+L → Clear terminal • Escape → Close modal/cancel •
Ctrl+Shift+D → Download results

■ PERFORMANCE OPTIMIZATIONS • Virtual Terminal: Limits to 1000 lines,
auto-cleanup • Batch Updates: Groups log messages for 60fps performance
• Memory Management: Cleans up old DOM elements • File Upload: 10MB
limit with progress tracking • Connection Pooling: Efficient EventSource
handling

■ SECURITY WARNINGS ⚠️ LEGAL USE ONLY - AUTHORIZATION REQUIRED • Always
obtain written permission before scanning • Use only on systems you own
or have explicit authorization • May trigger WAF/IDS alerts • Logs may
be recorded by security systems • Use in isolated environments for
testing

■ TROUBLESHOOTING PROBLEM: File upload fails SOLUTION: Check file size
(\<10MB), verify permissions

PROBLEM: Scan doesn't start SOLUTION: Verify backend is running, check
console logs

PROBLEM: Terminal freezes SOLUTION: Clear terminal (Ctrl+L), check
memory usage

PROBLEM: No output received SOLUTION: Verify EventSource connection,
check firewall

PROBLEM: UI lags with large files SOLUTION: Reduce terminal history,
close unused tabs

■ API ENDPOINTS POST /api/upload-file → Upload exploit.txt POST
/api/scan → Start new scan GET /api/stream/:id → Real-time output stream
POST /api/stop/:id → Stop running scan GET /api/files → List scan
results GET /api/file/:name → Download result file GET /api/check-upload
→ Check existing file POST /api/clear-upload → Clear uploaded file

■ TEST TARGETS (PRESETS) 1.
http://testphp.vulnweb.com/artists.php?artist=1 2.
https://zero.webappsecurity.com/login.html 3. http://demo.testfire.net/

■ PAYLOAD PRESETS • BEUS: Boolean+Error+Union+Stacked queries •
TIMEBASED: SLEEP(), BENCHMARK() based injection • UNION: Classic UNION
SELECT injection • ERROR: Error-based information extraction

■ SETTINGS CONFIGURATION • Aggressive Mode: Enable/disable level=5
risk=3 • Stealth Mode: Reduced noise, slower scanning • Auto-save
Results: Automatic file storage • Verbose Output: Detailed logging

■ BROWSER COMPATIBILITY ✅ Chrome 90+ → Full support ✅ Firefox 88+ →
Full support\
✅ Edge 90+ → Full support ⚠️ Safari 14+ → Limited support ✅ Opera 76+
→ Full support

■ FILE STRUCTURE chusa-ui/ ├── index.html \# Main interface ├──
server.js \# Node.js backend ├── server.py \# Python backend ├──
package.json \# Node.js dependencies ├── requirements.txt \# Python
dependencies ├── chusa_output/ \# Scan results directory └── uploads/ \#
Temporary file storage

■ DEVELOPMENT For developers: • No framework dependencies (Vanilla JS) •
Modular CSS with CSS variables • Event-driven architecture • RESTful API
design • Error boundary implementation

■ CONTRIBUTING 1. Fork the repository 2. Create feature branch 3. Follow
existing code style 4. Add tests for new features 5. Submit pull request

■ LICENSE MIT License - See LICENSE file for details Copyright (c) 2024
nu11secur1ty

■ SUPPORT • GitHub Issues: Bug reports & feature requests • Security
Reports: Use GitHub security advisories • Community: GitHub discussions

■ VERSION HISTORY 2.0.0 (2024-01-15) - Complete performance rewrite
1.5.0 (2023-11-20) - Added file mode support 1.0.0 (2023-09-10) -
Initial release

■ CREDITS Author: nu11secur1ty Contributors: Security research community
Inspired by: SQLMap, OWASP testing guide

■ DISCLAIMER This tool is for: ✓ Authorized penetration testing ✓
Security research (with permission) ✓ Educational purposes ✓
Vulnerability assessment (authorized)

NOT for: ✗ Unauthorized access attempts ✗ Malicious activities\
✗ Illegal hacking ✗ Network disruption
