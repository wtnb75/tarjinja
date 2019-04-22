# tarjinja: template + archive/rsync

## Install

- python -m venv .
- ./bin/pip install tarjinja

## Install head

- git clone https://github.com/wtnb75/tarjinja
- cd tarjinja
- python -m venv .
- ./bin/pip install -U .


## Use

```
# ./bin/tarjinja
Usage: tarjinja [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  copy
  rsync
  tarc
  tarx
# ./bin/tarjinja copy --help
Usage: tarjinja copy [OPTIONS]

Options:
  --input PATH                    [required]
  --output PATH                   [required]
  --out-type [Tar|Zip|Dir|List]   [required]
  --in-type [Tar|Zip|Dir|Single]  [required]
  --filter-type [Jinja|Multi|ReverseJinja|ReverseTemplate|ReverseFormat|ReversePercent|ReverseFstring|Template|Format|Percent|Fstring]
  --value FILENAME
  --verbose / --no-verbose
  --thru TEXT
  --help                          Show this message and exit.
```

- [examples](examples)
- tarjinja copy --in-type Dir --input examples/ex1 --out-type Dir --output /tmp/ex1 --filter-type Jinja --value examples/ex1.yaml
    - ls -l /tmp/ex1
- tarjinja copy --in-type Dir --input examples/ex2 --out-type Tar --output /tmp/ex2.tar.gz --filter-type Jinja --value examples/ex2.yaml
    - tar tvfz /tmp/ex2.tar.gz
- tarjinja tarc --value examples/pythoncli.yaml /tmp/example1.zip examples/pythoncli
    - unzip -l /tmp/example1.zip
