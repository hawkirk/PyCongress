from .client import Client


class MemberClient(Client):

    def get(self, bioguide=None, sponsor_type=None):
        if bioguide and sponsor_type:
            path = "member/{}/{}.json".format(
                bioguide,
                sponsor_type
            )

        elif bioguide:
            path = "member/{}.json".format(
                bioguide
            )

        else:
            path = "member.json"

        return self.fetch(path)

    def list_members(self):
        """
        Returns a list of congressional members.
        """
        return self.get()

    def member_info(self, bioguide):
        """
        Returns detailed information for a specified congressional member.
        """
        return self.get(
            bioguide=bioguide)

    def sponsored_legislation(self, bioguide, sponsor_type='sponsored-legislation'):
        """
        Returns the list of legislation sponsored or cosponsored by a specified
        congressional member.
        """
        sponsor_types = ['sponsored-legislation', 'cosponsored-legislation']
        if sponsor_type not in sponsor_types:
            raise ValueError("Invalid sponsor type. Expected one of: %s" % sponsor_types)
        return self.get(
            bioguide=bioguide,
            sponsor_type=sponsor_type)
