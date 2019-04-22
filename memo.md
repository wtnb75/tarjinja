# TODO

- rsync (--delete)
- expand python array (!= braceexpand)
- jinja extension
    - jinja2-time
    - jinja2-ospath
    - jinja2-stringcase
    - etc...
- output
    - prefix(tar)
- input
    - ignore, prune
    - filelist
- subcommands
    - tar/unzip compatible subcommands
    - rsync compatible subcommands

# DONE

- make cli
- reverse
    - raw string, dict -> template string
- copy mtime

## refactor

- separate input, filter, output
- pipeline
    - merge input, filter, output
- input
    - walk files
    - emit filter
    - tarfile, zipfile, dir, single file
- filter
    - apply template
    - emit output
    - jinja, string.Template, string.format, %, django
- output
    - write files
    - tarfile, zipfile, dir
