#!/usr/bin/env python3

from outline_text import outline
import click

@click.command()
@click.argument('phrase')
@click.option('-w', '--width', type=int)
@click.option('-h', '--height', default=3, type=int)
@click.option('-f', '--filler', default=' ', type=str)
@click.option('-r', '--frame', default='#', type=str)
@click.option('--header', is_flag=True)
@click.option('--footer', is_flag=True)
def main(phrase, width, height, filler, frame, header, footer):
    outline(phrase, width=width, height=height, filler=filler, frame=frame, header=header, footer=footer, print_output=True)


if __name__ == '__main__':
    main()