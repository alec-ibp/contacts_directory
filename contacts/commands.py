from contacts.model import Contact
from contacts.services import Contact_service
from tabulate import tabulate
import click


@click.group() # comando principal que administra los siguientes comandos
def contacts():
    """ Manage the conctacts functions """
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
    contact_service = Contact_service(context.obj['table_name'])
    contact_service.create_contact(Contact(name, company, email, job))


@contacts.command()
@click.pass_context
def list(context):
    contact_service = Contact_service(context.obj['table_name'])
    contact_list = contact_service.list_contacts()

    header = [fields for fields in Contact.schema()]
    table = []

    for contact in contact_list:
        table.append(
            [
                contact['name'],
                contact['company'],
                contact['email'],
                contact['job'],
                contact['uid'],
            ]
        )
    click.echo(tabulate(table,header))


@contacts.command()
@click.argument('contact_name', type=str)
@click.pass_context
def update(context, contact_name):
    """ Update a contact - require the contact name at the command line """
    contact_service = Contact_service(context.obj['table_name'])
    contact = _search_contact(contact_service, contact_name)

    if contact:
        contact = _update_contact_data(Contact(**contact[0]))
        contact_service.update_contacts(contact)
        click.echo('contact updated')
    else:
        click.echo('the contact doesnt exist')
    

@contacts.command()
@click.argument('contact_name',type=str)
@click.pass_context
def delete(context, contact_name):
    """ Delete a contact - require the contact name at the command line """
    contact_service = Contact_service(context.obj['table_name'])
    contact = _search_contact(contact_service, contact_name)

    if contact:
        contact_service.delete(contact[0])
        click.echo('Client deleted')
    else:
        click.echo('Client not found')
    

def _search_contact(contact_service, contact_name):
    contact_list = contact_service.list_contacts()
    contact = [contact for contact in contact_list if contact['name'].lower() == contact_name.lower()]

    return contact
    

def _update_contact_data(contact):

    click.echo('Leave empty if you dont want to modify the value')

    contact.name = click.prompt('New name', type=str, default=contact.name)
    contact.company = click.prompt(
        'New company', type=str, default=contact.company)
    contact.email = click.prompt('New email', type=str, default=contact.email)
    contact.job = click.prompt('New job', type=str, default=contact.job)

    return contact


c_commands = contacts
