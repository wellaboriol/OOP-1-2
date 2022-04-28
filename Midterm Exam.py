def main():
    class TemperatureConversion:
        def __init__(self,temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9)/5 + 32
        def Fahrenheit_to_Celsius(self):
            return(self.conversion()-32) * 5/9

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return (self._temp + 273.15)
        def Kelvin_to_Celsius(self):
            return(self.conversion()-273.15)

    tempInCelsius = float(input("Enter the temperature in Celsius:"))
    cvt1 = CelsiusToKelvin(tempInCelsius)
    print(str(cvt1.conversion()) +" "+ "Kelvin")
    cvt2 = CelsiusToFahrenheit(tempInCelsius)
    print(str(cvt2.conversion()) +" "+ "Fahrenheit")

    print(f"{cvt1.conversion()}={cvt1.Kelvin_to_Celsius()} Celsius")
    print(f"{cvt2.conversion()}={cvt2.Fahrenheit_to_Celsius()} Celsius")

main()

from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")

#Insert Button Widget
btn=Button(window, text="Click to Change Color", bg="White", activebackground="Yellow")
btn.place(relx=.5, y=200, anchor="center")
window.mainloop()