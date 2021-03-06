from __future__ import with_statement

from twisted.application import internet, service
from twisted.internet import protocol, reactor
from twisted.protocols import basic
from twisted.python import log
from twisted.protocols.policies import TimeoutMixin

class FlashPolicyProtocol(basic.LineOnlyReceiver, TimeoutMixin):
    delimiter = '\0'
    MAX_LENGTH = 64
    TIMEOUT = 15 # seconds

    def __init__(self):
        self.setTimeout(self.TIMEOUT)

    def lineReceived(self, request):
        if request != '<policy-file-request/>':
            self.transport.loseConnection()
            return
        self.transport.write(self.factory.response_body)
        self.resetTimeout()

class FlashPolicyFactory(protocol.ServerFactory):
    protocol = FlashPolicyProtocol

    def __init__(self):
        with open('/etc/flashpolicy.xml', 'rb') as f:
            self.response_body = f.read() + '\0'

application = service.Application('flashpolicy')
internet.TCPServer(843, FlashPolicyFactory()).setServiceParent(service.IServiceCollection(application))
