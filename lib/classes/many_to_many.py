import re

class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name

        NationalPark.all.append(self)
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if not hasattr(self, 'name') and isinstance(name, str) and len(name) >= 3:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        unique_list = []
        total_list = [trip.visitor for trip in Trip.all if trip.national_park == self]

        for visitor in total_list:
            if visitor not in unique_list:
                unique_list.append(visitor)
        
        return unique_list
    
    def total_visits(self):
        return len([trip for trip in Trip.all if trip.national_park == self])
    
    def best_visitor(self):
        best = None
        # visitors = self.visitors()

        for visitor in self.visitors():
            if not best:
                best = visitor
            elif visitor.total_visits_at_park(self) > best.total_visits_at_park(self):
                best = visitor
        
        return best
            
class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date

        Trip.all.append(self)
    
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        pattern = r'[a-zA-z]+\s{1}[0-9]{1,2}[a-z]{2}'
        regex = re.compile(pattern)

        if  isinstance(start_date, str) and regex.match(start_date) and len(start_date) >= 7:
            self._start_date = start_date
    
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        pattern = r'[A-z]+\s{1}[0-9]{1,2}[a-z]{2}'
        regex = re.compile(pattern)

        if isinstance(end_date, str) and regex.match(end_date) and len(end_date) >- 7:
            self._end_date = end_date
    
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        self._visitor = visitor
    
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        self._national_park = national_park




class Visitor:

    all = []

    def __init__(self, name):
        self.name = name

        Visitor.all.append(self)
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        unique_list = []
        total_list = [trip.national_park for trip in Trip.all if trip.visitor == self]

        for nat_park in total_list:
            if nat_park not in unique_list:
                unique_list.append(nat_park)
        
        return unique_list
    
    def total_visits_at_park(self, park):
        print(len([trip for trip in Trip.all if trip.visitor == self and trip.national_park == park]))
        return len([trip for trip in Trip.all if trip.visitor == self and trip.national_park == park])