# CHUSA SQL Injection Scanner UI  
### Complete Documentation – Version 2.0.0  
Author: nu11secur1ty  
Repository: https://github.com/nu11secur1ty/chusa  

## OVERVIEW
● Professional web interface for CHUSA SQL injection scanner  
● High-performance, responsive control panel  
● Dual scan modes (URL & File-based)  
● Real-time terminal output with syntax highlighting  
● Memory-optimized for large file handling  

## FEATURES
✓ URL Mode (-u): Direct URL scanning  
✓ File Mode (-r exploit.txt): Burp/Proxy file scanning  
✓ Aggressive Testing: --level=5 --risk=3 pre-configured  
✓ Real-time Output: Live streaming with color coding  
✓ Gadget Management: Collapsible control panels  
✓ Performance Optimized: Virtual scrolling, batch updates  
✓ Security Features: Input validation, confirmation dialogs  
✓ Responsive Design: Desktop & mobile  

## INSTALLATION
### Prerequisites
- Node.js 16+ or Python 3.8+  
- Chrome 90+, Firefox 88+, Edge 90+  
- 500MB free disk  

### Quick Start
git clone https://github.com/nu11secur1ty/chusa.git  
cd chusa  

Node.js:  
npm install  
npm start  

Python:  
pip install -r requirements.txt  
python server.py  

Open: http://localhost:8080  

## UI LAYOUT
┌─────────────────────────────────────┐  
│ HEADER: Status & Mode Indicators    │  
├─────────────────────────────────────┤  
│ 1. TARGET CONFIGURATION             │  
│ • URL input field                   │  
│ • Mode selector (URL/File)          │  
│ • File upload (10MB max)            │  
│ • Parameter input for file mode     │  
├─────────────────────────────────────┤  
│ 2. COMMAND BUTTONS                  │  
│ • FULL SCAN • DUMP                  │  
│ • DUMP ALL • DATABASES              │  
│ • TABLES • COLUMNS                  │  
│ • USERS • OS SHELL                  │  
│ • OS PWN                            │  
│ • [CTRL+C] STOP SCAN                │  
├─────────────────────────────────────┤  
│ 3. REAL-TIME TERMINAL               │  
│ • Live output streaming             │  
│ • Color-coded messages              │  
│ • Auto-scroll                       │  
└─────────────────────────────────────┘  

## SIDEBAR GADGETS
- CHUSA Controller  
- Engine Status  
- Active Parameters  
- Payload Presets  
- Engine Settings  
- Scan History  
- Test Targets  

## SCAN MODES
### URL MODE (-u)
python chusa.py -u "URL" --level=5 --risk=3  

### FILE MODE (-r exploit.txt)
python chusa.py -r exploit.txt -p "parameter"  

## COMMAND REFERENCE
FULL SCAN —scan  
DUMP —dump  
DUMP ALL —dump-all  
DATABASES —dbs  
TABLES —tables  
COLUMNS —columns  
USERS —users  
OS SHELL —os-shell  
OS PWN —os-pwn  

## DEFAULT PARAMETERS
--level=5  
--risk=3  
--technique=BEUS  
--batch  
--random-agent  
--timeout=30  
--retries=3  
--tamper=space2comment  

## KEYBOARD SHORTCUTS
Ctrl+Enter – full scan  
Ctrl+C – stop scan  
Ctrl+L – clear terminal  
Escape – cancel  
Ctrl+Shift+D – download results  

## PERFORMANCE
Virtual terminal, batch updates, memory cleanup, 10MB file limit, EventSource pooling  

## SECURITY WARNINGS
AUTHORIZED USE ONLY  

## TROUBLESHOOTING
File upload fails → check size  
Scan won't start → backend offline  
Terminal freeze → clear terminal  
No output → check firewall  
UI lag → reduce history  

## API ENDPOINTS
POST /api/upload-file  
POST /api/scan  
GET /api/stream/:id  
POST /api/stop/:id  
GET /api/files  
GET /api/file/:name  
GET /api/check-upload  
POST /api/clear-upload  

## TEST TARGETS
http://testphp.vulnweb.com/artists.php?artist=1  
https://zero.webappsecurity.com/login.html  
http://demo.testfire.net/  

## PAYLOAD PRESETS
BEUS, TIMEBASED, UNION, ERROR  

## SETTINGS
Aggressive, stealth, verbose, auto-save  

## BROWSER COMPATIBILITY
Chrome, Firefox, Edge, Opera (Safari limited)  

## FILE STRUCTURE
chusa-ui/...  

## DEVELOPMENT
Vanilla JS, modular CSS, REST API  

## CONTRIBUTING
Fork → Branch → Style → Tests → PR  

## LICENSE
MIT License  

## SUPPORT
GitHub Issues, Security Advisories, Discussions  

## VERSION HISTORY
2.0.0 – performance rewrite  
1.5.0 – file mode  
1.0.0 – initial  

## DISCLAIMER
Authorized testing only  
