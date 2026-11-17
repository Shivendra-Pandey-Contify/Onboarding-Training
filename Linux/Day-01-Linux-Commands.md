# Day 01 – Linux Commands for Backend Development

**Objective:** Learn essential Linux commands for filesystem navigation, file management, searching, permissions, process management and disk monitoring.

## 1. Filesystem Navigation

| Command | Description | Syntax |
|---|---|---|
| `pwd` | Display current directory | `pwd` |
| `ls` | List files and directories | `ls -la` |
| `cd` | Change directory | `cd project/` |
| `mkdir` | Create directories | `mkdir -p backend/apps` |
| `touch` | Create an empty file | `touch app.py` |

## 2. File Management

| Command | Description | Syntax |
|---|---|---|
| `cp` | Copy files/directories | `cp -r source/ destination/` |
| `mv` | Move or rename files | `mv old.py new.py` |
| `rm` | Remove files/directories | `rm -r folder/` |
| `cat` | Display file contents | `cat settings.py` |
| `less` | Read large files page by page | `less application.log` |

**Important:** `>` overwrites file contents, whereas `>>` appends content.

```bash
echo "Server started" > app.log
echo "New request received" >> app.log
```

## 3. Searching and Log Analysis

| Command | Description | Syntax |
|---|---|---|
| `grep` | Search text inside files | `grep -in "error" app.log` |
| `find` | Search files/directories | `find . -name "*.py"` |
| `head` | Display first lines | `head -n 20 app.log` |
| `tail` | Display last lines | `tail -n 50 app.log` |

Useful log monitoring:

```bash
tail -f application.log
grep -rn "ERROR" logs/
```

## 4. Permissions and Ownership

| Command | Description | Syntax |
|---|---|---|
| `chmod` | Change file permissions | `chmod 755 deploy.sh` |
| `chown` | Change file ownership | `sudo chown user:group file.py` |

**Permission reference:**

- Read (`r`) = 4
- Write (`w`) = 2
- Execute (`x`) = 1
- `755` = Owner: RWX, Group/Others: RX
- `644` = Owner: RW, Group/Others: R

## 5. Process Management

| Command | Description | Syntax |
|---|---|---|
| `ps` | Display running processes | `ps aux` |
| `top` | Monitor processes in real time | `top` |
| `kill` | Send a signal to a process | `kill PID` |
| `lsof` | List open files and inspect port usage | `lsof -i :8000` |

Useful process commands:

```bash
ps aux | grep python
pgrep -af python
kill PID
kill -9 PID
```

**Note:** Prefer normal termination using `kill PID`. Use `kill -9` only when necessary.

## 6. Disk Management

| Command | Description | Syntax |
|---|---|---|
| `df` | Display filesystem disk usage | `df -h` |
| `du` | Display directory/file space usage | `du -sh project/` |

Useful disk commands:

```bash
df -h
du -sh .
du -h -d 1 . | sort -h
```

## 7. Important Linux Operators

| Operator | Purpose |
|---|---|
| `.` | Current directory |
| `..` | Parent directory |
| `~` | Home directory |
| `*` | Wildcard |
| `>` | Redirect and overwrite |
| `>>` | Redirect and append |
| `\|` | Pipe output to another command |
| `&&` | Execute next command if previous succeeds |
| `;` | Execute commands sequentially |
| `sudo` | Execute with elevated privileges |

## 8. Practical Backend Use Cases

**1. Locate Django settings file**

```bash
find . -name "settings.py"
```

**2. Search application errors**

```bash
grep -in "error" application.log
```

**3. Monitor live application logs**

```bash
tail -f application.log
```

**4. Identify a process using port 8000**

```bash
lsof -i :8000
```

**5. Terminate a process**

```bash
kill PID
```

**6. Check server disk space**

```bash
df -h
```

**7. Check project directory size**

```bash
du -sh project/
```

**8. Make a deployment script executable**

```bash
chmod +x deploy.sh
```

---

### Key Learnings

