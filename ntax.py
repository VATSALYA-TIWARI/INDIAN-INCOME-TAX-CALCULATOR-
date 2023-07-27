import tkinter as tk
from tkinter import *  
from tkinter import ttk
from random import randint,choice
def calculate_tax():
    age = int(age_entry.get())
    Bsalary = int(Bsalary_entry.get())
    DA = int(DA_entry.get())
    HRA = int(HRA_entry.get())
    Lta = int(Lta_entry.get())
    OLL = int(OLL_entry.get())
    HrA= HRA/12
    A87=0
    Income = (Bsalary + DA + HRA + Lta + OLL)
    Income_label["text"] = f"YOUR TOTAL YEARLY INCOME IS: {Income}"

    # Get input for applicable waivers
    A80C = int(A80C_entry.get())
    if A80C > 150000:
        A80C = 150000
    A80CCD= int(A80CCD_entry.get())
    HIP= int(HIP_entry.get()) # 25k for 60 below 50k for upper
    if HIP > 25000:
        HIP = 25000
    H1checkup=int(H1checkup_entry.get()) # 5k reduction
    if H1checkup > 5000:
        H1checkup=5000
    A80DD= int(A80DD_entry.get()) # ONLY APPLICABLE FOR DISABLED 40 TO 80 PERCENT 75K MORE THAN 80, 125K
    if A80DD>=40 and A80DD<=80:
        A80DD= 75000
    elif A80DD>80:
        A80DD= 125000
    nm= int(nm_entry.get())
    mr= int(mr_entry.get())
    nr= int(mr*nm)
    if (HrA<=(Bsalary+DA)*0.5/12 and (HrA)<=(mr-(Bsalary*0.1/12))):
     HRa= nm*HrA
    elif(((Bsalary+DA)*0.5/12)<=HrA and (Bsalary+DA)*0.5/12 <= (mr-(Bsalary*0.1/12))):
     HRa= ((Bsalary+DA)*0.5/12)*nm
    else:
     HRa= (mr-(Bsalary*0.1/12))*nm
    S80E= int(S80E_entry.get()) #ENTIRE INTEREST AMOUNT CAN BE TAKEN AS TAX DEDUCTION.
    S80c= int(S80c_entry.get()) # 150K DEDUCTION UNDER THIS SECTION
    if S80c>150000:
        S80c=150000
    S24= int(S24_entry.get())# 200K DEDUCTION
    if S24>200000:
     S24=200000
    S80G= int(S80G_entry.get())# entire amount can be claimed excpet in hand cash exceeding 2000.
    S80GGC= int(S80GGC_entry.get()) #50 to 100 percent waiver alolowed.
    S80GG= int(nm*mr) # 25 percent of salary or 60k can be reduced whichever is lower
    if S80GG>60000:
        S80GG=60000
    #A80DDB IS NOT TAKEN UNDER THE CONSIDERATION.
    S80CCH= int(S80CCH_entry.get())
    S80EEB=int(S80EEB_entry.get())
    LTA= int(LTA_entry.get())#FOR SALARIED PEOPLE
    BOOKS= int(BOOKS_entry.get())
    RELALL= int(RELALL_entry.get())
    CHAL= int(CHAL_entry.get())
    if Income<500000:
        A87=int(12500)
    if HRa==0:
        HRa=S80GG
