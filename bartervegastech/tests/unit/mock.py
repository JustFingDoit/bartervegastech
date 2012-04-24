'''Mocks'''
from bartervegastech.dbmodels.barterdb import UserFactory


class MockUserFactory(object):
    id_iter = 0
    users = {}

    def __init__(self):
        self._add_user('Ben', 'Hur')

    def get(self, name):
        return self.users.get(name)

    def create_user(self, username, password):
        self._add_user(username, password)

    def __iter__(self):
        return iter(self.users)

    def _add_user(self, username, password):
        from bartervegastech.dbmodels.barterdb import UserAccount
        self.id_iter += 1
        user = UserAccount(username, password)
        user.id = self.id_iter
        self.users[username] = user

    def delete(self, id_):
        for name, user in self.users.items():
            if user.id == id_:
                del self.users[name]
                break


class MockFactory(object):

    def __init__(self):
        self.id_iter = 0
        self.objects = {}

    def get(self, name):
        return self.objects.get(name)

    def delete(self, id_):
        for name, object in self.objects.items():
            if object.id == id_:
                del self.objects[name]
                break

    def add(self, object_):
        self.id_iter += 1
        object_.id = self.id_iter
        self.objects[object_.name] = object_
        return object_

    def __iter__(self):
        return iter(self.objects)

    def get_by_id(self, id_):
        for name, obj in self.objects.items():
            if obj.id == id_:
                return obj


        
