# Day Discount Free Delivery Purchase
data ="""
Weekday	Yes	Yes	Yes
Weekday	Yes	Yes	Yes
Weekday	No	No	No
Holiday	Yes	Yes	Yes
Weekend	Yes	Yes	Yes
Holiday	No	No	No
Weekend	Yes	No	Yes
Weekday	Yes	Yes	Yes
Weekend	Yes	Yes	Yes
Holiday	Yes	Yes	Yes
Holiday	No	Yes	Yes
Holiday	No	No	No
Weekend	Yes	Yes	Yes
Holiday	Yes	Yes	Yes
Holiday	Yes	Yes	Yes
Weekday	Yes	Yes	Yes
Holiday	No	Yes	Yes
Weekday	Yes	No	Yes
Weekend	No	No	Yes
Weekend	No	Yes	Yes
Weekday	Yes	Yes	Yes
Weekend	Yes	Yes	No
Holiday	No	Yes	Yes
Weekday	Yes	Yes	Yes
Holiday	No	No	No
Weekday	No	Yes	No
Weekday	Yes	Yes	Yes
Weekday	Yes	Yes	Yes
Holiday	Yes	Yes	Yes
Weekend	Yes	Yes	Yes
"""

lines = data.strip().split('\n')

sum_samples = len(lines)
sum_weekday, sum_weekend, sum_holidays = 0, 0, 0
sum_disc, sum_nodisc, sum_deliv, sum_nodeliv, sum_purchase, sum_not_purchase = 0, 0, 0, 0, 0, 0

# for  P(X|Purchase)
px2_weekday, px2_weekend, px2_holidays = 0,0,0
px2_disc, px2_nodisc, px2_deliv, px2_nodeliv = 0,0,0,0

npx2_weekday, npx2_weekend, npx2_holidays = 0,0,0
npx2_disc, npx2_nodisc, npx2_deliv, npx2_nodeliv = 0,0,0,0

for line in lines:
    day, disc, delivery, purchase = line.split()
    if day =="Weekday":
        sum_weekday +=1
        if purchase == "Yes":
            px2_weekday +=1
        elif (purchase == "No"):
            npx2_weekday +=1
    elif day == "Weekend":
        sum_weekend +=1
        if purchase == "Yes":
            px2_weekend +=1
        elif (purchase == "No"):
            npx2_weekend +=1
    elif day == "Holiday":
        sum_holidays +=1
        if purchase == "Yes":
            px2_holidays +=1
        elif (purchase == "No"):
            npx2_holidays +=1

    if disc == "Yes":
        sum_disc +=1
        if purchase == "Yes":
            px2_disc +=1
        elif (purchase == "No"):
            npx2_disc +=1
    elif disc == "No":
        sum_nodisc +=1
        if purchase == "Yes":
            px2_nodisc +=1
        elif (purchase == "No"):
            npx2_nodisc +=1

    if delivery == "Yes":
        sum_deliv +=1
        if purchase == "Yes":
            px2_deliv +=1
        elif (purchase == "No"):
            npx2_deliv +=1
    elif delivery == "No":
        sum_nodeliv +=1
        if purchase == "Yes":
            px2_nodeliv +=1
        elif (purchase == "No"):
            npx2_nodeliv +=1

    if purchase == 'Yes':
        sum_purchase += 1
    elif purchase == "No":
        sum_not_purchase += 1

# check whether measurement alrd correct or not
# print(npx2_nodisc)
# print(npx2_disc)
# print(px2_disc)
# print(px2_nodisc)


# weekday no yes (purchase & not purchase)
# calculate P(purchase), P(notpurchase))
# prior probability #####################
p_purchase = sum_purchase/sum_samples
p_nopurchase = sum_not_purchase/sum_samples
# calculate (P(X))
# days
p_weekday = sum_weekday/sum_samples
p_weekend = sum_weekend/sum_samples
p_holidays =sum_holidays/sum_samples
# disc
p_disc = sum_disc/sum_samples
p_nodisc = sum_nodisc/sum_samples
# deliv
p_deliv =sum_deliv/sum_samples
p_nodeliv=sum_nodeliv/sum_samples

# print(p_purchase)

# calculate conditional probabilities
# P(Weekday | Purchase) 
# P(Weekday | Not purchase) 
# P(No Discount | Purchase) 
# P(No Discount | Not purchase)
# P(Yes Delivery | Purchase) 
# P(Yes Delivery | Not purchase)

def calculate_conditional(x,y):
    return x/y

# marginal probability P(X|purchase) & (P(X|notpurchase)) #####################
# days
weekday_p = calculate_conditional(sum_weekday,sum_purchase)
weekday_np = calculate_conditional(sum_weekday,sum_not_purchase)
weekend_p = calculate_conditional(sum_weekend,sum_purchase)
weekend_np = calculate_conditional(sum_weekend,sum_not_purchase)
holiday_p = calculate_conditional(sum_holidays,sum_purchase)
holiday_np = calculate_conditional(sum_holidays,sum_not_purchase)

