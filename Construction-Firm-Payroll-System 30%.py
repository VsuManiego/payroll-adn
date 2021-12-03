from tkinter import *
import random
import time
import datetime
from tkinter import messagebox

payroll = Tk()
payroll.geometry("1350x650")
payroll.resizable(0, 0)
payroll.title("Construction Firm Payroll Systems")

def exit():
    payroll.destroy()

def reset():
    EmployeeName.set("")
    Address.set("")
    Reference.set("")
    EmployerName.set("")
    City.set("")
    Basic.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    Pension.set("")
    StudenLoan.set("")
    NIPayment.set("")
    Deducations.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtherPaymentDue.set("")

def PayRef():
    PayDate.set(time.strftime("%d/%m/%Y"))
    refPay = random.randint(20000, 709467)
    refPaid = ("PR" + str(refPay))
    Reference.set(refPaid)

    NIPay = random.randint(20000, 559467)
    NIPaid = ("NI" + str(NIPay))
    NINumber.set(NIPaid)

def PayPeriod():
    i = datetime.datetime.now()
    TaxPeriod.set(i.month)

    NCode = random.randint(1200, 3467)
    CodeNI = ("NICode" + str(NCode))
    NICode.set(CodeNI)

def MonthlySalary():
    if Basic.get() == "":
        BS = 0
    else:
        try:
            BS = float(Basic.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
            Basic.set("")

    if City.get() == "":
        CW = 0
    else:
        try:
            CW = float(City.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
            City.set("")

    if OverTime.get() == "":
        OT = 0
    else:
        try:
            OT = float(OverTime.get())
        except ValueError:
            messagebox.showinfo("Error", "Wrong values!!! Use numbers.")
            OverTime.set("")





    MTax = ((BS + CW + OT) * 0.3)
    TTax = "pln", str('%.2f' % ((MTax)))
    Tax.set(TTax)

    M_StudenLoan = ((BS + CW + OT) * 0.02)
    MM_StudenLoan = "pln", str('%.2f' % ((M_StudenLoan)))
    StudenLoan.set(MM_StudenLoan)

    M_Pension = ((BS + CW + OT) * 0.012)
    MM_Pension = "pln", str('%.2f' % ((M_Pension)))
    Pension.set(MM_Pension)

    M_NIPayment = ((BS + CW + OT) * 0.021)
    MM_NIPayment = "pln", str('%.2f' % ((M_NIPayment)))
    NIPayment.set(MM_NIPayment)

    Deduct = MTax + M_Pension + M_StudenLoan + M_NIPayment
    Deducat_Payment =  "pln", str('%.2f' % ((Deduct)))
    Deducations.set(Deducat_Payment)

    NetPayAfter = ((BS + CW + OT) - Deduct)
    NetAfter = "pln", str('%.2f' % ((NetPayAfter)))
    NetPay.set(NetAfter)

    Gross_Pay = "pln", str('%.2f' % (BS + CW + OT))
    GrossPay.set(Gross_Pay)

    TaxablePay.set(TTax)
    PensionablePay.set(MM_Pension)
    OtherPaymentDue.set("0.00")

EmployeeName = StringVar()
Address = StringVar()
Reference = StringVar()
EmployerName = StringVar()
City = StringVar()
Basic = StringVar()
OverTime = StringVar()
GrossPay = StringVar()
NetPay = StringVar()
Tax = StringVar()
PostCode = StringVar()
Gender = StringVar()
PayDate = StringVar()
Pension = StringVar()
StudenLoan = StringVar()
NIPayment = StringVar()
Deducations = StringVar()
TaxPeriod = StringVar()
NINumber = StringVar()
NICode = StringVar()
TaxablePay = StringVar()
PensionablePay = StringVar()
OtherPaymentDue = StringVar()