#section 80TTB IS NOT TAKEN UNDER CONSIDERATION.
# ALLOWANCES:
    SD=int(50000)

    # ... Add input validations and calculations for other waivers ...

   #NEW TAX REGIME FORMULA
    Nincome = Income - RELALL - SD  - S80CCH
    if Nincome<= 700000:
     ntax= 0
    else:
        if Nincome <= 300000:  #3 lakh
            ntax = 0
        elif Nincome <= 600000: #6 Lakh
            ntax = (Nincome - 300000) * 0.05 
        elif Nincome <= 900000: # 9 lakh 
            ntax = (Nincome - 600000) * 0.10 + 15000 
        elif Nincome <= 1200000: #12 Lakh
            ntax = (Nincome - 900000) * 0.15 + 45000 
        elif Nincome <= 1500000: #15 lakh 
            ntax = (Nincome - 1200000) * 0.20 + 90000 
        elif Nincome <= 5000000:
            ntax = ((Nincome - 1500000) * 0.20+ 150000)*1.1
        elif Nincome <= 10000000:
            ntax = ((Nincome - 1500000) * 0.20 + 850000)*1.2
        else:
            ntax=((Nincome-10000000)*0.20+1850000)*1.25
    fntax=(ntax*1.04)
    # Display the calculated tax
    fntax_label["text"] = f"YOUR TOTAL YEARLY TAX ACCORDING TO NEW TAX REGIME IS: {fntax}"
    #OLD TAX REGIME FORMULA
    oincome=int(Income-A80C-A80CCD-HIP-H1checkup-A80DD-S80E-S80c-S24-S80G-S80GGC-HRa-LTA-SD-BOOKS-RELALL-CHAL-A87-S80CCH-S80EEB)
    if oincome <=250000:
        otax=0
    elif oincome<=500000:
        otax= (oincome-250000)*0.05
    elif oincome<=1000000:
        otax= (oincome-500000)*0.20+12500
    elif oincome<=5000000:
        otax= ((oincome-1000000)*0.30+112500)
    elif oincome <= 10000000:
        otax = ((oincome - 5000000) * 0.30 + 112500+1200000)*1.10
    elif oincome<=20000000:
        otax=((oincome-10000000)*0.30+112500+1200000+1500000)*1.15
    elif oincome<=50000000:
        otax=((oincome-20000000)*0.30+112500+1200000+1500000+3000000)*1.25
    else:
        otax=((oincome-50000000)*0.30+112500+1200000+1500000+3000000+9000000)*1.37
    fotax=int(otax+otax*0.04)
    fotax_label["text"] = f"YOUR TOTAL YEARLY TAX ACCORDING TO OLD TAX REGIME IS: {fotax}"

    if fotax>fntax:
        print("YOU WILL PAY LESS TAX IN THE NEW TAX REGIME BY",fotax-fntax)
    elif fotax==fntax :
        print("YOU WILL PAY EQUAL TAX IN EITHER CASES")
    else:
        print("YOU WILL PAY LESS TAX IN THE OLD REGIME BY",fntax-fotax)
    print("\nHOWEVER YOU CAN REDUCE YOUR TAXABLE INCOME BY THE FOLLOWING WAYS :\n")
    # SUGGESTIONS FOR TAX SAVINGS
    if A80C<150000:
      print("YOU CAN REDUCE YOUR TAXABLE INCOME BY" ,150000-A80C, '''MORE BY INVESTING IN THE FOLLOWING :-
    1. Equity-Linked Saving Scheme (ELSS)    2. Sukanya Samriddhi Yojana (SSY)              3. Unit Linked Insurance Plan (ULIP)
    4. Employees Provident Fund (EPF)       5. Principal amount payment towards home loan  6. National Saving Certificate (NSC)
    7. 5-year, tax-saving                    8. FDLIC premium                               9. stamp duty and registration charges for purchase of property
    10.Senior Citizen Savings Scheme (SCSS)  11.Infrastructure bond                        12. Public Provident FUND(PPF)''')
    if A80CCD<50000: 
     print("YOU CAN REDUCE YOUR TAXABLE INCOME BY",50000-A80CCD,"BY INVESTING IN NATIONAL PENSION SCHEME")
    if HIP < 25000:
        print("YOU CAN REDUCE YOUR TAXABLE INCOME BY", 25000-HIP,"BY BUYING A HEALTH INSURANCE FOR YOU AND YOUR FAMILY")
    if S80c<150000:
     print("YOU CAN REDUCE YOUR TAXABLE INCOME BY",150000-S80c," ON THE PRINCIPAL BY PURCHASING A NEW HOUSE WITH A LOAN")
    if S24<200000:
     print("YOU CAN REDUCE YOUR TAXABLE INCOME BY",200000-S24,"ON THE INTEREST BY PURCASHING A NEW HOUSE WITH A LOAN")
