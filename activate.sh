# Git commit hook
if [ ! -f .git/hooks/pre-commit ]; then
    echo -e "#!/bin/sh\n\n\nmario test" > .git/hooks/pre-commit
    chmod +x .git/hooks/pre-commit
fi

# Python env
virtualenv venv -p python2
source venv/bin/activate
pip install -Urrequirements.dev.txt
