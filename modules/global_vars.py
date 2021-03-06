LOAN_STATUS_FLAG = ['Fully Paid', 'Default']
LOAN_STATUS_PCT = ['Fully Paid %', 'Default %']
LOAN_STATUS = [['Fully Paid'],                           # fully paid
               ['Default', 'Charged Off']]               # default

dict_loan_flag = {LOAN_STATUS_FLAG[0]: LOAN_STATUS[0],   # fully paid
                  LOAN_STATUS_FLAG[1]: LOAN_STATUS[1]}   # default

STATUS_FLAG_COLORS = { 
                      LOAN_STATUS_FLAG[0]: 'green',      # good
                      LOAN_STATUS_FLAG[1]: 'red'}        # default

VARS_DESC = {'loan_amnt': 'Loan Amount', 'loan_status_flag': 'Loan Status Flag', 
             'hardship_flag': 'Hardship Flag', 'application_type': 'Application Type',
             'debt_settlement_flag': 'Debt Settlement Flag', 'term': 'Loan Term',
             'pymnt_plan': 'Payment Plan', 
             'emp_length': 'Employment Length', 'title':'Loan Purpose Desc',
             'grade': 'Grade', 
             'home_ownership': 'Home Ownership',
             'int_rate': 'Interest Rate', 'dti': 'Debt Ratio',
             'yrs_since_earliest_cr_line': 'Years since Earliest Credit Line', 
             'installment': 'Installment', 'total_pymnt': 'Total Payment', 
             'total_acc': 'Total Credit Lines', 'total_bal_il': 'Total Installment Acct Balance',
             'out_prncp': 'Remaining Outstanding Principal', 'revol_util': 'revol_util'
             }