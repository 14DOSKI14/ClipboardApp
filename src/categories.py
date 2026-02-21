# =============================================================================
# CATEGORIES.PY - Ordlister og kategorisering
# =============================================================================
# HVA: Inneholder kjente kommandoer og kode-nøkkelord
# HVORFOR: Brukes for å automatisk kategorisere clipboard-innhold
# HVORDAN: Sjekker tekst mot arrays med kjente ord
#
# OPPGAVEKRAV:
#   - Arrays (COMMANDS, CODE_KEYWORDS)
#   - For-løkker (sjekke mot arrays)
#   - If/else-tester (kategorisering)
#   - Egendefinerte funksjoner
# =============================================================================

import numpy as np

# =============================================================================
# COMMANDS - Omfattende array med terminal-kommandoer
# =============================================================================

COMMANDS = np.array([
    # --- FILSYSTEM ---
    "ls", "ll", "la", "ls -la", "ls -l", "ls -a",
    "cd", "cd ..", "cd ~", "cd /",
    "pwd", "mkdir", "mkdir -p", "rmdir",
    "rm", "rm -r", "rm -rf", "rm -f",
    "cp", "cp -r", "cp -rf",
    "mv", "touch", "cat", "less", "more", "head", "tail",
    "nano", "vim", "vi", "code", "code .", "open", "open .",
    "chmod", "chmod +x", "chmod 755", "chmod 777", "chmod 644",
    "chown", "chgrp",
    "find", "find .", "locate", "whereis", "which", "type",
    "ln", "ln -s", "readlink",
    "tree", "file", "stat", "wc", "wc -l",
    "diff", "cmp", "comm",
    "basename", "dirname", "realpath",

    # --- SYSTEM & PROSESSER ---
    "sudo", "sudo -i", "sudo su", "su", "su -",
    "ps", "ps aux", "ps -ef", "ps -a",
    "top", "htop", "btop", "atop",
    "kill", "kill -9", "killall", "pkill",
    "jobs", "bg", "fg", "nohup",
    "systemctl", "systemctl start", "systemctl stop", "systemctl restart",
    "systemctl status", "systemctl enable", "systemctl disable",
    "service", "service start", "service stop",
    "df", "df -h", "du", "du -sh", "du -h",
    "free", "free -h", "free -m",
    "uname", "uname -a", "uname -r",
    "uptime", "whoami", "id", "groups",
    "hostname", "hostnamectl",
    "date", "cal", "timedatectl",
    "shutdown", "reboot", "poweroff", "halt",
    "clear", "reset", "exit", "logout",
    "history", "history -c",
    "man", "info", "help", "whatis", "apropos",
    "env", "printenv", "set", "unset",
    "export", "source", ".", "alias", "unalias",
    "xargs", "tee", "time", "watch",
    "crontab", "crontab -e", "crontab -l",
    "at", "batch",
    "lsof", "fuser",
    "dmesg", "journalctl",
    "mount", "umount", "fdisk", "mkfs", "fsck",
    "lsblk", "blkid", "parted",

    # --- NETTVERK ---
    "ping", "ping -c", "ping6",
    "curl", "curl -X", "curl -o", "curl -O", "curl -I", "curl -s",
    "wget", "wget -O", "wget -c",
    "ssh", "ssh -i", "ssh -p", "ssh-keygen", "ssh-copy-id", "ssh-add",
    "scp", "scp -r", "sftp", "rsync", "rsync -avz",
    "ftp", "telnet", "nc", "netcat", "ncat",
    "netstat", "netstat -tulpn", "ss", "ss -tulpn",
    "ifconfig", "ip", "ip addr", "ip link", "ip route",
    "route", "arp", "arping",
    "nslookup", "dig", "host", "whois",
    "traceroute", "tracepath", "mtr",
    "nmap", "nmap -sV", "nmap -sS", "nmap -p",
    "tcpdump", "wireshark", "tshark",
    "iptables", "ip6tables", "ufw", "firewall-cmd",
    "nmcli", "nmtui", "iwconfig", "iwlist",
    "hostname", "hostnamectl",
    "openssl", "openssl s_client",

    # --- GIT ---
    "git", "git init", "git clone",
    "git status", "git add", "git add .", "git add -A",
    "git commit", "git commit -m", "git commit -am",
    "git push", "git push origin", "git push -u", "git push --force",
    "git pull", "git pull origin", "git fetch", "git fetch --all",
    "git branch", "git branch -a", "git branch -d", "git branch -D",
    "git checkout", "git checkout -b", "git switch", "git switch -c",
    "git merge", "git rebase", "git rebase -i",
    "git log", "git log --oneline", "git log --graph",
    "git diff", "git diff --staged", "git diff HEAD",
    "git stash", "git stash pop", "git stash list", "git stash drop",
    "git reset", "git reset --hard", "git reset --soft",
    "git revert", "git cherry-pick",
    "git tag", "git tag -a", "git tag -d",
    "git remote", "git remote -v", "git remote add",
    "git config", "git config --global",
    "git show", "git blame", "git bisect",
    "git clean", "git clean -fd",
    "git submodule", "git lfs",

    # --- PAKKEBEHANDLING ---
    # Python
    "pip", "pip3", "pip install", "pip3 install",
    "pip uninstall", "pip freeze", "pip list",
    "pip install -r", "pip install --upgrade",
    "python -m pip", "python3 -m pip",
    "pipenv", "poetry", "conda",
    "virtualenv", "venv", "python -m venv",
    "pyenv",

    # Node.js
    "npm", "npm install", "npm i", "npm init",
    "npm run", "npm start", "npm test", "npm build",
    "npm update", "npm uninstall", "npm list",
    "npm install -g", "npm install --save-dev",
    "npx", "yarn", "yarn add", "yarn install",
    "yarn run", "yarn start", "yarn build",
    "pnpm", "bun",
    "nvm", "nvm use", "nvm install",

    # macOS
    "brew", "brew install", "brew uninstall",
    "brew update", "brew upgrade", "brew list",
    "brew search", "brew info", "brew doctor",
    "brew cask", "brew services",
    "port", "mas",

    # Linux
    "apt", "apt-get", "apt install", "apt-get install",
    "apt update", "apt upgrade", "apt remove",
    "apt search", "apt list", "apt autoremove",
    "dpkg", "dpkg -i", "dpkg -l",
    "yum", "yum install", "yum update", "yum remove",
    "dnf", "dnf install", "dnf update",
    "rpm", "rpm -i", "rpm -qa",
    "pacman", "pacman -S", "pacman -Syu", "pacman -R",
    "snap", "snap install", "flatpak",
    "zypper",

    # Rust
    "cargo", "cargo build", "cargo run", "cargo test",
    "cargo new", "cargo add", "cargo install",
    "rustup", "rustc",

    # Go
    "go", "go run", "go build", "go test",
    "go get", "go mod", "go install",

    # Ruby
    "gem", "gem install", "bundle", "bundler",
    "rbenv", "rvm",

    # --- KJØRING AV PROGRAMMER ---
    "python", "python3", "python2",
    "python -c", "python -m", "python --version",
    "node", "node -v", "nodejs",
    "java", "javac", "java -jar",
    "gcc", "g++", "clang", "clang++",
    "make", "make install", "make clean",
    "cmake", "ninja", "meson",
    "ruby", "perl", "php", "lua",
    "bash", "sh", "zsh", "fish",
    "docker", "docker run", "docker build", "docker-compose",
    "kubectl", "helm", "terraform", "ansible",
    "vagrant", "packer",

    # --- ARKIV & KOMPRIMERING ---
    "tar", "tar -xvf", "tar -cvf", "tar -xzf", "tar -czf",
    "tar -xjf", "tar -cjf",
    "zip", "unzip", "gzip", "gunzip",
    "bzip2", "bunzip2", "xz", "unxz",
    "7z", "7za", "rar", "unrar",
    "zcat", "zless", "zgrep",

    # --- TEKST & SØK ---
    "grep", "grep -r", "grep -i", "grep -v", "grep -E",
    "egrep", "fgrep", "rg", "ripgrep", "ag",
    "awk", "gawk", "sed", "sed -i",
    "sort", "sort -n", "sort -r", "sort -u",
    "uniq", "uniq -c", "cut", "cut -d",
    "tr", "rev", "tac",
    "head", "head -n", "tail", "tail -n", "tail -f",
    "echo", "printf", "cat", "tac",
    "paste", "join", "split",
    "fmt", "fold", "column",
    "strings", "od", "hexdump", "xxd",
    "jq", "yq", "xmllint",

    # --- DIVERSE ---
    "screen", "tmux", "byobu",
    "htpasswd", "base64", "md5sum", "sha256sum", "shasum",
    "gpg", "gpg2",
    "aws", "aws s3", "az", "gcloud",
    "heroku", "vercel", "netlify",
    "ffmpeg", "convert", "identify",
    "youtube-dl", "yt-dlp",
    "sqlite3", "mysql", "psql", "mongo", "redis-cli",
    "vim", "nvim", "emacs", "nano", "pico",
    "./", "./"
])