# discount
discount_p = calculate_conditional(sum_disc,sum_purchase)
discount_np = calculate_conditional(sum_disc,sum_not_purchase)
nodiscount_p = calculate_conditional(sum_nodisc,sum_purchase)
nodiscount_np = calculate_conditional(sum_nodisc,sum_not_purchase)

# delivery
delivery_p = calculate_conditional(sum_deliv,sum_purchase)
delivery_np = calculate_conditional(sum_deliv,sum_not_purchase)
nodelivery_p = calculate_conditional(sum_nodeliv,sum_purchase)
nodelivery_np =calculate_conditional(sum_nodeliv,sum_not_purchase)


# weekday no yes (purchase & not purchase)
def calculation(a,b,c):
    if a.lower() == "weekday":
    # hitung P(X)
        a1 = p_weekday
        # probability purchase if weekday (a2)
        a2 = px2_weekday
        a3 = npx2_weekday
    elif a.lower() == "weekend":
        a1 = p_weekend
        a2 = px2_weekend
        a3 = npx2_weekend
    elif a.lower() == "holiday":
        a1 = p_holidays
        a2 = px2_holidays
        a3 = npx2_holidays

    if b.lower() == "yes":
        b1 = p_disc
        b2 = px2_disc
        b3 = npx2_disc
    elif b.lower() == "no":
        b1 = p_nodisc
        b2 = px2_nodisc
        b3 = npx2_nodisc

    if c.lower() == "yes":
        c1 = p_deliv
        c2 = px2_deliv
        c3 = npx2_deliv
    elif c.lower() == "no":
        c1 = p_nodeliv
        c2 = px2_nodeliv
        c3 = npx2_nodeliv


    # if d.lower() == "yes":
    #     d = p_purchase
    # elif d.lower() == "no":
    #     d = p_nopurchase
    d_purchase  = p_purchase
    # print(p_purchase)
    d_nopurchase = p_nopurchase
    # print(p_nopurchase)

    
    # P(Purchase) & P(NOTPURCHASE) 
    # marginal probability P(X) ###
    px = a1 * b1 *c1

    # P(X|Purchase)  
    # conditional probability ###
    # i.e, (purchase, weekday) (purchase, no delivery), (purchase, no disc)
    px2_purchase = a2/sum_purchase*b2/sum_purchase*c2/sum_purchase
    # P(X|notPurchase)
    px2_nopurchase =  a3/sum_not_purchase*b3/sum_not_purchase*c3/sum_not_purchase

    # BY BAYES' RULE:
    # P(Purchase | Day=Weekday, Discount=No, Delivery=Yes)
    # formula = P(Purchase|B) = P(B|Purchase) * P(Purchase) / P(B)
    bayes_purchase = px2_purchase * d_purchase / px
    bayes_nopurchase = px2_nopurchase * d_nopurchase / px
    print("For the input: ",a,",",b,"(discount)",",",c, "(free delivery).")
    print("The probability of purchasing: ", bayes_purchase)
    print("The probability of not purchasing: ", bayes_nopurchase)

# P(Purchase | Day=Weekday, Discount=No, Delivery=Yes)
# formula = P(Purchase|B) = P(B|Purchase) * P(Purchase) / P(B)
# p_probability = calculation("weekday","no","yes")
print("\n")
print("\t William Jonathan Mulyadi (2502045683)")
print("\t\t Naive-Bayes assignment\n")
while True:
    print("Please choose between 1, 2, and 3")
    print("1. (Default assignment) Weekday, No Discount, Yes Delivery")
    print("2. Manual input!")
    print("3. To exit")
    z = int(input("Enter 1/2/3: "))
    if z ==1:
        print("\n")
        calculation("weekday","no","yes")
        print("\n")
    elif z ==2:
        print("Please input between these!")
        print("First input: weekday / weekend / holiday")
        print("Second input (discount): yes / no ")
        print("Third input (delivery): yes / no")

        # Get user inputs
        a = input("First input: ").lower()
        b = input("Second input: ").lower()
        c = input("Third input: ").lower()

        while a not in ['weekday', 'weekend', 'holiday'] or b not in ['yes', 'no'] or c not in ['yes', 'no']:
            print("Invalid input(s). Please re-enter the incorrect input(s).")
            if a not in ['weekday', 'weekend', 'holiday']:
                a = input("First input: ").lower()
            if b not in ['yes', 'no']:
                b = input("Second input: ").lower()
            if c not in ['yes', 'no']:
                c = input("Third input: ").lower()
        print("\n")
        calculation(a,b,c)
        print("\n")
    elif z == 3:
        break
    else: 
        continue



