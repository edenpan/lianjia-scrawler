# coding=utf-8
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
    # info_dict = {'houseID': "121", 'totalPrice': '121100'}
    info_dict = {"id":121, "title":u'京基御景华城', "link":'https://sz.lianjia.com/xiaoqu/121', 'district': u'福田区', 'bizcircle': u'赤尾1', 'tagList': u'近地铁7号线赤尾站'\
     ,'onsale':'1', 'year':'' }
    # hisprice_data_source.append(
                    # {"houseID": info_dict["houseID"], "totalPrice": info_dict["totalPrice"]})
    # model.Hisprice.insert_many(
    #                 hisprice_data_source).upsert().execute()                    

    # model.Hisprice.insert_many(hisprice_data_source).on_conflict(conflict_target=[model.Hisprice.houseID,model.Hisprice.totalPrice], preserve=[model.Hisprice.totalPrice],update={}).execute()                    
    model.Community.insert(info_dict).on_conflict(conflict_target=[model.Community.id], preserve=[model.Community.title, model.Community.link, model.Community.district, \
                model.Community.bizcircle, model.Community.tagList, model.Community.onsale, model.Community.onrent, model.Community.year, \
                model.Community.housetype, model.Community.cost, model.Community.service, \
                model.Community.company, model.Community.building_num, model.Community.house_num, \
                model.Community.price, model.Community.city],update={}).execute()

if __name__ == "__main__":
    # originalCode()
    regionlist = settings.REGIONLIST  # only pinyin support
    city = settings.CITY
    # model.database_init()
    core.GetCommunityByRegionlist(city, regionlist)
    # communitylist = get_communitylist(city)
    # core.GetHouseByCommunitylist(city, communitylist)
    # core.GetSellByCommunitylist(city, communitylist)
    # testUpsertDB()
    

