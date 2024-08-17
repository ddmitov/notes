# Create repository:
git init
git add *.*
git commit -m 'initial commit'
git remote add repository https://github.com/user/repository.git
git pull https://github.com/user/repository.git
git push repository master

# Create git web page:
git clone https://github.com/user/repository.git
cd repository
git checkout --orphan gh-pages
git rm -rf .
git add index.html
git commit -a -m 'readme page commit'
git push origin gh-pages

# Synchronize local repo with remote one:
git pull https://github.com/user/repository.git

# Synchronize a fork:
git clone https://github.com/user/fork-repository
git remote -v
git remote add upstream https://github.com/user/upstream-repository
git remote -v
git fetch upstream
git checkout master
git merge upstream/master
git push origin master

# Create a branch:
git checkout -b feat/title
git status

# Commit to a branch:
git add directory
git commit -m 'label'
git pull https://user:token@github.com/user/repository.git
git push https://user:token@github.com/user/repository.git feat/title

# Add submodule:
git submodule add https://github.com/user/repo-of-the-submodule-source ./relative/path/in/the/target/repo

# Remove a branch:
git branch --delete feat/title
git push origin --delete feat/title
