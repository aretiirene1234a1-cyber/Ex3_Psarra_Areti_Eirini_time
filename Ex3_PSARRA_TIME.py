#Ex3 Time calculation

#Give minutes(input)
minutes_user=int(input("Give minutes"))
#Give seconds (input)
seconds_user=int(input("Give seconds"))


#Calculations
#Convert minutes to hours (integer division)
hours=minutes_user//60
#Modulo division
minutes=minutes_user % 60

#Convert seconds to hours (integer division)
hours_conv=seconds_user//3600
#Convert seconds to minutes (modulo division and integer)
minutes_con=(seconds_user%3600) // 60
seconds=seconds_user%60

#print the results
print(f"{minutes_user} minutes is: {hours:.0f} hours and {minutes} minutes")
print(f"{seconds_user} second is: {hours_conv:.0f} hours and {minutes_con} minutes and {seconds} seconds ")

##############################
#optional (float)
minutes_user_float=float(input("Give minutes (float)"))
hours_float=minutes_user_float//60
minutes_float=minutes_user_float % 60
print(f"{minutes_user_float} minutes is: {hours_float} hours and {minutes_float:.2f} minutes")