## How to use Prewikka apps

### Requirements

You need Prewikka 5.0.0 or higher.

### Source

The git repo for Prewikka apps is available on [GitHub](https://github.com/Prelude-SIEM-Contrib/prewikka-apps-twitter) and can be cloned like this:

    git clone https://github.com/Prelude-SIEM-Contrib/prewikka-apps-twitter.git

### Install

Once the source code downloaded:

    python setup.py install

Configure /etc/prewikka/prewikka.conf and add this for PreludeSIEM twitter account:

    [twitter]
    account: PreludeSIEM
    widget-id: 721615793658728448

Then restart Prewikka.

### License

The code is released under the GPLv2 license. See the COPYING file.

### Development

Please feel free to propose your own Prewikka apps by submitting a pull request.
