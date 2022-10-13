from .client import Client


class MemberClient(Client):

    def get(self, bioguide=None):
        if bioguide:
            path = "member/{}.json".format(
                bioguide
            )

        else:
            path = "member.json"

        return self.fetch(path)

    def all_members(self):
        return self.get()

    def member_details(self, bioguide):
        return self.get(
            bioguide=bioguide)
