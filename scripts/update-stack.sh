set -e
set -x


tutum stack inspect scraper-$1 ||
tutum stack create --sync -f stacks/$1.yml -n scraper-$1
tutum stack update --sync -f stacks/$1.yml scraper-$1