# =============================================================================
# CODE_KEYWORDS - Omfattende array med kode-nøkkelord
# =============================================================================

CODE_KEYWORDS = np.array([
    # --- PYTHON ---
    "def ", "class ", "import ", "from ", "as ",
    "if __name__", "__init__", "__main__",
    "self.", "self,", "cls.",
    "print(", "return ", "yield ",
    "elif ", "else:", "except:", "except ", "finally:",
    "try:", "raise ", "assert ",
    "lambda ", "lambda:",
    "async ", "await ", "asyncio",
    "with ", "as:",
    "for ", "in ", "while ",
    "break", "continue", "pass",
    "True", "False", "None",
    "and ", "or ", "not ", "is ",
    "@property", "@staticmethod", "@classmethod",
    "@dataclass", "@decorator",
    "super()", "isinstance(", "type(",
    "len(", "range(", "enumerate(",
    "list(", "dict(", "set(", "tuple(",
    "open(", "read(", "write(",
    "append(", "extend(", "pop(",
    "keys()", "values()", "items()",
    "join(", "split(", "strip(",
    "format(", "f\"", "f'",
    "__str__", "__repr__", "__len__",
    "pip install", "requirements.txt",

    # --- JAVASCRIPT / TYPESCRIPT ---
    "function ", "function(", "() =>", "=> {",
    "const ", "let ", "var ",
    "console.log", "console.error", "console.warn",
    "document.", "window.", "navigator.",
    "getElementById", "querySelector", "querySelectorAll",
    "addEventListener", "removeEventListener",
    "createElement", "appendChild", "innerHTML",
    "require(", "module.exports", "export default",
    "export ", "import ", "from '", "from \"",
    "async function", "await ", "Promise",
    ".then(", ".catch(", ".finally(",
    "new Promise", "resolve(", "reject(",
    "fetch(", "axios.", "XMLHttpRequest",
    "JSON.parse", "JSON.stringify",
    "typeof ", "instanceof ",
    "Array.", "Object.", "String.", "Number.",
    ".map(", ".filter(", ".reduce(", ".forEach(",
    ".find(", ".some(", ".every(", ".includes(",
    "push(", "pop(", "shift(", "unshift(",
    "slice(", "splice(", "concat(",
    "setTimeout(", "setInterval(", "clearTimeout(",
    "null", "undefined", "NaN",
    "true", "false",
    "this.", "this,",
    "class ", "extends ", "constructor(",
    "static ", "get ", "set ",
    "interface ", "type ", "enum ",
    "React", "useState", "useEffect", "useRef",
    "useCallback", "useMemo", "useContext",
    "Vue", "Angular", "Svelte",
    "express", "app.get", "app.post", "app.use",
    "router.", "req.", "res.", "next(",
    "package.json", "node_modules",

    # --- JAVA ---
    "public class", "private class", "protected class",
    "public static void main",
    "public ", "private ", "protected ",
    "static ", "final ", "abstract ",
    "void ", "int ", "String ", "boolean ",
    "double ", "float ", "long ", "char ",
    "new ", "this.", "super.",
    "extends ", "implements ",
    "interface ", "enum ",
    "@Override", "@Deprecated", "@SuppressWarnings",
    "System.out.print", "System.out.println",
    "System.err", "System.in",
    "try {", "catch (", "finally {",
    "throw ", "throws ",
    "import java.", "import javax.",
    "package ",
    ".equals(", ".toString(", ".hashCode(",
    "ArrayList", "HashMap", "LinkedList",
    "IOException", "Exception", "RuntimeException",

    # --- C / C++ ---
    "#include", "#define", "#ifdef", "#ifndef", "#endif",
    "#pragma", "#error", "#warning",
    "int main", "void main", "main(",
    "printf(", "scanf(", "sprintf(", "fprintf(",
    "cout <<", "cin >>", "endl",
    "std::", "using namespace",
    "malloc(", "calloc(", "realloc(", "free(",
    "new ", "delete ", "delete[]",
    "sizeof(", "typedef ", "struct ",
    "enum ", "union ",
    "const ", "static ", "extern ", "volatile ",
    "inline ", "virtual ", "override ",
    "public:", "private:", "protected:",
    "template<", "typename ",
    "nullptr", "NULL",
    "vector<", "map<", "set<", "list<",
    "string ", "char*", "int*", "void*",
    "->", "::", "<<", ">>",

    # --- C# ---
    "using System", "namespace ",
    "Console.WriteLine", "Console.ReadLine",
    "public class", "private class",
    "async Task", "await ",
    "var ", "dynamic ",
    "get;", "set;",
    "LINQ", ".Select(", ".Where(",

    # --- GO ---
    "package main", "func main",
    "func ", "go func",
    "import (", "import \"",
    "fmt.Print", "fmt.Println", "fmt.Sprintf",
    "if err != nil", "err != nil",
    "defer ", "go ", "chan ",
    "make(", "append(",
    "struct {", "interface {",
    ":= ", "var ", "const ",
    "range ", "select {", "case ",

    # --- RUST ---
    "fn main", "fn ",
    "let ", "let mut ", "const ",
    "println!", "print!", "format!",
    "pub ", "mod ", "use ",
    "impl ", "trait ", "struct ",
    "enum ", "match ", "=> ",
    "Option<", "Result<", "Some(", "None",
    "Ok(", "Err(",
    "unwrap()", "expect(",
    "&", "&mut", "Box<", "Rc<", "Arc<",
    "async fn", ".await",
    "cargo", "crate",

    # --- RUBY ---
    "def ", "end", "class ",
    "puts ", "print ", "p ",
    "require ", "require_relative",
    "attr_accessor", "attr_reader", "attr_writer",
    "initialize", "@", "@@",
    "do |", "{ |", ".each ", ".map ",
    "nil", "true", "false",
    "if ", "elsif ", "unless ",
    "module ", "include ", "extend ",
    "gem ", "Gemfile",

    # --- PHP ---
    "<?php", "?>", "<?=",
    "echo ", "print ", "var_dump(",
    "function ", "class ",
    "$_GET", "$_POST", "$_SESSION", "$_COOKIE",
    "public function", "private function",
    "namespace ", "use ",
    "require ", "include ", "require_once",
    "->", "=>", "::",
    "array(", "[]",
    "new ", "extends ", "implements ",

    # --- SQL ---
    "SELECT ", "FROM ", "WHERE ",
    "INSERT INTO", "VALUES ",
    "UPDATE ", "SET ", "DELETE FROM",
    "CREATE TABLE", "DROP TABLE", "ALTER TABLE",
    "CREATE DATABASE", "DROP DATABASE",
    "CREATE INDEX", "DROP INDEX",
    "JOIN ", "LEFT JOIN", "RIGHT JOIN", "INNER JOIN",
    "OUTER JOIN", "CROSS JOIN",
    "ON ", "AND ", "OR ", "NOT ",
    "ORDER BY", "GROUP BY", "HAVING ",
    "LIMIT ", "OFFSET ",
    "COUNT(", "SUM(", "AVG(", "MAX(", "MIN(",
    "DISTINCT ", "AS ", "LIKE ",
    "IN (", "BETWEEN ", "IS NULL", "IS NOT NULL",
    "PRIMARY KEY", "FOREIGN KEY", "REFERENCES",
    "UNIQUE", "NOT NULL", "DEFAULT ",
    "BEGIN", "COMMIT", "ROLLBACK",

    # --- HTML ---
    "<!DOCTYPE", "<html", "</html>",
    "<head", "</head>", "<body", "</body>",
    "<div", "</div>", "<span", "</span>",
    "<p>", "</p>", "<a ", "</a>",
    "<img ", "<input", "<button", "<form",
    "<table", "<tr", "<td", "<th",
    "<ul", "<ol", "<li",
    "<script", "</script>", "<style", "</style>",
    "<link ", "<meta ",
    "href=", "src=", "class=", "id=",
    "<header", "<footer", "<nav", "<main",
    "<section", "<article", "<aside",
    "/>", "></", "<!--", "-->",

    # --- CSS ---
    "margin:", "padding:", "border:",
    "width:", "height:", "max-width:", "min-width:",
    "display:", "flex", "grid", "block", "inline",
    "position:", "absolute", "relative", "fixed",
    "top:", "right:", "bottom:", "left:",
    "color:", "background:", "background-color:",
    "font-size:", "font-family:", "font-weight:",
    "text-align:", "text-decoration:",
    "justify-content:", "align-items:",
    "flex-direction:", "flex-wrap:",
    "z-index:", "opacity:", "visibility:",
    "transform:", "transition:", "animation:",
    "@media", "@keyframes", "@import",
    ":hover", ":focus", ":active", ":visited",
    "::before", "::after",
    ".class", "#id", "!important",
    "px", "em", "rem", "%", "vh", "vw",
    "rgb(", "rgba(", "hsl(", "#",

    # --- SHELL / BASH ---
    "#!/bin/bash", "#!/bin/sh", "#!/usr/bin/env",
    "if [", "then", "else", "elif", "fi",
    "for ", "in ", "do", "done",
    "while ", "until ",
    "case ", "esac",
    "function ", "() {",
    "$1", "$2", "$@", "$#", "$?", "$$",
    "${", "$(",
    "echo ", "read ", "printf ",
    "exit ", "return ",
    "local ", "export ",
    "shift", "getopts",
    "test ", "[ ", "[[ ",
    "-eq", "-ne", "-lt", "-gt", "-le", "-ge",
    "-f ", "-d ", "-e ", "-r ", "-w ", "-x ",
    "&&", "||", "|", ">", ">>", "<", "<<",
    "2>&1", "/dev/null",

    # --- CONFIG / DATA ---
    ".json", ".yaml", ".yml", ".toml", ".xml",
    ".env", ".ini", ".conf", ".cfg",
    "apiVersion:", "kind:", "metadata:",
    "version:", "name:", "description:",
    "dependencies:", "devDependencies:",
    "scripts:", "main:", "module:",

    # --- GENERELLE SYMBOLER ---
    "{", "}", "[", "]", "(", ")",
    "==", "===", "!=", "!==",
    ">=", "<=", "<", ">",
    "&&", "||", "!",
    "++", "--", "+=", "-=", "*=", "/=",
    "=>", "->", "::", "...",
    "/**", "*/", "//", "/*", "#",
    ";;", ";;", ":;"
])


