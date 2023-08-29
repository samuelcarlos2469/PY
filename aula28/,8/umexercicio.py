class ContactList(list):
    def search(self,name):
        matching_contacts = [c for c in self
                             if name in c.name]
        return matching_contacts