- Understood Linux filesystem navigation and directory structures.
- Practised creating, copying, moving and deleting files.
- Learned to search files and analyse application logs.
- Understood Linux permissions and ownership.
- Learned to inspect, monitor and terminate processes.
- Practised checking filesystem and directory disk usage.
- Explored practical Linux commands used in backend development and server troubleshooting.

**Day 01 Status:** Completed – Linux Command Fundamentals.

Terminals logs: 
shivendra@fedora:~$ cd desktop
bash: cd: desktop: No such file or directory
shivendra@fedora:~$ mkdir linux-practice
shivendra@fedora:~$ cd linux-practice
shivendra@fedora:~/linux-practice$ touch notes.txt
shivendra@fedora:~/linux-practice$ touch python.txt
shivendra@fedora:~/linux-practice$ touch linux.txt
shivendra@fedora:~/linux-practice$ mkdir projects
shivendra@fedora:~/linux-practice$ mkdir logs
shivendra@fedora:~/linux-practice$ ls
linux.txt  logs  notes.txt  projects  python.txt
shivendra@fedora:~/linux-practice$ ls -l
total 0
-rw-r--r--. 1 shivendra shivendra 0 Nov 17 10:41 linux.txt
drwxr-xr-x. 1 shivendra shivendra 0 Nov 17 10:42 logs
-rw-r--r--. 1 shivendra shivendra 0 Nov 17 10:41 notes.txt
drwxr-xr-x. 1 shivendra shivendra 0 Nov 17 10:42 projects
-rw-r--r--. 1 shivendra shivendra 0 Nov 17 10:41 python.txt
shivendra@fedora:~/linux-practice$ ls a
ls: cannot access 'a': No such file or directory
shivendra@fedora:~/linux-practice$ ls -lh
total 0
-rw-r--r--. 1 shivendra shivendra 0 Nov 17 10:41 linux.txt
drwxr-xr-x. 1 shivendra shivendra 0 Nov 17 10:42 logs
-rw-r--r--. 1 shivendra shivendra 0 Nov 17 10:41 notes.txt
drwxr-xr-x. 1 shivendra shivendra 0 Nov 17 10:42 projects
-rw-r--r--. 1 shivendra shivendra 0 Nov 17 10:41 python.txt
shivendra@fedora:~/linux-practice$ ls -la
total 0
drwxr-xr-x. 1 shivendra shivendra  80 Nov 17 10:42 .
drwx------. 1 shivendra shivendra 348 Nov 17 10:40 ..
-rw-r--r--. 1 shivendra shivendra   0 Nov 17 10:41 linux.txt
drwxr-xr-x. 1 shivendra shivendra   0 Nov 17 10:42 logs
-rw-r--r--. 1 shivendra shivendra   0 Nov 17 10:41 notes.txt
drwxr-xr-x. 1 shivendra shivendra   0 Nov 17 10:42 projects
-rw-r--r--. 1 shivendra shivendra   0 Nov 17 10:41 python.txt
shivendra@fedora:~/linux-practice$ ls project
ls: cannot access 'project': No such file or directory
shivendra@fedora:~/linux-practice$ ls projects
shivendra@fedora:~/linux-practice$ cd projects
shivendra@fedora:~/linux-practice/projects$ cd ..
shivendra@fedora:~/linux-practice$ cd /
shivendra@fedora:/$ cd ~
shivendra@fedora:~$ cd linux-practice
shivendra@fedora:~/linux-practice$ cd -
/home/shivendra
shivendra@fedora:~$ cd linux-practice
shivendra@fedora:~/linux-practice$ cd ../logs
bash: cd: ../logs: No such file or directory
shivendra@fedora:~/linux-practice$ cd ~/Desktop
shivendra@fedora:~/Desktop$ cd ..
shivendra@fedora:~$ cd linux-practice
shivendra@fedora:~/linux-practice$ pwd
/home/shivendra/linux-practice
shivendra@fedora:~/linux-practice$ mkdir -p project/src/controller
shivendra@fedora:~/linux-practice$ ls
linux.txt  logs  notes.txt  project  projects  python.txt
shivendra@fedora:~/linux-practice$ ls project
src
shivendra@fedora:~/linux-practice$ ls -la
total 0
drwxr-xr-x. 1 shivendra shivendra  94 Nov 17 11:11 .
drwx------. 1 shivendra shivendra 348 Nov 17 10:40 ..
-rw-r--r--. 1 shivendra shivendra   0 Nov 17 10:41 linux.txt
drwxr-xr-x. 1 shivendra shivendra   0 Nov 17 10:42 logs
-rw-r--r--. 1 shivendra shivendra   0 Nov 17 10:41 notes.txt
drwxr-xr-x. 1 shivendra shivendra   6 Nov 17 11:11 project
drwxr-xr-x. 1 shivendra shivendra   0 Nov 17 10:42 projects
-rw-r--r--. 1 shivendra shivendra   0 Nov 17 10:41 python.txt
shivendra@fedora:~/linux-practice$ ls project -la
total 0
drwxr-xr-x. 1 shivendra shivendra  6 Nov 17 11:11 .
drwxr-xr-x. 1 shivendra shivendra 94 Nov 17 11:11 ..
drwxr-xr-x. 1 shivendra shivendra 20 Nov 17 11:11 src
shivendra@fedora:~/linux-practice$ cp notes.txt backup-notes.txt
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  linux.txt  logs  notes.txt  project  projects  python.txt
shivendra@fedora:~/linux-practice$ cp python.txt projects/
shivendra@fedora:~/linux-practice$ ls projects
python.txt
shivendra@fedora:~/linux-practice$ cp -r projects backup-projects
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  backup-projects  linux.txt  logs  notes.txt  project  projects  python.txt
shivendra@fedora:~/linux-practice$ mv notes.txt mynotes.txt
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  backup-projects  linux.txt  logs  mynotes.txt  project  projects  python.txt
shivendra@fedora:~/linux-practice$ mv mynotes.txt logs/
shivendra@fedora:~/linux-practice$ ls logs
mynotes.txt
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  backup-projects  linux.txt  logs  project  projects  python.txt
shivendra@fedora:~/linux-practice$ mv logs/mynotes.txt notes.txt
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  backup-projects  linux.txt  logs  notes.txt  project  projects  python.txt
shivendra@fedora:~/linux-practice$ ls logs
shivendra@fedora:~/linux-practice$ rm python.txt
shivendra@fedora:~/linux-practice$ rm -i linux.txt
rm: remove regular empty file 'linux.txt'? y
shivendra@fedora:~/linux-practice$ rm -r backup-projects
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  logs  notes.txt  project  projects
shivendra@fedora:~/linux-practice$ echo "learning linux commands" > notes.txt
shivendra@fedora:~/linux-practice$ cat notes.txt
learning linux commands
shivendra@fedora:~/linux-practice$ echo "add in backup notes.txt" > backup-notes.txt
shivendra@fedora:~/linux-practice$ cat notes.txt backup-notes.txt
learning linux commands
add in backup notes.txt
shivendra@fedora:~/linux-practice$ cat > notes.txt
hello from shivendra , i am learning the linux commandsshivendra@fedora:~/linux-practice$ 
shivendra@fedora:~/linux-practice$ cat notes.txt
hello from shivendra , i am learning the linux commandsshivendra@fedora:~/linux-practice$ 
shivendra@fedora:~/linux-practice$ cat >> notes.txt
learning the distinction between using > >> shivendra@fedora:~/linux-practice$ 
shivendra@fedora:~/linux-practice$ cat notes.txt
hello from shivendra , i am learning the linux commandslearning the distinction between using > >> shivendra@fedora:~/linux-practice$ for i in $(seq 1 500); do echo "Line $i: Fedora on UTM is running Linux practice with less command"; done > ~/practice.txt
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  logs  notes.txt  project  projects
shivendra@fedora:~/linux-practice$ less -/practice.txt
There is no -/ option ("less --help" for help)
Missing filename ("less --help" for help)
shivendra@fedora:~/linux-practice$ touch practice.txt
shivendra@fedora:~/linux-practice$ for i in $(seq 1 500); do echo "Line $i: Fedora on UTM is running Linux practice with less command"; done > ~/practice.txt
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  logs  notes.txt  practice.txt  project  projects
shivendra@fedora:~/linux-practice$ less practice.txt
shivendra@fedora:~/linux-practice$ echo "Python is easy" > python.txt
echo "Linux is powerful" >> python.txt
echo "Python supports Django" >> python.txt
echo "Django uses Python" >> python.tx
shivendra@fedora:~/linux-practice$ ls
backup-notes.txt  logs  notes.txt  practice.txt  project  projects  python.tx  python.txt
shivendra@fedora:~/linux-practice$ grep "Python" python.txt
Python is easy
Python supports Django
shivendra@fedora:~/linux-practice$ grep -n "Python" python.txt
1:Python is easy
3:Python supports Django
shivendra@fedora:~/linux-practice$ grep -v "Python" python.txt
Linux is powerful
shivendra@fedora:~/linux-practice$ find . -name "python.txt"
./projects/python.txt
./python.txt
shivendra@fedora:~/linux-practice$ find . -name "*.py"
shivendra@fedora:~/linux-practice$ touch hello.py
shivendra@fedora:~/linux-practice$ find . -name "*.py"
./hello.py
shivendra@fedora:~/linux-practice$ find . -type d
.
./projects
./logs
./project
./project/src
top - 14:18:50 up  4:05,  1 user,  load average: 0.23, 0.10, 0.05
Tasks: 240 total, 1 running, 239 sleep, 0 d-sleep, 0 stopped, 0 zombie
%Cpu(s):  3.0 us,  0.3 sy,  0.0 ni, 96.3 id,  0.0 wa,  0.2 hi,  0.1 si,  0.0 st 
MiB Mem :   3886.1 total,    255.8 free,   2125.5 used,   1874.7 buff/cache     
MiB Swap:   3886.0 total,   2443.2 free,   1442.8 used.   1760.6 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                              
   8757 shivend+  20   0 1722052 606916 184504 S   6.2  15.3   1:52.51 ptyxis                               
   2353 shivend+  20   0 4355440 591372 149992 S   4.6  14.9  18:10.89 gnome-shell                          
  11022 shivend+  20   0  235880   5552   3440 R   0.7   0.1   0:00.42 top                                  
     45 root      39  19       0      0      0 S   0.3   0.0   0:10.43 khugepaged                           
    619 polkitd   20   0  386272  19432   6620 S   0.3   0.5   0:01.95 polkitd                              
      1 root      20   0   43104  16392   9284 S   0.0   0.4   0:03.86 systemd                              
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.05 kthreadd                             
      3 root      20   0       0      0      0 S   0.0   0.0   0:00.00 pool_workqueue_release               
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-rcu_gp                     
      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-sync_wq                    
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-kvfree_rcu_reclaim         
      7 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-slub_flushwq               
      8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-netns                      
     10 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-kblockd                 
     13 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-mm_percpu_wq               
     15 root      20   0       0      0      0 S   0.0   0.0   0:00.06 ksoftirqd/0                          
     16 root      20   0       0      0      0 I   0.0   0.0   0:00.61 rcu_preempt                          
     17 root      20   0       0      0      0 S   0.0   0.0   0:00.00 rcu_exp_par_gp_kthread_worker/0      
     18 root      20   0       0      0      0 S   0.0   0.0   0:00.03 rcu_exp_gp_kthread_worker            
     19 root      rt   0       0      0      0 S   0.0   0.0   0:00.00 migration/0                          
     20 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/0                              
     21 root      20   0       0      0      0 S   0.0   0.0   0:00.00 cpuhp/1                              
     22 root      rt   0       0      0      0 S   0.0   0.0   0:00.01 migration/1                          
