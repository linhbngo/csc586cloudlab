import geni.portal as portal
import geni.rspec.pg as pg
pc = portal.Context()
request = pc.makeRequestRSpec()

tourDescription = \
"""
This profile provides a two-node set to study SSO. One node will be the LDAP server, and the other node is a client
who is to be authenticated using LDAP. 
"""

#
# Setup the Tour info with the above description and instructions.
#  
tour = IG.Tour()
tour.Description(IG.Tour.TEXT,tourDescription)
request.addTour(tour)

for i in range(2):
  if i == 0:
    node = request.XenVM("ldapserver")    
  else
    node = request.XenVM("ldapclient")
   
  node.routable_control_ip = "true"  
  node.disk_image = "urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD"
  
# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
