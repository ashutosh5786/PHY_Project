import math
import os
import matplotlib.pyplot as plt

print("~~~~~~~~WE ARE GOING TO STUDY THE RESPONSE FOR LCR CIRCUIT~~~~~~~~~~\n")
print("Enter The Following Values\n")
resistance = float(input("Enter The Value oF Resistance: (Ohm)\n"))
inductor = float(input("Enter The Value oF Inductor:(H)\n"))
capacitance = float(input("Enter The Value oF Capacitance:(F)\n"))
serpar = input("Enter The Type Of Circuit:\n1> Type 1:Series Circuit\n2> Type 2:Parallel Circuit\n")
if serpar == "1":

        print("You Are Going For Series LCR Circuit:\n")
        resonatingfreq = (1 / 2 * 3.14 * math.sqrt(capacitance * inductor))
        print("Frequency is:", resonatingfreq)
        inductivereactance = (2*3.14*resonatingfreq*inductor)
        print("Inductive Reaction is: ", inductivereactance)
        capacitivereactance = (2*3.14*resonatingfreq*capacitance)
        print("Capacitive Reaction is: ", capacitivereactance)
        bandwidth=(resistance/inductor)
        print("Bandwidth is:", bandwidth)
        qualityfactor = (1/resistance)*(math.sqrt(inductor/resistance))
        print("Quality Factor is:", qualityfactor)
        if inductivereactance == capacitivereactance:
                print("Yes It's a Resonating Frq with Value:", resonatingfreq)
        else:
                print("Not Resonating Frequency, value is:", resonatingfreq)
        x = [1000, 2000, 3000, 4000, 4200, 4400, 4600, 4800, 5000, 6000, 7000]
        y = [5.5, 11, 16.5, 17.5, 17, 16.5, 16, 15.5, 15, 13, 10.5]
        plt.plot(x, y)
        plt.xlabel(" X - axis (Frequency)")
        plt.ylabel("Y - axis (Current)")
        plt.title("Graph for 25ohm Resistor")
        plt.show()
if serpar == "2":
        print("You Are Going For Parallel LCR Circuit:\n")
        resonatingfreq = (1 / 2 * 3.14 * math.sqrt(capacitance * inductor))
        print("Frequency is:", resonatingfreq)
        bandwidth = (resistance / inductor)
        print("Bandwidth is:", bandwidth)
        qualityfactor = (2*3.14*resonatingfreq)*(resistance*capacitance)
        print("Quality Factor is:", qualityfactor)
        capacitivereactance = (2 * 3.14 * resonatingfreq * capacitance)
        print("Capacitive Reaction is: ", capacitivereactance)
        inductivereactance = (2 * 3.14 * resonatingfreq * inductor)
        print("Inductive Reaction is: ", inductivereactance)
        if inductivereactance == capacitivereactance:
                print("Yes It's a Resonating Frq with Value:", resonatingfreq)
        else:
                print("Not Resonating Frequency, value is:", resonatingfreq)
        x = [1000, 2000, 3000, 4000, 4200, 4400, 4600, 4800, 5000, 6000, 7000]
        y = [17, 12, 5, 3, 4, 5, 6, 6.5, 7.5, 10, 12.5]
        plt.plot(x, y)
        plt.xlabel(" X - axis (Frequency)")
        plt.ylabel("Y - axis (Current)")
        plt.title("Graph for 25ohm Resistor")
        plt.show()
