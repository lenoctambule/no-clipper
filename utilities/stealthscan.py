import bannergrab as bg

class StealthScan:
   hosts_batch = list(bg.Host)
   port_list = [20,21,22,80,443,1337,8080]

   def __init__(self) -> None:
       pass

   def

   def genbatch_from_mask(self, mask : str) -> bool :
       pass

   def set_batch(self, batch : list(bg.Host)) -> bool :
       pass

   def set_portlist(self, port_list : list(int)) -> None:
       for i in port_list :
          if not (i > 0 or i < 65536) :
             raise Exception("Invalid port.")
       self.port_list = port_list
