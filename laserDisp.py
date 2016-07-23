def main():
	print("Welcome to the Laser Displacment Simulator")
	filename = raw_input("Please input the file name:") + ".txt"
	print("The name of your file shall be %s." % (filename))
	with open(filename, "w") as file:
		file.write("This is a test.")
	testDuration = raw_input("Please enter the test duration in hours.")
	stepSize = raw_input("Please enter the step size in seconds.")
	dataPoints = int(testDuration)*60*60 / int(stepSize)
	print("Your test shall last %s hours with a step size of %s seconds, giving a total of %s data points." % (testDuration, stepSize, dataPoints))


if __name__ == "__main__": main()