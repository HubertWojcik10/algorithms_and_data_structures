
from itu.algs4.searching.red_black_bst import RedBlackBST
import datetime

'''
This is my solution to the Kattis Flights problem (week 11). 
The problem is to maintain the flight schedule at a given airport.

In week 11, we learned about red-black trees, which I used to solve this problem.
'''


class Flights:
    def __init__(self, n):
        self.n = n
        self.time_format = '%H:%M:%S'
        self._st = self._schedule()

    def _str_to_date(self, t):
        d = datetime.datetime.strptime(t, self.time_format)
        return d

    def _date_to_time(self, t):
        s = t.strftime(self.time_format)
        return s

    def _schedule(self):
        '''creates a schedule of flights'''
        st = RedBlackBST()
        for _ in range(self.n):
            time, city = input().split()
            time = self._str_to_date(time)
            st.put(time, city)

        return st

    def cancel(self, time):
        '''cancels a certain flight'''
        time = self._str_to_date(time)
        self._st.delete(time)

    
    def _add_sec(self, time, seconds):
        '''a helper function for delay()'''
        delta = datetime.timedelta(seconds=seconds)
        new_time = time + delta 

        return new_time

    def delay(self, time, d):
        '''delays a certain flight'''
        #canceling the original flight (keeping the destination)
        prev_time = self._str_to_date(time)
        dest = self._st.get(prev_time)
        self.cancel(time)

        updated_time = self._add_sec(prev_time, int(d))

        #delaying the flight by adding a new flight with updated time
        self._st.put(updated_time, dest)


    def reroute(self, time, city):
        '''reroutes a flight to a new destination'''
        time = self._str_to_date(time)
        self._st.put(time, city)

    def dest(self, time):
        '''returns the destination of a given flight'''
        time = self._str_to_date(time)
        dest = self._st.get(time)
        if dest is not None:
            return dest
        return '-'

    def next(self, time):
        '''returns the next flight after a given time'''
        time = self._str_to_date(time)

        #get the next departure using _st.ceiling()
        next_departure = self._st.ceiling(time)
        destination = self._st.get(next_departure)

        date = f'{self._date_to_time(next_departure)} {destination}'
        return date

    def count(self, t1, t2):
        '''returns the number of flights between two times'''
        t1 = self._str_to_date(t1)
        t2 = self._str_to_date(t2)

        #count the number of flights between t1 and t2 using _st.size_range()
        count = self._st.size_range(t1, t2)
        return count


n, m = map(int, input().split())

flights = Flights(n)

for _ in range(m):
    inpt = input().split()

    if inpt[0] == 'cancel':
        time = inpt[1]
        flights.cancel(time)
    elif inpt[0] == 'delay':
        _, time, city = inpt
        flights.delay(time, city)
    elif inpt[0] == 'reroute':
        _, time, city = inpt
        flights.reroute(time, city)
    elif inpt[0] == 'destination':
        time = inpt[1]
        print(flights.dest(time))
    elif inpt[0] == 'next':
        time = inpt[1]
        print(flights.next(time))
    elif inpt[0] == 'count':
        _, t1, t2 = inpt
        print(flights.count(t1, t2))