shivendra@fedora:~/linux-practice$ df
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/vda3       30840832 8059808  22182272  27% /
devtmpfs            4096       0      4096   0% /dev
tmpfs            1989664     108   1989556   1% /dev/shm
efivarfs              56       3        54   5% /sys/firmware/efi/efivars
tmpfs             795868    1392    794476   1% /run
none                1024       0      1024   0% /run/credentials/systemd-journald.service
none                1024       0      1024   0% /run/credentials/systemd-resolved.service
tmpfs            1989664       8   1989656   1% /tmp
/dev/vda3       30840832 8059808  22182272  27% /home
/dev/vda2        1992552  716032   1155280  39% /boot
/dev/vda1         613184   38436    574748   7% /boot/efi
tmpfs               1024       0      1024   0% /run/stratisd/ns_mounts
tmpfs             397932     116    397816   1% /run/user/1000
/dev/sda1        2886306 2886306         0 100% /run/media/shivendra/Fedora-WS-Live-45
shivendra@fedora:~/linux-practice$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda3        30G  7.7G   22G  27% /
devtmpfs        4.0M     0  4.0M   0% /dev
tmpfs           1.9G  108K  1.9G   1% /dev/shm
efivarfs         56K  2.8K   54K   5% /sys/firmware/efi/efivars
tmpfs           778M  1.4M  776M   1% /run
none            1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
none            1.0M     0  1.0M   0% /run/credentials/systemd-resolved.service
tmpfs           1.9G  8.0K  1.9G   1% /tmp
/dev/vda3        30G  7.7G   22G  27% /home
/dev/vda2       2.0G  700M  1.2G  39% /boot
/dev/vda1       599M   38M  562M   7% /boot/efi
tmpfs           1.0M     0  1.0M   0% /run/stratisd/ns_mounts
tmpfs           389M  116K  389M   1% /run/user/1000
/dev/sda1       2.8G  2.8G     0 100% /run/media/shivendra/Fedora-WS-Live-45
shivendra@fedora:~/linux-practice$ du -sh
16K	.
shivendra@fedora:~/linux-practice$ du -sh .
16K	.
shivendra@fedora:~/linux-practice$ cd ~m
bash: cd: ~m: No such file or directory
shivendra@fedora:~/linux-practice$ cd ~n
bash: cd: ~n: No such file or directory
shivendra@fedora:~/linux-practice$ cd ~h
bash: cd: ~h: No such file or directory
shivendra@fedora:~/linux-practice$ cd ~


