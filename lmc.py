import sys

class CPU():

	def __init__(self):
		self.memory = []
		self.accumulator = 0
		self.counter = 0
		self.op = ''

	def reset(self):
		self.memory = []
		self.accumulator = 0
		self.counter = 0

		for x in range(100):
			self.memory.append('000')

	def run(self):
		while self.counter < 100:
			instruction = self.memory[self.counter]
			if instruction == '901':
				self.op = '901'
			elif instruction == '902':
				self.op = '902'
			elif instruction == '000':
				self.op = '000'
			else:
				self.op = instruction[0]
				arg = int(instruction[1] + instruction[2])

			self.counter += 1

			if self.op == '1':
				self.add(arg)
			elif self.op == '2':
				self.subtract(arg)
			elif self.op == '3':
				self.store(arg)
			elif self.op == '5':
				self.load(arg)
			elif self.op == '6':
				self.branch(arg)
			elif self.op == '7':
				self.branchIfZero(arg)
			elif self.op == '8':
				self.branchIfPositive(arg)
			elif self.op == '901':
				self.input()
			elif self.op == '902':
				self.output()
			elif self.op == '000':
				self.halt()

	def add(self, arg):
		self.accumulator = self.accumulator + self.memory[arg]

	def subtract(self, arg):
		self.accumulator = self.accumulator - self.memory[arg]

	def store(self, arg):
		self.memory[arg] = self.accumulator

	def load(self, arg):
		self.accumulator = self.memory[arg]

	def branch(self, arg):
		self.counter = arg

	def branchIfZero(self, arg):
		if self.accumulator == 0:
			self.counter = arg

	def branchIfPositive(self, arg):
		if self.accumulator > 0:
			self.counter = arg

	def input(self):
		self.accumulator = int(input())

	def output(self):
		print(self.accumulator)

	def halt(self):
		sys.exit()

cpu = CPU()

cpu.reset()
cpu.memory = ['901','308','901','309','508','109','902','000','000','000','000','000','000','000','000','000','000','000','000','000','000','000','000', ]
cpu.run()
