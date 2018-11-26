import sys

class CPU():

	def __init__(self):
		self.memory = []
		self.accumulator = 0
		self.counter = 0

	def reset(self):
		self.memory = []
		self.accumulator = 0
		self.counter = 0

		for x in range(100):
			self.memory.append(0)

	def add(self, arg):
		self.accumulator = self.accumulator + arg

	def subtract(self, arg):
		self.accumulator = self.accumulator - arg

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
		self.accumulator = input()	

	def output(self):
		print(self.accumulator)

	def halt(self):
		sys.exit()							

cpu = CPU()

cpu.reset()
cpu.reset()
print(len(cpu.memory))