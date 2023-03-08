# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH
unsetopt autocd
# Path to your oh-my-zsh installation.
export ZSH="/home/<HOME>/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
#ZSH_THEME="robbyrussell"
#ZSH_THEME="miloshadzic"
#ZSH_THEME="gnzh"
#ZSH_THEME="jnrowe"
#ZSH_THEME="af-magic"
ZSH_THEME="miloshadzic"
#
# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in $ZSH/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment one of the following lines to change the auto-update behavior
# zstyle ':omz:update' mode disabled  # disable automatic updates
 zstyle ':omz:update' mode auto      # update automatically without asking
# zstyle ':omz:update' mode reminder  # just remind me to update when it's time

# Uncomment the following line to change how often to auto-update (in days).
# zstyle ':omz:update' frequency 13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
 DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# You can also set it to another string to have that shown instead of the default red dots.
# e.g. COMPLETION_WAITING_DOTS="%F{yellow}waiting...%f"
# Caution: this setting can cause issues with multiline prompts in zsh < 5.7.1 (see #5765)
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git command-not-found tmux fzf ssh-agent zsh-syntax-highlighting zsh-autosuggestions)
source $ZSH/oh-my-zsh.sh

# zsh-syntax-highlighting
ZSH_HIGHLIGHT_HIGHLIGHTERS=(main brackets pattern)
ZSH_HIGHLIGHT_STYLES[default]=none
ZSH_HIGHLIGHT_STYLES[unknown-token]=fg=red,bold
ZSH_HIGHLIGHT_STYLES[reserved-word]=fg=cyan,bold
ZSH_HIGHLIGHT_STYLES[suffix-alias]=fg=green,underline
ZSH_HIGHLIGHT_STYLES[global-alias]=fg=magenta
ZSH_HIGHLIGHT_STYLES[precommand]=fg=green,underline
ZSH_HIGHLIGHT_STYLES[commandseparator]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[autodirectory]=fg=green,underline
ZSH_HIGHLIGHT_STYLES[path]=underline
ZSH_HIGHLIGHT_STYLES[path_pathseparator]=
ZSH_HIGHLIGHT_STYLES[path_prefix_pathseparator]=
ZSH_HIGHLIGHT_STYLES[globbing]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[history-expansion]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[command-substitution]=none
ZSH_HIGHLIGHT_STYLES[command-substitution-delimiter]=fg=magenta
ZSH_HIGHLIGHT_STYLES[process-substitution]=none
ZSH_HIGHLIGHT_STYLES[process-substitution-delimiter]=fg=magenta
ZSH_HIGHLIGHT_STYLES[single-hyphen-option]=fg=magenta
ZSH_HIGHLIGHT_STYLES[double-hyphen-option]=fg=magenta
ZSH_HIGHLIGHT_STYLES[back-quoted-argument]=none
ZSH_HIGHLIGHT_STYLES[back-quoted-argument-delimiter]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[single-quoted-argument]=fg=yellow
ZSH_HIGHLIGHT_STYLES[double-quoted-argument]=fg=yellow
ZSH_HIGHLIGHT_STYLES[dollar-quoted-argument]=fg=yellow
ZSH_HIGHLIGHT_STYLES[rc-quote]=fg=magenta
ZSH_HIGHLIGHT_STYLES[dollar-double-quoted-argument]=fg=magenta
ZSH_HIGHLIGHT_STYLES[back-double-quoted-argument]=fg=magenta
ZSH_HIGHLIGHT_STYLES[back-dollar-quoted-argument]=fg=magenta
ZSH_HIGHLIGHT_STYLES[assign]=none
ZSH_HIGHLIGHT_STYLES[redirection]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[comment]=fg=black,bold
ZSH_HIGHLIGHT_STYLES[named-fd]=none
ZSH_HIGHLIGHT_STYLES[numeric-fd]=none
ZSH_HIGHLIGHT_STYLES[arg0]=fg=green
ZSH_HIGHLIGHT_STYLES[bracket-error]=fg=red,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-1]=fg=blue,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-2]=fg=green,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-3]=fg=magenta,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-4]=fg=yellow,bold
ZSH_HIGHLIGHT_STYLES[bracket-level-5]=fg=cyan,bold
ZSH_HIGHLIGHT_STYLES[cursor-matchingbracket]=standout