print("YOU CAN REDUCE YOUR TAXABLE INCOME BY DONATING TO AGNIVEER CORP FUND,CHARITIES,RELIEF FUNDS AND VARIOUS NGO's")
print("THANK YOU FOR USING INDIAN TAX CALCULATOR , WE HOPE WE HELPED YOU IN YOUR CORPORATE JOURNEY")

# Create a Tkinter window

window = tk.Tk()
window.title("Indian Tax Calculator")
# Create and pack the welcome message label
welcome_label = tk.Label(window, text="WELCOME TO THE INDIAN TAX CALCULATOR\nWE HOPE TO PROVIDE YOU THE BEST SERVICE\nKINDLY GO THROUGH THE QUESTIONS AND BE RELAXED AS WE FIGURE OUT THE BEST OPTION FOR YOU\nIF IN CASE A CERTAIN AMOUNT IN DEDUCTION IS NOT APPLICABLE FOR YOU ENTER 0")
welcome_label.pack()

# Create labels and entry fields for inputs
age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

Bsalary_label = tk.Label(window, text="Basic Salary:")
Bsalary_label.pack()
Bsalary_entry = tk.Entry(window)
Bsalary_entry.pack()

DA_label = tk.Label(window, text="DA:")
DA_label.pack()
DA_entry = tk.Entry(window)
DA_entry.pack()

HRA_label = tk.Label(window, text="HRA:")
HRA_label.pack()
HRA_entry = tk.Entry(window)
HRA_entry.pack()

Lta_label = tk.Label(window, text="LTA:")
Lta_label.pack()
Lta_entry = tk.Entry(window)
Lta_entry.pack()

OLL_label = tk.Label(window, text="OTHER ALLOWENCES:")
OLL_label.pack()
OLL_entry = tk.Entry(window)
OLL_entry.pack()

A80C_label = tk.Label(window, text=''' \n                                                                       

1. Equity-Linked Saving Scheme (ELSS)    2. Sukanya Samriddhi Yojana (SSY)              3. Unit Linked Insurance Plan (ULIP)
4. Employees’ Provident Fund (EPF)       5. Principal amount payment towards home loan  6. National Saving Certificate (NSC)
7. 5-year, tax-saving                    8. FDLIC premium                               9. stamp duty and registration charges for purchase of property
10.Senior Citizen Savings Scheme (SCSS)  11.Infrastructure bond                        12. Public Provident Fund (PPF)
\n ENTER THE TOTAL AMOUNT INVESTED OUT OF THESE INVESTMENTS :''')
A80C_label.pack()
A80C_entry = tk.Entry(window)
A80C_entry.pack()

A80CCD_label = tk.Label(window, text= "ENTER YOUR NATIONAL PENSION SCHEME (NPS) CONTRIBUTION : ")
A80CCD_label.pack()
A80CCD_entry = tk.Entry(window)
A80CCD_entry.pack()

HIP_label = tk.Label(window, text= "ENTER THE TOTAL AMOUNT OF HEALTH INSURANCE PREMIUM PAID BY YOU FOR YOURSELF , PARENTS , SPOUSE AND CHILDREN : ")
HIP_label.pack()
HIP_entry = tk.Entry(window)
HIP_entry.pack()

H1checkup_label = tk.Label(window, text= "ENTER YOUR TOTAL HEALTH CHECKUP EXPENSES OF YOURSELF,SPOSE,PARENTS AND CHILDRENS : ")
H1checkup_label.pack()
H1checkup_entry = tk.Entry(window)
H1checkup_entry.pack()

A80DD_label = tk.Label(window, text= "IF YOU ARE DISABLED THEN ENTER THE PERCENTAGE OF YOUR DISABILITY OTHERWISE TYPE 0 : ")
A80DD_label.pack()
A80DD_entry = tk.Entry(window)
A80DD_entry.pack()

nm_label = tk.Label(window, text= " ENTER THE NUMBER OF MONTHS YOU HAVE PAID RENT:  ")
nm_label.pack()
nm_entry = tk.Entry(window)
nm_entry.pack()

mr_label = tk.Label(window, text= " ENTER YOUR MONTHLY RENT : ")
mr_label.pack()
mr_entry = tk.Entry(window)
mr_entry.pack()

