import requests
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import json
import xmltodict
import logging
import sys


logging.basicConfig(level=logging.INFO)


def get_xml_data(url):
    logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
    response = requests.get(url)
    response_xml = response.content.decode('utf-8')
    assert isinstance(response_xml, str)
    return response_xml


def xml_to_json_data(xml_data):
    logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
    xml_data = xmltodict.parse(xml_data)
    json_data = json.loads(json.dumps(xml_data))
    return json_data


def parse_json(json_data):
    logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
    items = json_data['response']['body']['items']['item']
    # logging.info(items)
    return items


def get_item(url):
    """:rtype = dict"""
    logging.info("Loaded Func %s ", sys._getframe().f_code.co_name)
    return parse_json(xml_to_json_data(get_xml_data(url)))


if __name__ == "__main__":
    service_key = "z78AYjaYuuQ8e58v4VEYfL95N4Gf74fK%2FiJHHKns6tvcPv77DsZZzDZ0uuxE5y33xLhzkLYcJKifHI8bb3c4zg%3D%3D"
    pharmacy_url = "http://apis.data.go.kr/B551182/pharmacyInfoService/getParmacyBasisList?serviceKey=" + service_key + "&pageNo=1&numOfRows=200"
    get_item(pharmacy_url)