Practice:
shivendra@fedora:~$ mkdir developer-workspace
shivendra@fedora:~$ cd developer-workspace
shivendra@fedora:~/developer-workspace$ mkdir frontend backend database logs
shivendra@fedora:~/developer-workspace$ mkdir -p backend/apps/accounts
shivendra@fedora:~/developer-workspace$ touch backend/manage.py
shivendra@fedora:~/developer-workspace$ touch backend/requirements.txt
shivendra@fedora:~/developer-workspace$ touch frontend/index.html
shivendra@fedora:~/developer-workspace$ touch logs/application.log
shivendra@fedora:~/developer-workspace$ touch database/schema.sql
shivendra@fedora:~/developer-workspace$ ls -la
total 0
drwxr-xr-x. 1 shivendra shivendra  54 Nov 17 14:58 .
drwx------. 1 shivendra shivendra 410 Nov 17 14:57 ..
drwxr-xr-x. 1 shivendra shivendra  58 Nov 17 14:59 backend
drwxr-xr-x. 1 shivendra shivendra  20 Nov 17 15:00 database
drwxr-xr-x. 1 shivendra shivendra  20 Nov 17 14:59 frontend
drwxr-xr-x. 1 shivendra shivendra  30 Nov 17 15:00 logs
shivendra@fedora:~/developer-workspace$ find . -type f
./frontend/index.html
./backend/manage.py
./backend/requirements.txt
./database/schema.sql
./logs/application.log
shivendra@fedora:~/developer-workspace$ find . -type d
.
./frontend
./backend
./backend/apps
./backend/apps/accounts
./database
./logs
shivendra@fedora:~/developer-workspace$ pwd
/home/shivendra/developer-workspace
shivendra@fedora:~/developer-workspace$ echo "Learning linux for backend Development"> backend/notes.txt
shivendra@fedora:~/developer-workspace$ ls backend
apps  manage.py  notes.txt  requirements.txt
shivendra@fedora:~/developer-workspace$ cp backend/notes.txt backend/backup_notes.txt
shivendra@fedora:~/developer-workspace$ ls backend
apps  backup_notes.txt  manage.py  notes.txt  requirements.txt
shivendra@fedora:~/developer-workspace$ cat backend/notes.txt
Learning linux for backend Development
shivendra@fedora:~/developer-workspace$ less backend/backup_notes.txt
shivendra@fedora:~/developer-workspace$ mv backend/backup_notes.txt backend/final_notes.txt
shivendra@fedora:~/developer-workspace$ ls backend
apps  final_notes.txt  manage.py  notes.txt  requirements.txt
shivendra@fedora:~/developer-workspace$ echo "INFO Server Started"> logs/application.log
shivendra@fedora:~/developer-workspace$ echo "Error Database connection failed">> logs/application.log
shivendra@fedora:~/developer-workspace$ echo "INFO User Loggedin">> logs/application.log
shivendra@fedora:~/developer-workspace$ echo "Error Invalid Credential" >> logs/application.log
shivendra@fedora:~/developer-workspace$ cat logs/application.log
INFO Server Started
Error Database connection failed
INFO User Loggedin
Error Invalid Credential
shivendra@fedora:~/developer-workspace$ grep "ERROR" logs/application.log
shivendra@fedora:~/developer-workspace$ grep "Error" logs/application.log
Error Database connection failed
Error Invalid Credential
shivendra@fedora:~/developer-workspace$ grep -in "error" logs/application.log
2:Error Database connection failed
4:Error Invalid Credential
shivendra@fedora:~/developer-workspace$ grep -ic "error" logs/application.log
2
shivendra@fedora:~/developer-workspace$ find . -name "*.log"
./logs/application.log
shivendra@fedora:~/developer-workspace$ touch backend/deploy.sh
shivendra@fedora:~/developer-workspace$ ls -l backend/deploy.sh
-rw-r--r--. 1 shivendra shivendra 0 Nov 17 15:15 backend/deploy.sh
shivendra@fedora:~/developer-workspace$ chmod 755 backend/deploy.sh
shivendra@fedora:~/developer-workspace$ ls -l backend/deploy.sh
-rwxr-xr-x. 1 shivendra shivendra 0 Nov 17 15:15 backend/deploy.sh
shivendra@fedora:~/developer-workspace$ chmod 644 backend/deploy.sh
shivendra@fedora:~/developer-workspace$ ls -l backend/deploy.sh
-rw-r--r--. 1 shivendra shivendra 0 Nov 17 15:15 backend/deploy.sh
shivendra@fedora:~/developer-workspace$ ps aux | grep sleep
shivend+   11673  0.0  0.0 232120  2100 pts/0    S+   15:18   0:00 sleep 300
shivend+   11677 50.0  0.0 232500  2300 pts/1    S+   15:19   0:00 grep --color=auto sleep
shivendra@fedora:~/developer-workspace$ kill 11673
shivendra@fedora:~/developer-workspace$ ps aux | grep sleep
shivend+   11693  0.0  0.0 233136  2292 pts/1    S+   15:20   0:00 grep --color=auto sleep
shivendra@fedora:~/developer-workspace$ df -h .
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda3        30G  7.7G   22G  27% /home
shivendra@fedora:~/developer-workspace$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/vda3        30G  7.7G   22G  27% /
devtmpfs        4.0M     0  4.0M   0% /dev
tmpfs           1.9G  108K  1.9G   1% /dev/shm
efivarfs         56K  2.8K   54K   5% /sys/firmware/efi/efivars
tmpfs           778M  1.4M  776M   1% /run
none            1.0M     0  1.0M   0% /run/credentials/systemd-journald.service
none            1.0M     0  1.0M   0% /run/credentials/systemd-resolved.service
tmpfs           1.9G  8.0K  1.9G   1% /tmp
/dev/vda3        30G  7.7G   22G  27% /home
/dev/vda2       2.0G  700M  1.2G  39% /boot
/dev/vda1       599M   38M  562M   7% /boot/efi
tmpfs           1.0M     0  1.0M   0% /run/stratisd/ns_mounts
tmpfs           389M  120K  389M   1% /run/user/1000
/dev/sda1       2.8G  2.8G     0 100% /run/media/shivendra/Fedora-WS-Live-45
shivendra@fedora:~/developer-workspace$ 




