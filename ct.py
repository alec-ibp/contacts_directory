import click
from contacts import commands as contact_commands

CONTACTS_LIST = 'contacts.csv'

@click.group() # definir el punto de entrada la funcion se convierte en otro decorador
@click.pass_context
def cli(context):
    context.obj = {}
    context.obj['name_list'] = CONTACTS_LIST

cli.add_command(contact_commands.c_commands)