class Problem:
	def __init__(self):
		self.I = []
		self.Desired =[]
		self.Output = []
		self.E = []
		self.P = []
		self.K = 1
		self.iters =1
		
	def setup(self):
		self.iters = int(input("How many iterations do you want to do?"))
		self.K = float(input("What should your proportional constant be?"))
		for i in range(0,self.iters,1):
			print("On iteration "+str(i))
			self.I.append(float(input("What is the input from the system?")))
			self.Desired.append(float(input("What is the desired output?")))
			self.Output.append(float(input("What is the actual output?")))
		print("|I(t)\t|Desired|Output|e(t)\t|e(t-1)\t|Pd(t)\t|");
		for i in range(0,self.iters,1):
			print("|"+str(self.I[i])+"\t|"+str(self.Desired[i])+"\t|"+str(self.Output[i])+"\t|\t|"+(str(0) if i==0 else "")+"\t|\t|")
			#+str(self.E[i])+"\t|"
			#+str(self.E[i-1] if i>0 else 0)+"\t|"
			#+str(self.P[i])+"\t|")
		
	def solve(self):
		for i in range(0, self.iters,1):
			self.E.append(self.Output[i] - self.Desired[i])
			self.P.append(self.I[i] - (self.E[i]*self.K + (self.E[i] - self.E[i-1] if i >0 else 0)))
		print("|I(t)\t|Desired|Output|e(t)\t|e(t-1)\t|Pd(t)\t|");
		for i in range(0,self.iters,1):
			print("|"+str(self.I[i])+"\t|"+str(self.Desired[i])+"\t|"+str(self.Output[i])+"\t|"+str(self.E[i])+"\t|"+str(self.E[i-1] if i>0 else 0)+"\t|"+str(self.P[i])+"\t|")	
				
if __name__ == "__main__":
	x = Problem()
	x.setup()
	input("Press any key to solve")
	x.solve()