S80E_label = tk.Label(window, text= " ENTER THE INTEREST AMOUNT IF YOU HAVE TAKEN AN EDUCATION LOAN : ")
S80E_label.pack()
S80E_entry = tk.Entry(window)
S80E_entry.pack()

S80c_label = tk.Label(window, text= " ENTER THE PRINCIPAL AMOUNT OF YOUR LOAN REPAYMENT OF THE HOUSE PURCHASED :  ")
S80c_label.pack()
S80c_entry = tk.Entry(window)
S80c_entry.pack()

S24_label = tk.Label(window, text= " ENTER THE INTEREST AMOUNT ON YOUR HOME LOAN IF YOU RESIDE IN THE RESIDENTIAL PROPERTY :  ")
S24_label.pack()
S24_entry = tk.Entry(window)
S24_entry.pack()

S80G_label = tk.Label(window, text= " ENTER THE AMOUNT YOU DONATED TO RELIEF FUND OR CHARITABLE ORGANIZATIONS :   ")
S80G_label.pack()
S80G_entry = tk.Entry(window)
S80G_entry.pack()

S80GGC_label = tk.Label(window, text= " ENTER THE AMOUNT DONATED TO A POLITICAL PARTY OR ELECTORAL FUND WHICH IS REGISTERED :   ")
S80GGC_label.pack()
S80GGC_entry = tk.Entry(window)
S80GGC_entry.pack()

S80CCH_label = tk.Label(window, text= " ENTER THE AMOUNT DONATED TOWARDS AGNIVEER CORPUS FUND :   ")
S80CCH_label.pack()
S80CCH_entry = tk.Entry(window)
S80CCH_entry.pack()

S80EEB_label = tk.Label(window, text= " IN CASE YOU HAVE PURCHASED AN ELECTRIC VEHICLE ENTER THE INTEREST AMOUNT ON THE LOAN :   ")
S80EEB_label.pack()
S80EEB_entry = tk.Entry(window)
S80EEB_entry.pack()

LTA_label = tk.Label(window, text= " ENTER THE AMOUNT SPENT OF TRAVELLING BY EITHER AIR , TRAIN AND PUBLIC TRANSPORT IN A DOMESTIC TRIP UNDER LEAVE TRAVEL ALLOWANCE :   ")
LTA_label.pack()
LTA_entry = tk.Entry(window)
LTA_entry.pack()

BOOKS_label = tk.Label(window, text= "ENTER THE EXPENSES INCURRED ON PERIODICLES,BOOKS,JOURNALS,NEWSPAPERS :    ")
BOOKS_label.pack()
BOOKS_entry = tk.Entry(window)
BOOKS_entry.pack()

RELALL_label = tk.Label(window, text= " ENTER THE RELOCATION ALLOWANCE PROVIDED BY YOUR EMPLOYER :   ")
RELALL_label.pack()
RELALL_entry = tk.Entry(window)
RELALL_entry.pack()

CHAL_label = tk.Label(window, text= ''' The allowance given by the employer to the employee for their child’s education is tax-exempt. 
                    A maximum of Rs. 100/month can be claimed by an employee as an exemption. 
                    This comes up to Rs. 1,200/year. This exemption is valid for a maximum of two children. 
                    ENTER THE CHILDREN ALLOWANCE PROVIDED BY YOUR COMPANY : ''')
CHAL_label.pack()
CHAL_entry = tk.Entry(window)
CHAL_entry.pack()
# ... Add labels and entry fields for other inputs ...

# Create a button to calculate tax
calculate_button = tk.Button(window, text="Calculate Taxes", command=calculate_tax)
calculate_button.pack()

# Create a label to display the income and tax

Income_label = tk.Label(window, text="YOUR TOTAL YEARLY INCOME IS : ")
Income_label.pack()

fntax_label = tk.Label(window, text="YOUR TOTAL YEARLY TAX ACCORDING TO NEW TAX REGIME IS: ")
fntax_label.pack()

fotax_label = tk.Label(window, text= "YOUR TOTAL YEARLY TAX ACCORDING TO OLD TAX REGIME IS")
fotax_label.pack()

# Run the Tkinter event loop
window.mainloop()