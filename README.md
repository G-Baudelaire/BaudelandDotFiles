# Managing Repo

## Create Repo

Files are tracked via git fom `~/.dotfiles`.
Clone the contents of the repo into `~/.dotfiles`.

```
echo "alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME" >> $HOME/.zshrc
source ~/.zshrc
config config --local status.showUntrackedFiles no
```

This adds and soruces an alias `config` that allows us to utilise the repo from anywhere without interfering with other git repos.

E.g.

```
config status
config add ~/.config/hypr/
```

## Installing the Repo

WIP: Not install script does not exist - only config files and scripts.

```
git clone --bare https://github.com/G-Baudelaire/BaudelandDotFiles.git $HOME/.dotfiles
echo "alias config='/usr/bin/git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME" >> $HOME/.zshrc
source ~/.zshrc
config checkout
```

Likely to give warnings about overwriting. Just remove the existing config files (this is for a fresh install), or back them up elsewhere.
