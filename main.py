import click
import os
import pomo

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['pomo'] = pomo.Client()

@cli.command()
@click.pass_context
def init(ctx):
    click.echo('Initializing')

@cli.command()
@click.pass_context
def start(ctx):
    click.echo('Starting pomo session')
    try:
        ctx.obj['pomo'].start_session()
    except Exception as e:
        click.echo(e)
        click.echo("Quit pomo session, something went wrong")


@cli.command()
@click.pass_context
def status(ctx):
    click.echo('Display Current Status')
    try:
        ctx.obj['pomo'].check_session()
    except Exception as e:
        click.echo(e)
        click.echo("Quit pomo session, something went wrong")

@cli.command()
@click.pass_context
def report(ctx):
    click.echo('Generate report desplay')

if __name__ == '__main__':
    cli(obj={})
