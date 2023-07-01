# Get https certificate details
> This is my awesome Flask project. It does amazing things!

Allows to obtain information about the certificate of a domain over https.

1. Reads a txt file containing the domain addresses.
2. Creates a connection with the url and through sockets obtains the certificate data.
3. Builds a json with the obtained data
4. It makes the information available as a service. 

![](header.png)

## Installation

OS X & Linux or Windows:

1. Clone the repository:

```sh
git clone https://github.com/peedpy/obtain_certificate_https_details.git
```

2. Install the dependencies:

```sh
pip install -r requirements.txt
```

## Usage example
1. python app.py 8001

2. Open your web browser and visit [http://localhost:8001/obtain_certificates_status](http://localhost:8001/obtain_certificates_status)

3. Output:

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
      "emitted_on": "Jun 7 12:13:43 2023 GMT",
      "expired_on": "Sep 5 12:13:42 2023 GMT",
      "name": "https://nissei.com",
      "remaining_days": "65 days, 17:53:17"
    },
    {
      "certificate_expired": true,
      "emitted_on": "Jun 7 12:13:43 2023 GMT",
      "expired_on": "Sep 5 12:13:42 2023 GMT",
      "name": "http://embajadadeluruguay.com.py"
    }
  ],
  "01/07/23",
  "18:16:06"
]


## Release History

* 0.0.1
    * Work in progress

## Contributing

1. Fork it (<https://github.com/peedpy/obtain_certificate_https_details.git>)
2. Create your feature branch (`git checkout -b feature/x`)
3. Commit your changes (`git commit -am 'Add some x'`)
4. Push to the branch (`git push origin feature/x`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
