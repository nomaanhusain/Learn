# Cowin Slot Finder

## Instructions to use

In cmd, run `pip install requests`

Copy all the content of `cowin.py`  and paste them in a `.py` file and execute.

Suppose you state is `Uttar Pradesh`, ensure that `U` and `P` are capital.
Enter proper District name as shown on cowin portal.
Enter date in the proper **_DD-MM-YYYY_** format otherwise the code might run but results wont be proper.
**MAKE SURE THE DATE FORMAT IS CORRECT**


## Changing Parameters
**The code is set by default for 18+ people and for Dose 1 slots of *COVAXIN*.**
To change these parameters, get to Line **86** of `cowin.py`.

Inside `if`, it should look like this:
`i['available_capacity_dose1']>0 and i['min_age_limit']==18 and i['vaccine']=='COVAXIN'`.

### Change to Dose 2
To change to Dose 2, change `available_capacity_dose1` to `available_capacity_dose2`, it should look like this:
`i['available_capacity_dose2']>0 and i['min_age_limit']==18 and i['vaccine']=='COVAXIN'`.
Also at line **90** change `available_capacity_dose1` to `available_capacity_dose2`, it should look like 
`doseCount=doseCount+i['available_capacity_dose2']`

### Switch to 45+
To change to 45+ replace `18` with `45`, it should look like this:
`i['available_capacity_dose2']>0 and i['min_age_limit']==45 and i['vaccine']=='COVAXIN'`.

### To remove age restriction
Or if you want to remove age restriction entirely, remove the condition, it should look like this:
`i['available_capacity_dose1']>0 and i['vaccine']=='COVAXIN'`.

### To switch vaccine
If you want to change to `COVISHIELD`, replace `COVAXIN` with `COVISHIELD`, it should look like this:
`i['available_capacity_dose1']>0 and i['min_age_limit']==18 and i['vaccine']=='COVISHIELD'`.
### To remove vaccine restriction
If you want to remove vaccine restriction, it should look like this: 
`i['available_capacity_dose1']>0 and i['min_age_limit']==18`.

Combinations of these conditions can be used to get desired result accordingly.
