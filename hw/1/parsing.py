import requests
import json

cookies = {
    'yp': '1991832117.multib.1#1980679440.pcs.0#1697576599.pgp.2_27767338#1688585827.szm.1_25:1536x864:1536x752#1991832230.udn.cDpzbm9wb3ZkYW5pbDdAZ21haWwuY29t',
    'mda': '0',
    'yandexuid': '9954179351662633414',
    'yuidss': '9954179351662633414',
    'is_gdpr': '0',
    'is_gdpr_b': 'CL+ydhDliAEoAg==',
    '_yasc': 'kUr18BRNYo7hxRx9NZMcwhepPz0T9QzU4fN/VFTjWmPTd7PyD5LRSfBswwp4PImZAnbbe67ehpezBBE4ngqrtZEazjU=',
    'i': 'HIbs6ZZ8VWNOgA/OWCOY92YWFikv4DYtxmsk57dqVdJnvjCDxhXNP2fg/Ii1MPw8vDe07UVc2cwtSgK6GwyRWVFrDh4=',
    'my': 'YwA=',
    '_ym_uid': '16626334172737420',
    '_ym_d': '1694678146',
    'yashr': '216647901676365910',
    'gdpr': '0',
    'L': 'AQhncV0OBwACcFBfQXFRQX9oVVJfdE9qKyUFPDgmVxQYBTVEOFI9Fi8JeiQKPg==.1676472230.15254.333037.bd039d6157f9314d7e87931c2ff9276d',
    'yandex_login': 'snopovdanil7@gmail.com',
    'Session_id': '3:1695071971.5.0.1676472230461:z8OuVQ:d.1.2:1|1753469947.0.2.3:1676472230|3:10275951.729074.DYpjQtmxP09ajASnYQ-IjPJguw4',
    'sessionid2': '3:1695071971.5.0.1676472230461:z8OuVQ:d.1.2:1|1753469947.0.2.3:1676472230|3:10275951.729074.fakesign0000000000000000000',
    'skid': '7267353841679255289',
    'sessar': '1.1182.CiBDNj87odW1MsVraPhLdpEkuMEBEx0JQ4Hve9Gf0j0vKA.KyqP-j5oUIhJdnc8iMmCTm8QCKhfULfO_HHJZdJuLbM',
    'ymex': '2010038145.yrts.1694678145',
    'ys': 'udn.cDpzbm9wb3ZkYW5pbDdAZ21haWwuY29t#c_chck.1992622775',
    'Cookie_check': 'EgCcH6OX',
    'device_id': 'aaad0911d70b21e9114abc0b97c55d5f3d3f7e0b5',
    'active-browser-timestamp': '1695284605899',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'lastVisitedPage': '%7B%7D',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/117.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'yp=1991832117.multib.1#1980679440.pcs.0#1697576599.pgp.2_27767338#1688585827.szm.1_25:1536x864:1536x752#1991832230.udn.cDpzbm9wb3ZkYW5pbDdAZ21haWwuY29t; mda=0; yandexuid=9954179351662633414; yuidss=9954179351662633414; is_gdpr=0; is_gdpr_b=CL+ydhDliAEoAg==; _yasc=kUr18BRNYo7hxRx9NZMcwhepPz0T9QzU4fN/VFTjWmPTd7PyD5LRSfBswwp4PImZAnbbe67ehpezBBE4ngqrtZEazjU=; i=HIbs6ZZ8VWNOgA/OWCOY92YWFikv4DYtxmsk57dqVdJnvjCDxhXNP2fg/Ii1MPw8vDe07UVc2cwtSgK6GwyRWVFrDh4=; my=YwA=; _ym_uid=16626334172737420; _ym_d=1694678146; yashr=216647901676365910; gdpr=0; L=AQhncV0OBwACcFBfQXFRQX9oVVJfdE9qKyUFPDgmVxQYBTVEOFI9Fi8JeiQKPg==.1676472230.15254.333037.bd039d6157f9314d7e87931c2ff9276d; yandex_login=snopovdanil7@gmail.com; Session_id=3:1695071971.5.0.1676472230461:z8OuVQ:d.1.2:1|1753469947.0.2.3:1676472230|3:10275951.729074.DYpjQtmxP09ajASnYQ-IjPJguw4; sessionid2=3:1695071971.5.0.1676472230461:z8OuVQ:d.1.2:1|1753469947.0.2.3:1676472230|3:10275951.729074.fakesign0000000000000000000; skid=7267353841679255289; sessar=1.1182.CiBDNj87odW1MsVraPhLdpEkuMEBEx0JQ4Hve9Gf0j0vKA.KyqP-j5oUIhJdnc8iMmCTm8QCKhfULfO_HHJZdJuLbM; ymex=2010038145.yrts.1694678145; ys=udn.cDpzbm9wb3ZkYW5pbDdAZ21haWwuY29t#c_chck.1992622775; Cookie_check=EgCcH6OX; device_id=aaad0911d70b21e9114abc0b97c55d5f3d3f7e0b5; active-browser-timestamp=1695284605899; _ym_isad=2; _ym_visorc=b; lastVisitedPage=%7B%7D',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.4346034032624708',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx', params=params, cookies=cookies, headers=headers)
jd = json.loads(response.content)
jswd = []
for position in jd["chartPositions"]:
    jswd.append(({'number': position['track']['id'], 'title': position['track']['title'], 'artists': [artist['name'] for artist in position['track']['artists']]}))

with open ('result.json', 'w') as jf:
    jf.write(json.dumps({'tracks': jswd}, ensure_ascii=False))

