import os
import csv
from contacts.model import Contact

class Contact_service:

    def __init__(self,table_name) -> None:
        self.table_name = table_name

    def create_contact(self, contact):
        with open(self.table_name, mode='a', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=Contact.schema())
            writer.writerow(contact.to_dict())
    
    def list_contacts(self):
        with open(self.table_name, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f,fieldnames=Contact.schema())
            return list(reader)

    def update_contacts(self, contact_updated):
        contact_list = self.list_contacts()
        updated_list = []

        for contact in contact_list:
            if contact['uid'] == contact_updated.uid:
                updated_list.append(contact_updated.to_dict())
            else:
                updated_list.append(contact)

        self._save_to_disk(updated_list)

    def delete(self, contact_to_delete):
        contact_list = [contact for contact in self.list_contacts() if contact['uid'] != contact_to_delete['uid']]
        self._save_to_disk(contact_list)
    

    def _save_to_disk(self, contacts):
        tmp_table = self.table_name + '.tmp'
        with open(tmp_table,mode='w', encoding='utf-8') as f:
            writer = csv.DictWriter(f,fieldnames=Contact.schema())
            writer.writerows(contacts)
        
        os.remove(self.table_name)
        os.rename(tmp_table, self.table_name)
