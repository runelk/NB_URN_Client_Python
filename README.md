Python Client for the URN PID service by the National Library of Norway
=======================================================================

This is a library and a set of command line tools for communicating with the SOAP ID service available at the National Library of Norway.

For more information (in Norwegian):
* Regarding URN: http://www.nb.no/idtjeneste/about_urn.jsf
* Regarding the SOAP API: http://www.nb.no/idtjeneste/about_urn_webservice.jsf


Library
-------
The **nb_urn_client** directory contains the library for communicating with the SOAP API.
It is a thin wrapper around the SOAP API calls. To see how it's used, take a look at the commands in the **bin** directory.


Command Line Tools
------------------

The **bin** directory contains a set of command line tools that make use of the library.

### Examples for command line tools:
To reserve the next available urn in some series:
```
./bin/reserve_next_urn --series-code foo:bar:prefix
```

The service will return information about the newly generated URN.
To add a URL to the newly generated URN (where foo is the URN adress returned from the previous step):

```
./bin/add_url --urn foo --url http://www.bar.com
```

To see that the URL was added, request information about the URN:

```
./bin/find_urn --urn foo
```

You can add more than one URL to a URN. To register one of them as the default URL for a URN:

```
./bin/set_default_url --urn foo --url http://www.bar.com
```

You can also request information for all URNs containing a specific URL:

```
./bin/find_urns_for_url --url http://www.bar.com
```

Configuration
-------------

The **config** directory contains an example of the YAML config file used by the client.
Replace the dummy entries with the information you have received from the National Library.


Dependencies
------------

* suds
* yaml

Recommendation: Create a [virtualenv](http://virtualenv.readthedocs.org/) and install these dependencies using [pip](http://pip.readthedocs.org/).

Testing
-------

The **test**-folder contains a unittest suite for testing against a mockservice
(currently not included in the repository)
Go to the test folder and run nosetests without log capture
(nose barfs on something in the suds library):

```
nosetests --nologcapture
```