def categorize(text):
    """
    Kategoriserer tekst som command, code eller text.

    Bruker if/else og for-løkker for å sjekke mot arrays.

    Args:
        text: Tekst fra clipboard

    Returns:
        "command", "code" eller "text"
    """
    # Sjekk at teksten er gyldig
    if not text or len(text.strip()) < 2:
        return None

    text_stripped = text.strip()
    text_lower = text_stripped.lower()

    # For-løkke: Sjekk om teksten starter med en kjent kommando
    for cmd in COMMANDS:
        cmd_lower = cmd.lower()
        if text_lower.startswith(cmd_lower):
            # Sjekk at det er slutt eller mellomrom etter kommandoen
            if len(text_lower) == len(cmd_lower) or text_lower[len(cmd_lower)] in ' \t\n-|>&':
                return "command"

    # For-løkke: Sjekk om teksten inneholder kode-nøkkelord
    for keyword in CODE_KEYWORDS:
        if keyword in text_stripped:
            return "code"

    # Ekstra sjekk: Mange spesialtegn = sannsynligvis kode
    special_chars = text_stripped.count('{') + text_stripped.count('}')
    special_chars += text_stripped.count('(') + text_stripped.count(')')
    special_chars += text_stripped.count(';') + text_stripped.count(':')

    if special_chars >= 3 and len(text_stripped) > 10:
        return "code"

    # Sjekk for innrykk (indikerer kode)
    lines = text_stripped.split('\n')
    indented_lines = 0
    for line in lines:
        if line.startswith('    ') or line.startswith('\t'):
            indented_lines += 1

    if indented_lines >= 2:
        return "code"

    # Hvis ingen match, returner text
    return "text"