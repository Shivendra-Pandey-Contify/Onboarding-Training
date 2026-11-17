# Day 01 – Linux Commands for Backend Development

**Environment:** Fedora Workstation 45 (running on UTM) · Shell: `bash` · Terminal: Ptyxis
**Date:** 17 Nov 2026
**Objective:** Learn essential Linux commands for filesystem navigation, file management, searching, log analysis, permissions, process management and disk monitoring, with a backend (Django-style) workflow in mind.

---

## Table of Contents

1. [Filesystem Navigation](#1-filesystem-navigation)
2. [File Management](#2-file-management)
3. [Viewing and Writing File Content](#3-viewing-and-writing-file-content)
4. [Searching and Log Analysis](#4-searching-and-log-analysis)
5. [Permissions and Ownership](#5-permissions-and-ownership)
6. [Process Management](#6-process-management)
7. [Disk Management](#7-disk-management)
8. [Important Linux Operators](#8-important-linux-operators)
9. [Practical Backend Use Cases](#9-practical-backend-use-cases)
10. [Hands-on Practice Log (Annotated)](#10-hands-on-practice-log-annotated)
11. [Mistakes and Lessons Learned](#11-mistakes-and-lessons-learned)
12. [Quick Cheat Sheet](#12-quick-cheat-sheet)
13. [Key Learnings](#13-key-learnings)

---

## 1. Filesystem Navigation

| Command | Description | Common Syntax | Notes |
|---|---|---|---|
| `pwd` | Print the current working directory | `pwd` | Shows the absolute path, e.g. `/home/shivendra/linux-practice` |
| `ls` | List files and directories | `ls -la` | `-l` long format, `-a` include hidden files, `-h` human-readable sizes |
| `cd` | Change directory | `cd project/` | `cd` alone or `cd ~` goes home; `cd -` returns to the previous directory |
| `mkdir` | Create directories | `mkdir -p backend/apps` | `-p` creates parent directories and does not fail if they exist |
| `touch` | Create an empty file (or update its timestamp) | `touch app.py` | Useful for quickly scaffolding files |

### Useful `ls` flags

| Flag | Meaning |
|---|---|
| `-l` | Long listing (permissions, owner, size, date) |
| `-a` | Show hidden files (names starting with `.`) |
| `-h` | Human-readable sizes (K, M, G), used with `-l` |
| `-la` | Long listing including hidden files |
| `-t` | Sort by modification time |
| `-R` | Recursive listing |

### Reading `ls -l` output

```text
drwxr-xr-x. 1 shivendra shivendra  80 Nov 17 10:42 logs
-rw-r--r--. 1 shivendra shivendra   0 Nov 17 10:41 notes.txt
```

| Part | Meaning |
|---|---|
| `d` / `-` | First character: `d` = directory, `-` = regular file |
| `rwxr-xr-x` | Permissions for owner, group, others (3 characters each) |
| `.` | SELinux security context present (Fedora/RHEL feature) |
| `1` | Hard link count |
| `shivendra shivendra` | Owner and group |
| `80` | Size in bytes (use `-h` for K/M/G) |
| `Nov 17 10:42` | Last modified time |
| `logs` | File or directory name |

### Path types

| Type | Example | Description |
|---|---|---|
| Absolute path | `/home/shivendra/linux-practice` | Starts from root `/`, works from anywhere |
| Relative path | `../logs` | Relative to the current directory |
| Home shortcut | `~/Desktop` | `~` expands to `/home/<user>` |

> **Linux is case-sensitive.** `Desktop` and `desktop` are different names.

---

## 2. File Management

| Command | Description | Common Syntax | Notes |
|---|---|---|---|
| `cp` | Copy files/directories | `cp -r source/ destination/` | `-r` is required for directories |
| `mv` | Move or rename | `mv old.py new.py` | Same command for both operations |
| `rm` | Remove files/directories | `rm -r folder/` | **No recycle bin. Deleted means gone.** |
| `cat` | Display file contents | `cat settings.py` | Best for small files; can combine several files |
| `less` | Read large files page by page | `less application.log` | `q` quit, `/word` search, `Space` next page, `b` previous page, `G` end, `g` start |

### Safe deletion

| Command | Behaviour |
|---|---|
| `rm file.txt` | Deletes immediately |
| `rm -i file.txt` | Asks for confirmation before deleting |
| `rm -r folder/` | Deletes a directory and its contents recursively |
| `rm -rf folder/` | Force + recursive, no prompts (**dangerous**, double-check the path) |

### Copy, move and rename patterns

```bash
cp notes.txt backup-notes.txt         # copy file
cp python.txt projects/               # copy into a directory
cp -r projects backup-projects        # copy a directory recursively
mv notes.txt mynotes.txt              # rename
mv mynotes.txt logs/                  # move into a directory
mv logs/mynotes.txt notes.txt         # move back (and rename)
```

---

## 3. Viewing and Writing File Content

### Redirection

| Operator | Behaviour |
|---|---|
| `>` | Writes output to a file and **overwrites** existing content |
| `>>` | **Appends** output to the end of a file |

```bash
echo "Server started" > app.log          # creates / overwrites
echo "New request received" >> app.log   # appends
```

### Writing with `cat`

```bash
cat > notes.txt      # type text, then press Ctrl+D to save (overwrites)
cat >> notes.txt     # type text, then press Ctrl+D to save (appends)
cat notes.txt backup-notes.txt   # print several files one after another
```

> Press **Enter before Ctrl+D**. Otherwise the file has no trailing newline and the shell prompt appears on the same line as the file content (this happened in the practice log).

### Generating test data with a loop

```bash
for i in $(seq 1 500); do
  echo "Line $i: Fedora on UTM is running Linux practice with less command"
done > ~/practice.txt
```

| Part | Meaning |
|---|---|
| `seq 1 500` | Generates numbers 1 to 500 |
| `$( ... )` | Command substitution |
| `for ... do ... done` | Loop |
| `> ~/practice.txt` | Sends all loop output to a file in the home directory |

---

## 4. Searching and Log Analysis

| Command | Description | Common Syntax |
|---|---|---|
| `grep` | Search text inside files | `grep -in "error" app.log` |
| `find` | Search files/directories by name, type, etc. | `find . -name "*.py"` |
| `head` | Show the first lines | `head -n 20 app.log` |
| `tail` | Show the last lines | `tail -n 50 app.log` |

### `grep` flags

| Flag | Meaning | Example |
|---|---|---|
| *(none)* | Case-sensitive match | `grep "Python" python.txt` |
| `-n` | Show line numbers | `grep -n "Python" python.txt` |
| `-i` | Ignore case | `grep -i "error" logs/application.log` |
| `-v` | Invert match (lines **not** containing the text) | `grep -v "Python" python.txt` |
| `-c` | Count matching lines | `grep -ic "error" logs/application.log` |
| `-r` | Search recursively through directories | `grep -rn "ERROR" logs/` |

### `find` options

| Option | Meaning | Example |
|---|---|---|
| `-name` | Match by file name (supports wildcards) | `find . -name "*.log"` |
| `-type f` | Files only | `find . -type f` |
| `-type d` | Directories only | `find . -type d` |

### Live log monitoring

```bash
tail -f application.log        # follow a log in real time (Ctrl+C to stop)
grep -rn "ERROR" logs/         # search every file under logs/ with line numbers
```

---

## 5. Permissions and Ownership

| Command | Description | Common Syntax |
|---|---|---|
| `chmod` | Change file permissions | `chmod 755 deploy.sh` |
| `chown` | Change file ownership | `sudo chown user:group file.py` |

### Permission values

| Permission | Letter | Number |
|---|---|---|
| Read | `r` | 4 |
| Write | `w` | 2 |
| Execute | `x` | 1 |

### Common modes

| Mode | Symbolic | Owner | Group | Others | Typical use |
|---|---|---|---|---|---|
| `755` | `rwxr-xr-x` | RWX | R-X | R-X | Scripts, executables, directories |
| `644` | `rw-r--r--` | RW- | R-- | R-- | Normal files |
| `600` | `rw-------` | RW- | --- | --- | Private files (keys, secrets) |
| `777` | `rwxrwxrwx` | RWX | RWX | RWX | **Avoid.** Insecure |

### How the number is calculated

```text
755 → Owner: 4+2+1 = 7 (rwx)   Group: 4+0+1 = 5 (r-x)   Others: 4+0+1 = 5 (r-x)
644 → Owner: 4+2+0 = 6 (rw-)   Group: 4+0+0 = 4 (r--)   Others: 4+0+0 = 4 (r--)
```

### Symbolic form

```bash
chmod +x deploy.sh      # add execute for everyone
chmod u+x deploy.sh     # add execute for the owner only
chmod go-w file.txt     # remove write from group and others
```

---

## 6. Process Management

| Command | Description | Common Syntax |
|---|---|---|
| `ps` | Show running processes | `ps aux` |
| `top` | Monitor processes in real time | `top` (press `q` to quit) |
| `kill` | Send a signal to a process | `kill PID` |
| `lsof` | List open files and inspect port usage | `lsof -i :8000` |

### Useful process commands

```bash
ps aux | grep python     # find python processes (the grep itself also appears)
pgrep -af python         # cleaner: list PIDs with full command lines
kill PID                 # polite termination (SIGTERM)
kill -9 PID              # force kill (SIGKILL), last resort
```

### Signals

| Command | Signal | Behaviour |
|---|---|---|
| `kill PID` | `SIGTERM` (15) | Asks the process to shut down gracefully |
| `kill -9 PID` | `SIGKILL` (9) | Kills immediately, with no cleanup |

> Prefer `kill PID`. Use `kill -9` only if the process does not respond.

### Reading `ps aux`

```text
USER       PID %CPU %MEM    VSZ   RSS TTY   STAT START   TIME COMMAND
shivend+ 11673  0.0  0.0 232120  2100 pts/0 S+   15:18   0:00 sleep 300
```

| Column | Meaning |
|---|---|
| `USER` | Owner of the process |
| `PID` | Process ID (used with `kill`) |
| `%CPU` / `%MEM` | CPU and memory usage |
| `STAT` | State (`S` sleeping, `R` running, `+` foreground) |
| `COMMAND` | The command that started the process |

### Reading `top` (from the practice session)

| Line | Meaning |
|---|---|
| `load average: 0.23, 0.10, 0.05` | System load over 1, 5 and 15 minutes (low = idle) |
| `Tasks: 240 total, 1 running` | Process counts by state |
| `%Cpu(s): ... 96.3 id` | 96.3% of CPU is idle |
| `MiB Mem: 3886.1 total, 255.8 free` | RAM overview; `buff/cache` is reclaimable |
| `MiB Swap: 3886.0 total, 1442.8 used` | Swap in use means RAM pressure |
| Top processes | `ptyxis` (terminal) and `gnome-shell` (desktop) used the most memory |

---

## 7. Disk Management

| Command | Description | Common Syntax |
|---|---|---|
| `df` | Show filesystem disk usage | `df -h` |
| `du` | Show directory/file space usage | `du -sh project/` |

### Flags

| Flag | Meaning |
|---|---|
| `-h` | Human-readable sizes |
| `-s` | Summary only (one total line) |
| `-d 1` | Limit depth to 1 level (for `du`) |

### Useful disk commands

```bash
df -h                       # all filesystems
df -h .                     # filesystem containing the current directory
du -sh .                    # total size of the current directory
du -h -d 1 . | sort -h      # size of each subfolder, smallest to largest
```

### Reading `df -h` (from the practice session)

| Filesystem | Size | Used | Avail | Use% | Mounted on | Comment |
|---|---|---|---|---|---|---|
| `/dev/vda3` | 30G | 7.7G | 22G | 27% | `/` and `/home` | Main disk; root and home share it |
| `/dev/vda2` | 2.0G | 700M | 1.2G | 39% | `/boot` | Boot files |
| `/dev/vda1` | 599M | 38M | 562M | 7% | `/boot/efi` | EFI system partition |
| `tmpfs` | 1.9G | 8.0K | 1.9G | 1% | `/tmp` | Lives in RAM |
| `/dev/sda1` | 2.8G | 2.8G | 0 | 100% | `/run/media/.../Fedora-WS-Live-45` | Installer ISO, always 100% (read-only), not a problem |

---

## 8. Important Linux Operators

| Operator | Purpose | Example |
|---|---|---|
| `.` | Current directory | `find . -name "*.py"` |
| `..` | Parent directory | `cd ..` |
| `~` | Home directory | `cd ~` |
| `-` | Previous directory (with `cd`) | `cd -` |
| `*` | Wildcard (any characters) | `ls *.txt` |
| `>` | Redirect and overwrite | `echo "x" > file` |
| `>>` | Redirect and append | `echo "x" >> file` |
| `\|` | Pipe output into another command | `ps aux \| grep python` |
| `&&` | Run next command only if previous succeeds | `mkdir app && cd app` |
| `;` | Run commands sequentially, regardless of result | `cd app; ls` |
| `sudo` | Run with elevated privileges | `sudo chown user file` |

---

## 9. Practical Backend Use Cases

| # | Task | Command |
|---|---|---|
| 1 | Locate the Django settings file | `find . -name "settings.py"` |
| 2 | Search application errors | `grep -in "error" application.log` |
| 3 | Count errors in a log | `grep -ic "error" application.log` |
| 4 | Monitor live application logs | `tail -f application.log` |
| 5 | Find the process using port 8000 | `lsof -i :8000` |
| 6 | Terminate a process gracefully | `kill PID` |
| 7 | Check server disk space | `df -h` |
| 8 | Check project directory size | `du -sh project/` |
| 9 | Make a deployment script executable | `chmod +x deploy.sh` |
| 10 | Find the biggest folders | `du -h -d 1 . \| sort -h` |

### Typical troubleshooting workflow

```bash
# 1. Is the app running and which process is it?
ps aux | grep python

# 2. Is something already using the port?
lsof -i :8000

# 3. What do the logs say?
tail -n 50 logs/application.log
grep -in "error" logs/application.log

# 4. Is the disk full?
df -h

# 5. Stop a misbehaving process
kill PID
```

---

## 10. Hands-on Practice Log (Annotated)

### Practice 1: `~/linux-practice`

**Goal:** Create a workspace and practise navigation, copy/move/delete, redirection, `less`, `grep`, `find`, `top`, `df` and `du`.

| Step | Commands | What it did |
|---|---|---|
| Create workspace | `mkdir linux-practice`, `cd linux-practice` | New working directory |
| Create files | `touch notes.txt python.txt linux.txt` | Three empty files |
| Create folders | `mkdir projects logs` | Two directories |
| Inspect | `ls`, `ls -l`, `ls -lh`, `ls -la` | Compared listing formats |
| Navigate | `cd projects`, `cd ..`, `cd /`, `cd ~`, `cd -` | Practised relative, absolute and previous-directory moves |
| Nested dirs | `mkdir -p project/src/controller` | Created three levels in one command |
| Copy | `cp notes.txt backup-notes.txt`, `cp python.txt projects/`, `cp -r projects backup-projects` | File, file-to-folder and recursive copy |
| Move/rename | `mv notes.txt mynotes.txt`, `mv mynotes.txt logs/`, `mv logs/mynotes.txt notes.txt` | Rename, move, move back |
| Delete | `rm python.txt`, `rm -i linux.txt`, `rm -r backup-projects` | Plain, interactive and recursive delete |
| Write | `echo "..." > notes.txt`, `cat > notes.txt`, `cat >> notes.txt` | Overwrite vs append |
| Large file | `for i in $(seq 1 500) ...` then `less practice.txt` | Generated 500 lines and paged through them |
| Search | `grep "Python"`, `grep -n`, `grep -v` | Match, line numbers, inverted match |
| Find | `find . -name "python.txt"`, `find . -name "*.py"`, `find . -type d` | Search by name, wildcard and type |
| Monitor | `top` | Live process and memory view |
| Disk | `df`, `df -h`, `du -sh`, `du -sh .` | Filesystem and directory size |

**Final state of `~/linux-practice`:**

```text
linux-practice/
├── backup-notes.txt
├── hello.py
├── logs/
├── notes.txt
├── practice.txt
├── project/
│   └── src/
│       └── controller/
├── projects/
│   └── python.txt
├── python.tx          ← typo file (see Mistakes section)
└── python.txt
```

### Practice 2: `~/developer-workspace` (backend project simulation)

**Goal:** Build a realistic backend project layout and run log analysis, permission and process tasks on it.

```bash
mkdir developer-workspace && cd developer-workspace
mkdir frontend backend database logs
mkdir -p backend/apps/accounts
touch backend/manage.py backend/requirements.txt
touch frontend/index.html logs/application.log database/schema.sql
```

**Resulting structure:**

```text
developer-workspace/
├── backend/
│   ├── apps/
│   │   └── accounts/
│   ├── manage.py
│   └── requirements.txt
├── database/
│   └── schema.sql
├── frontend/
│   └── index.html
└── logs/
    └── application.log
```

**Verification:** `find . -type f` listed 5 files and `find . -type d` listed 6 directories (including `.`).

#### Notes: copy, view, rename

```bash
echo "Learning linux for backend Development" > backend/notes.txt
cp backend/notes.txt backend/backup_notes.txt
cat backend/notes.txt
less backend/backup_notes.txt
mv backend/backup_notes.txt backend/final_notes.txt
```

#### Log analysis

```bash
echo "INFO Server Started"              > logs/application.log
echo "Error Database connection failed" >> logs/application.log
echo "INFO User Loggedin"               >> logs/application.log
echo "Error Invalid Credential"         >> logs/application.log
```

| Command | Output | Lesson |
|---|---|---|
| `grep "ERROR" logs/application.log` | *(nothing)* | Case-sensitive: the log has `Error`, not `ERROR` |
| `grep "Error" logs/application.log` | 2 lines | Exact case matches |
| `grep -in "error" logs/application.log` | `2:...` and `4:...` | `-i` ignores case, `-n` shows line numbers |
| `grep -ic "error" logs/application.log` | `2` | Counts matching lines |
| `find . -name "*.log"` | `./logs/application.log` | Locate log files |

#### Permissions on a script

```bash
touch backend/deploy.sh
ls -l backend/deploy.sh      # -rw-r--r--  (644, not executable)
chmod 755 backend/deploy.sh
ls -l backend/deploy.sh      # -rwxr-xr-x  (755, executable)
chmod 644 backend/deploy.sh
ls -l backend/deploy.sh      # -rw-r--r--  (back to 644)
```

#### Process management

Run in terminal 1:

```bash
sleep 300
```

Run in terminal 2:

```bash
ps aux | grep sleep     # shows sleep 300 (PID 11673) plus the grep itself
kill 11673              # SIGTERM
ps aux | grep sleep     # only the grep line remains, so the process is gone
```

#### Disk usage

```bash
df -h .     # /dev/vda3  30G  7.7G  22G  27%  /home
df -h       # all filesystems
```

---

## 11. Mistakes and Lessons Learned

| # | What happened | Cause | Fix / Lesson |
|---|---|---|---|
| 1 | `cd desktop` → *No such file or directory* | Linux is case-sensitive; the folder is `Desktop` | Use `cd ~/Desktop`, and press **Tab** to autocomplete |
| 2 | `ls a` → *cannot access 'a'* | Wrong path (tested on purpose) | Read error messages: they name the missing path |
| 3 | `ls project` failed, `ls projects` worked | Directory is `projects` (plural) | Check spelling with `ls` first |
| 4 | `cd ../logs` failed from `linux-practice` | `..` goes to the home dir, where there is no `logs` | Use `cd logs` (child) or `cd ../linux-practice/logs` |
| 5 | `less -/practice.txt` → *no -/ option* | Typed `-/` instead of `~/` | `~/practice.txt` is the correct path |
| 6 | First loop wrote `~/practice.txt`, but `ls` in `linux-practice` didn't show it | `~` is the home dir, not the current dir | Use `./practice.txt` or `> practice.txt` for the current dir |
| 7 | `>> python.tx` created a stray `python.tx` file | Typo in the file name | `>>` silently creates files. Delete with `rm python.tx` |
| 8 | `cat > notes.txt` output merged with the prompt | No Enter before Ctrl+D, so no trailing newline | Press Enter, then Ctrl+D |
| 9 | `cd ~m`, `cd ~n`, `cd ~h` failed | `~name` means *another user's* home directory | Use `~` alone or `~/folder` |
| 10 | `grep "ERROR"` returned nothing | grep is case-sensitive | Use `grep -i` when case is unknown |
| 11 | `ps aux \| grep sleep` showed two lines | grep matches its own process | Use `pgrep -af sleep` or `grep "[s]leep"` |
| 12 | `/dev/sda1` shows 100% used | Mounted Fedora live ISO (read-only) | Normal, ignore it |

### Cleanup commands for the stray file

```bash
rm ~/linux-practice/python.tx
```

---

## 12. Quick Cheat Sheet

```bash
# Navigation
pwd                     ls -la                  cd ~            cd -            cd ..
# Create
mkdir -p a/b/c          touch file.txt
# Copy / move / delete
cp -r src/ dst/         mv old new              rm -i file      rm -r dir/
# View / write
cat file                less file               head -n 20 f    tail -n 50 f    tail -f f
echo "x" > f            echo "x" >> f
# Search
grep -in "text" f       grep -rn "text" dir/    grep -v "text" f    grep -ic "text" f
find . -name "*.py"     find . -type d          find . -type f
# Permissions
chmod 755 f             chmod 644 f             chmod +x f          sudo chown user:group f
# Processes
ps aux | grep name      pgrep -af name          top                 kill PID        kill -9 PID
lsof -i :8000
# Disk
df -h                   du -sh .                du -h -d 1 . | sort -h
```

---

## 13. Key Learnings

- Understood Linux filesystem navigation, absolute vs relative paths, and the `.`, `..`, `~` and `-` shortcuts.
- Practised creating, copying, moving, renaming and deleting files and directories (including `-p`, `-r`, `-i`).
- Learned the difference between `>` (overwrite) and `>>` (append), and the risk of accidental file creation.
- Learned to read large files with `less` and to generate test data with shell loops.
- Learned to search file content with `grep` (`-i`, `-n`, `-v`, `-c`, `-r`) and to locate files with `find`.
- Analysed a sample application log and understood why case sensitivity matters.
- Understood permission notation (`rwx`, numeric modes `755`/`644`) and applied `chmod` to a script.
- Learned to inspect and stop processes with `ps`, `top` and `kill`, and why `kill` is preferred over `kill -9`.
- Read `df -h` and `du -sh` output to understand disk and directory usage.
- Built a realistic backend project structure and used it for practical troubleshooting scenarios.
- Learned from real errors: case sensitivity, typos, wrong relative paths and `~` misuse.

### Next steps

- Practise `lsof -i :8000` with a running dev server (e.g. `python3 -m http.server 8000`).
- Try `sudo` with `chown` on a test file.
- Learn `sort`, `uniq`, `wc` and `awk` for deeper log analysis.
- Create a small shell script (`deploy.sh`) that actually runs.

---

**Day 01 Status:** ✅ Completed – Linux Command Fundamentals.
