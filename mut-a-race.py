'''
Create mapping between amino acids switch state and phenotype. There are three switches per protein and three proteins per organism.
As each switch is binary this means there are 8 possible states across all three. Each switch configuration should map to a number in the range [0, 1]. Figure out a way to map each number in this range (eg 0.25) to a the phenotype (eg the leg is the quarter longest it could be)
Grade each phenotype in each environment. Eg long legs best on grass, ok in water, worst in swamp
Create function to compute total "fitness" or % of that animals capacity in each environment
Create pygame main loop which:
	Animates the movement of the animals in place
	Updates each animals fitness status / % of potential capacity
	Controls the speed of the movement of the background which correlates to fitness status / % of potential capacity
	Cycles environment as each organism completes each one
	Counts down start
	Detects winning
	Have a victory sequence for the winner
	Restarts when all players have completed
	Connects to hardware switches
'''

