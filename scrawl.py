import core
import model
import settings
from peewee import *
import datetime



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

def testUpsertDB():
    hisprice_data_source = []
    info_dict = {"houseID":121, "totalPrice":111000 }
    hisprice_data_source.append(
                    {"houseID": info_dict["houseID"], "totalPrice": info_dict["totalPrice"]})
    # model.Hisprice.insert_many(
    #                 hisprice_data_source).upsert().execute()                    

    model.Hisprice.insert_many(hisprice_data_source).on_conflict(conflict_target=[model.Hisprice.houseID,model.Hisprice.totalPrice], preserve=[model.Hisprice.totalPrice],update={}).execute()                    

if __name__ == "__main__":
    # originalCode()
    regionlist = settings.REGIONLIST  # only pinyin support
    city = settings.CITY
    model.database_init()
    core.GetCommunityByRegionlist(city, regionlist)
    # communitylist = get_communitylist(city)
    # core.GetHouseByCommunitylist(city, communitylist)
    # core.GetSellByCommunitylist(city, communitylist)
    # testUpsertDB()
    

