# encoding=utf8  #编码
import json
import urllib.request


# 基于百度地图API下的经纬度信息来解析地理位置信息
def getlocation(lat, lng):
    # 31.809928, 102.537467, 3019.300
    # lat = '31.809928'
    # lng = '102.537467'
    url = 'http://api.map.baidu.com/reverse_geocoding/v3/?ak=QsmV82HINEAPblwWGaLXAj4L5p9BWvY2&output=json&coordtype=wgs84ll&location=%s,%s' % (
    lat, lng)
    req = urllib.request.urlopen(url)  # json格式的返回数据
    res = req.read().decode()  # 将其他编码的字符串解码成unicode
    print(res)
    return json.loads(res)


# json序列化解析数据(lat:纬度，lng:经度)
def jsonFormat(lat, lng):
    str = getlocation(lat, lng)
    dictjson = {}  # 声明一个字典
    # get()获取json里面的数据
    jsonResult = str.get('result')
    address = jsonResult.get('addressComponent')
    # 国家
    country = address.get('country')
    # 国家编号（0：中国）
    country_code = address.get('country_code')
    # 省
    province = address.get('province')
    # 城市
    city = address.get('city')
    # 城市等级
    city_level = address.get('city_level')
    # 县级
    district = address.get('district')
    # 把获取到的值，添加到字典里（添加）
    dictjson['country'] = country
    dictjson['country_code'] = country_code
    dictjson['province'] = province
    dictjson['city'] = city
    dictjson['city_level'] = city_level
    dictjson['district'] = district
    return dictjson


if __name__ == '__main__':
    # a=getlocation('47.919815','29.252728')

    print(jsonFormat('29.252728','47.919815'))