# zsh-autosuggestions
#ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=244"  # choose when using 256-color theme
ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#999999"

# fzf
[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
#fzcode() { print -z `cat ~/.fzcode/{posts,ppn} | fzf --tac --cycle --height=~50% --color=16` }
SharpCollection() { print -z `curl -sSL "https://api.github.com/repos/Flangvik/SharpCollection/git/trees/master?recursive=1" | jq -r ".tree[].path" | grep \\.exe | while read line; do echo "curl -sSL https://github.com/Flangvik/SharpCollection/raw/master/$line -o"; done | fzf --tac --cycle --height=~50% --color=16` }
Feroxbuster-w() { print -z `([ -d /usr/share/seclists ] && find /usr/share/seclists/Discovery/Web-Content -maxdepth 1 -type f || find /usr/share/wordlists/dirbuster/ -maxdepth 1 -type f) | sort | while read line; do echo "feroxbuster -w $line -A -k -r -t 15 -n -u"; done | fzf --tac --cycle --height=~50% --color=16` }
Ffuf-w() { print -z `([ -d /usr/share/seclists ] && find /usr/share/seclists/Discovery/Web-Content -maxdepth 1 -type f || find /usr/share/wordlists/dirbuster/ -maxdepth 1 -type f) | sort | while read line; do echo "ffuf -w $line -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36' -ic -sf -r -c -t 15 -mc all -u"; done | fzf --tac --cycle --height=~50% --color=16` }
Httpx-p() { print -z `(echo 'httpx -sc -fr -location -title -server -td -method -ip -cname -cdn -p "80,81,443,1080,3000,3128,7001,7002,8080,8443,8888" -t 15 -l'; echo 'httpx -sc -fr -location -title -server -td -method -ip -cname -cdn -t 15 -l') | fzf --tac --cycle --height=~50% --color=16` }

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

export PATH="${PATH}:${HOME}/.local/bin/"
export GOPATH=$HOME/go
export PATH=$PATH:/usr/local/go/bin:$HOME/go/bin:$HOME/.local/bin:$PATH:/snap/bin:$HOME/.cargo/env:$HOME/.cargo/bin/

alias vim='nvim'
alias o='obsidian &>/dev/null & disown'
alias ؤمثشق='clear'
alias disable_aslr='echo 0 | sudo tee /proc/sys/kernel/randomize_va_space'
alias enable_aslr='echo 2 | sudo tee /proc/sys/kernel/randomize_va_space'
alias battery='upower -i /org/freedesktop/UPower/devices/battery_BAT0'
alias hdd="cd /mnt/hdd"
alias wifi-list='nmcli dev wifi'
alias clipboard="xclip -sel clip"
alias windows-exploit-suggester="$(which wes)"
alias pullall="ls | xargs -P10 -I{} git -C {} pull"


HtbEnv(){
  if [[ -f ~/.tmuxinator/ && -f ~/.tmuxinator/htb.yml ]]
  then
    echo "[+] Starting HTB Session in 3 Seconds"
    sleep 3
    tmuxinator start htb
  else:
    echo "[!] htb.yml is not found"
  fi
}

wificonnect(){
	local RED='\033[0;31m'
	local NC='\033[0m'
	if [ "$#" -ne  "0" ];
	then
		nmcli device wifi connect "$1" password "$2"
	else
		echo -e "${RED}[!] Usage: $0 <WIFI-SSID> <PASSWORD>${NC}"
	fi
}

wifidisconnect(){
	local RED='\033[0;31m'
  local NC='\033[0m'
	if [ "$#" -ne "0" ];
	then
		nmcli device disconnect "$1"
	else
		echo -e "${RED}[!] Usage: $0 <WIFI-SSID>${NC}"
	fi
}

ctf_init(){
	local RED='\033[0;31m'
  local NC='\033[0m'
	if [ "$#" -ne "0" ];
	then
		mkdir -p "$1"/{web,forensics,reverse,pwn}
	else
		echo -e "${RED}[!] Usage: $0 <CTF-NAME> ${NC}"
	fi
}
# Fix keyboard layout
setxkbmap -option 'grp:alt_shift_toggle' -layout us,ar -variant ,qwerty -model pc105

# pwninit (auto patch binarieera)

[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh
function rtfm() { ~/tools/rtfm/rtfm.py "$@" 2>/dev/null }
