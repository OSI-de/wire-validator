MIN_SECTION = 0.5
class Wire:
     def __init__(self, wire, section):
          self.wire = wire
          if section:
               self.section= float(section)
          else:
               self.section=None

     def check_cross_section(self):
        if self.section is None:
            return "Kein Querschnitt"
        if self.section < MIN_SECTION:
               return "Kleiner Leitungsquerschnitt"
        return "OK"
     def is_valid(self):
         return bool(self.wire) and self.section is not None