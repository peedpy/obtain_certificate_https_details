# obtain_certificate_https_details
#INPUTS
$ python app.py

#OUTPUT
No port has been defined!

#INPUTS
$ python app.py 7000
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on

#OUTPUT
#LOG
URL without http/s[url2]:  www.abc.com.py
TLSv1.3
{'subject': [[['commonName', 'abccolor.web.arc-cdn.net']]], 'issuer': [[['countryName', 'US']], [['organizationName', "Let's Encrypt"]], [['commonName', 'R3']]], 'version': 3, 'serialNumber': '03F2578076ADA7924A0D8751217484E66A2A', 'notBefore': 'Jun 22 12:16:12 2023 GMT', 'notAfter': 'Sep 20 12:16:11 2023 GMT', 'subjectAltName': [['DNS', 'abccolor.web.arc-cdn.net'], ['DNS', 'www.abc.com.py']], 'OCSP': ['http://r3.o.lencr.org'], 'caIssuers': ['http://r3.i.lencr.org/']}
datetime_expired: 2023-09-20 12:16:11
datetime_now:     2023-07-01 18:20:24
dif: 80 days, 17:55:47
--------------------------------------------------

URL without http/s[url2]:  nissei.com
TLSv1.2
{'subject': [[['commonName', 'nissei.com']]], 'issuer': [[['countryName', 'US']], [['organizationName', "Let's Encrypt"]], [['commonName', 'R3']]], 'version': 3, 'serialNumber': '047CF9831AE76C9B1F22C7A5EAF32C551C7C', 'notBefore': 'Jun  7 12:13:43 2023 GMT', 'notAfter': 'Sep  5 12:13:42 2023 GMT', 'subjectAltName': [['DNS', 'nissei.com'], ['DNS', 'www.nissei.com']], 'OCSP': ['http://r3.o.lencr.org'], 'caIssuers': ['http://r3.i.lencr.org/']}
datetime_expired: 2023-09-05 12:13:42
datetime_now:     2023-07-01 18:20:25
dif: 65 days, 17:53:17
--------------------------------------------------


http://localhost:8001/obtain_certificates_status
[
  [
    {
      "certificate_expired": false, 
      "emitted_on": "Jun 22 12:16:12 2023 GMT", 
      "expired_on": "Sep 20 12:16:11 2023 GMT", 
      "name": "https://www.abc.com.py", 
      "remaining_days": "80 days, 17:55:47"
    }, 
    {
      "certificate_expired": false, 
      "emitted_on": "Jun  7 12:13:43 2023 GMT", 
      "expired_on": "Sep  5 12:13:42 2023 GMT", 
      "name": "https://nissei.com", 
      "remaining_days": "65 days, 17:53:17"
    }, 
    {
      "certificate_expired": true, 
      "emitted_on": "Jun  7 12:13:43 2023 GMT", 
      "expired_on": "Sep  5 12:13:42 2023 GMT", 
      "name": "http://embajadadeluruguay.com.py"
    }
  ], 
  "01/07/23", 
  "18:16:06"
]




#Some commands
 site:.com.py -inurl:http
 site:.com.py -inurl:https