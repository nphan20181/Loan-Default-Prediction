LOAN_STATUS_FLAG = ['Fully Paid', 'Low Risk', 'Medium Risk', 'High Risk']
LOAN_STATUS = [['Fully Paid'],                                                    # good
               ['Current'],                                                       # current
               ['In Grace Period', 'Late (16-30 days)', 'Late (31-120 days)'],    # low risk
               ['Default', 'Charged Off']]                                        # high risk

dict_loan_flag = {LOAN_STATUS_FLAG[0]: LOAN_STATUS[0],   # good
                  LOAN_STATUS_FLAG[1]: LOAN_STATUS[1],   # current
                  LOAN_STATUS_FLAG[2]: LOAN_STATUS[2],   # low risk
                  LOAN_STATUS_FLAG[3]: LOAN_STATUS[3]}   # high risk

STATUS_FLAG_COLORS = { 
                      LOAN_STATUS_FLAG[0]: 'green',      # good
                      LOAN_STATUS_FLAG[1]: 'blue',       # current
                      LOAN_STATUS_FLAG[2]: 'orange',     # low risk
                      LOAN_STATUS_FLAG[3]: 'red'}        # high risk

VARS_DESC = {'loan_amnt': 'Loan Amount', 'loan_status_flag': 'Loan Status Flag', 
             'hardship_flag': 'Hardship Flag', 'application_type': 'Application Type',
             'debt_settlement_flag': 'Debt Settlement Flag', 'term': 'Loan Term',
             'pymnt_plan': 'Payment Plan', 'initial_list_status': 'Initial List Status',
             'emp_length': 'Employment Length', 'title':'Loan Purpose Desc',
             'grade': 'Grade', 'verification_status': 'Verification Status', 
             'home_ownership': 'Home Ownership',
             'int_rate': 'Interest Rate', 'dti': 'Debt Ratio',
             'yrs_since_earliest_cr_line': 'Years since Earliest Credit Line', 
             'installment': 'Installment', 'total_pymnt': 'Total Payment', 
             'total_rec_int': 'Interest Received to Date', 'loan_return': 'Loan Return', 
             'total_rec_prncp': 'Principal Received to Date',
             'total_acc': 'Total Credit Lines', 'total_bal_il': 'Total Installment Acct Balance',
             'out_prncp': 'Remaining Outstanding Principal'
             }