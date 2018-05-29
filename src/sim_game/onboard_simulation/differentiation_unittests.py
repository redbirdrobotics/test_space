import unittest
from differentiation_impl import Differentiate_Roombas
from math import sqrt


ROOMBA_SPEED_M = 0.333333

# class Roomba(object):
# 	def __init__(self, x, y):
# 		self.x = x
# 		self.y = y
# 		self.active = False

# class RoombaCorrelator(object):
# 	def __init__(self):
# 		self.roombas = []
# 		self.time_step = 0.

# 	def set_time(self, time_step):
# 		self.time_step = time_step

# 	def set_roombas(self, new_roombas):
# 		self.roombas = new_roombas

# 	def recognizes_old_roomba(self, roombas_to_test):
# 		for r in self.roombas:
# 			for roomba_to_test in roombas_to_test:
# 				dx = roomba_to_test.x - r.x
# 				dy = roomba_to_test.y - r.y
# 				distance_travelled_if_same = sqrt(dx**2 + dy**2)
# 				max_possible_distance_traveled = (ROOMBA_SPEED_M) * self.time_step
# 				if distance_travelled_if_same <= max_possible_distance_traveled:
# 					return True
#
#		return False




class DiffTests(unittest.TestCase):

	def aggregate_test(self):

		correlator = Differentiate_Roombas(None, None, None)

		initial_roombas = [
			Roomba(1., 1.), # should remain in
			Roomba(2., 2.), # should exit
			Roomba(3., 3.), # should exit
			]

		correlator.set_roombas(initial_roombas)

		# correlator.find_match_in_previous_message_impl()

		updated_roombas = [
			Roomba(),
			Roomba(),
			Roomba(),
			]

		correlator.set_roombas(updated_roombas)


	# def correlates_when_within_possible_range(self):
	# 	roombas = [Roomba(1., 1.)]
	# 	c = RoombaCorrelator()
	# 	c.set_roombas(roombas)
	# 	c.set_time(1.0)

	# 	# change it to within range
	# 	new_roomba = Roomba(1.32, 1.32)
	# 	new_roombas = [ new_roomba ]
	# 	c.set_time(2.0)

	# 	self.assertTrue(c.recognizes_old_roomba(new_roombas))

	# def does_not_correlate_when_outside_possible_range(self):
	# 	roombas = [Roomba(1., 1.)]
	# 	c = RoombaCorrelator()
	# 	c.set_roombas(roombas)
	# 	c.set_time(1.0)

	# 	# change it to within range
	# 	new_roomba = Roomba(1.34, 1.34)
	# 	new_roombas = [new_roomba]
	# 	c.set_time(2.0)

	# 	self.assertTrue(c.recognizes_old_roomba(new_roombas))


if __name__ == '__main__':
	unittest.main()
