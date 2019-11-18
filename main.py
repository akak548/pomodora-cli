import click
import os
import pomo

@click.group()
@click.option('--debug/--no-debug', default=False)
@click.pass_context
def cli(ctx,debug):
    ctx.pomo = pomo.Client()

@cli.command()
def init(ctx):
    click.echo('Initializing')

@cli.command()
def start(ctx):
    click.echo('Starting')
    
@cli.command()
def status(ctx):
    click.echo('Display Current Status')

@cli.command()
def report(ctx):
    click.echo('Generate report desplay')

if __name__ == '__main__':
    cli()
