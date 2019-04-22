import click
from logging import getLogger, basicConfig, INFO, DEBUG

log = getLogger(__name__)

VERSION = "{{version|default("unknown")}}"


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        print(ctx.get_help())


def set_verbose(flag):
    fmt = '%(asctime)s %(levelname)s %(message)s'
    if flag:
        basicConfig(level=DEBUG, format=fmt)
    else:
        basicConfig(level=INFO, format=fmt)


@cli.command()
def subcmd():
    click.echo("{{name}} subcommand")


if __name__ == "__main__":
    cli()
