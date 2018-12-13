import core
import model
import settings


def get_communitylist(city):
    res = []
    for community in model.Community.select():
        if community.city == city:
            res.append(community.title)
    return res

def originalCode():
    
    core.GetHouseByRegionlist(city, regionlist)
    core.GetRentByRegionlist(city, regionlist)
    # Init,scrapy celllist and insert database; could run only 1st time
    core.GetCommunityByRegionlist(city, regionlist)
    communitylist = get_communitylist(city)  # Read celllist from database
    core.GetSellByCommunitylist(city, communitylist)

if __name__ == "__main__":
    # originalCode()
    regionlist = settings.REGIONLIST  # only pinyin support
    city = settings.CITY
    # model.database_init()
    # core.GetCommunityByRegionlist(city, regionlist)
    communitylist = get_communitylist(city)
    core.GetHouseByCommunitylist(city, communitylist)
    core.GetSellByCommunitylist(city, communitylist)

