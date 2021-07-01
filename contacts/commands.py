import click


@click.group() # comando principal que administra los siguientes comandos
def contacts():
    """ Manage the clients functions """
    pass


@contacts.command()
@click.option('-n', '--name',
              type=str,
              prompt=True,
              help='The contact name')

@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The contact company')

@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The contact email')

@click.option('-j', '--job',
              type=str,
              prompt=True,
              help='The contact job')
@click.pass_context
def create(context, name, company, email, job):
    """ Create a new contact in your list """
    pass


@click.command()
@click.argument('contact_name', type=str)
@click.pass_context
def update(context, contact_name):
    """ Update a contact - require the contact name at the command line """

    pass





c_commands = contacts