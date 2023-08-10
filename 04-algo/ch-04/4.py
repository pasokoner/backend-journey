def get_num_verified_in_audience(influencer, count=0, influencers_counted=None):
    if influencers_counted == None:
        influencers_counted = set()

    if influencer.name in influencers_counted:
        return 0

    print(influencer.name)

    influencers_counted.add(influencer.name)

    count += int(influencer.is_verified)
    for follower in influencer.followers.keys():
        count += get_num_verified_in_audience(
            influencer.followers[follower],
            count=0,
            influencers_counted=influencers_counted,
        )

    return count


# don't touch below this line


class Influencer:
    def __init__(self, name, is_verified):
        self.name = name
        self.is_verified = is_verified
        self.followers = {}


def test(influencer):
    result = get_num_verified_in_audience(influencer)
    print(f"{influencer.name} has {result} verified followers in their audience")
    print("====================================")


def main():
    tiff = Influencer("Tiff", False)
    john = Influencer("John", False)
    amit = Influencer("Amit", True)
    jake = Influencer("Jake", False)
    dan = Influencer("Dan", False)
    steph = Influencer("Steph", True)
    jess = Influencer("Jess", True)
    jill = Influencer("Jill", False)
    mike = Influencer("Mike", False)
    courtland = Influencer("Courtland", True)

    tiff.followers = {
        john.name: john,
        amit.name: amit,
        jake.name: jake,
        dan.name: dan,
    }

    amit.followers = {
        steph.name: steph,
        jess.name: jess,
    }

    dan.followers = {
        tiff.name: tiff,
        jill.name: jill,
        mike.name: mike,
        courtland.name: courtland,
    }

    test(tiff)
    test(amit)
    test(dan)


main()
