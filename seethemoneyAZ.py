# %%
import requests
import json
import pandas as pd
import numpy as np

def convert_unix_date(date_str):
    unix_time = ''.join([i for i in date_str if i.isdigit()])
    return pd.to_datetime(unix_time, unit='ms')
    

class seethemoneyAZ:
    """
    Initializes a seethemoneyAZ object initialized with a particular set of cookies
    """
    def __init__(self, cookie, userid) -> None:
        self.cookies = {
            '__cf_bm': cookie,
            'SeeTheMoneyUserHistory': f'UserID={userid}&URLHash=JurisdictionId=0|Page=80|startYear=2000|endYear=2022|IsLessActive=false|ShowOfficeHolder=false|View=Detail|Name=7~1272383|entityId=1272383|TablePage=1|TableLength=2',
        }
        self.headers = {
            'authority': 'seethemoney.az.gov',
            'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://seethemoney.az.gov',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://seethemoney.az.gov/Reporting/Explore',
            'accept-language': 'en-US,en;q=0.9',
        }

    
    def campaign_list(self, name, max_records):
        params = [
            ('Page', '1'),
            ('startYear', '2002'),
            ('endYear', '2022'),
            ('JurisdictionId', '0'),
            ('TablePage', '1'),
            ('TableLength', '10'),
            ('IsLessActive', 'false'),
            ('ShowOfficeHolder', 'false'),
            ('ChartName', '1'),
            ('IsLessActive', 'false'),
            ('ShowOfficeHolder', 'false'),
        ]
        data = {
            'draw': '999',
            # 'columns[0][data]': 'EntityLastName',
            # 'columns[0][name]': '',
            # 'columns[0][searchable]': 'true',
            # 'columns[0][orderable]': 'true',
            # 'columns[0][search][value]': '',
            # 'columns[0][search][regex]': 'false',
            # 'columns[1][data]': 'CommitteeName',
            # 'columns[1][name]': '',
            # 'columns[1][searchable]': 'true',
            # 'columns[1][orderable]': 'true',
            # 'columns[1][search][value]': '',
            # 'columns[1][search][regex]': 'false',
            # 'columns[2][data]': 'OfficeName',
            # 'columns[2][name]': '',
            # 'columns[2][searchable]': 'true',
            # 'columns[2][orderable]': 'true',
            # 'columns[2][search][value]': '',
            # 'columns[2][search][regex]': 'false',
            # 'columns[3][data]': 'PartyName',
            # 'columns[3][name]': '',
            # 'columns[3][searchable]': 'true',
            # 'columns[3][orderable]': 'true',
            # 'columns[3][search][value]': '',
            # 'columns[3][search][regex]': 'false',
            # 'columns[4][data]': 'Income',
            # 'columns[4][name]': '',
            # 'columns[4][searchable]': 'true',
            # 'columns[4][orderable]': 'true',
            # 'columns[4][search][value]': '',
            # 'columns[4][search][regex]': 'false',
            # 'columns[5][data]': 'Expense',
            # 'columns[5][name]': '',
            # 'columns[5][searchable]': 'true',
            # 'columns[5][orderable]': 'true',
            # 'columns[5][search][value]': '',
            # 'columns[5][search][regex]': 'false',
            # 'columns[6][data]': 'CashBalance',
            # 'columns[6][name]': '',
            # 'columns[6][searchable]': 'true',
            # 'columns[6][orderable]': 'true',
            # 'columns[6][search][value]': '',
            # 'columns[6][search][regex]': 'false',
            # 'columns[7][data]': 'IESupport',
            # 'columns[7][name]': '',
            # 'columns[7][searchable]': 'true',
            # 'columns[7][orderable]': 'true',
            # 'columns[7][search][value]': '',
            # 'columns[7][search][regex]': 'false',
            # 'columns[8][data]': 'IEOpposition',
            # 'columns[8][name]': '',
            # 'columns[8][searchable]': 'true',
            # 'columns[8][orderable]': 'true',
            # 'columns[8][search][value]': '',
            # 'columns[8][search][regex]': 'false',
            'order[0][column]': '0',
            'order[0][dir]': 'desc',
            'start': '0',
            'length': str(max_records),
            'search[value]': name,
            'search[regex]': 'true',
        }
        response = requests.post('https://seethemoney.az.gov/Reporting/GetNEWTableData/', params=params, cookies=self.cookies, headers=self.headers, data=data)
        return response
    
    
    def pac_list(self, name, max_records):
        params = [
            ('Page', '2'),
            ('startYear', '2002'),
            ('endYear', '2022'),
            ('JurisdictionId', '0'),
            ('TablePage', '1'),
            ('TableLength', '10'),
            ('IsLessActive', 'false'),
            ('ShowOfficeHolder', 'false'),
            ('ChartName', '2'),
            ('IsLessActive', 'false'),
            ('ShowOfficeHolder', 'false'),
        ]

        data = {
            'draw': '6',
            'columns[0][data]': 'EntityLastName',
            'columns[0][name]': '',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'true',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'Income',
            'columns[1][name]': '',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'Expense',
            'columns[2][name]': '',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'CashBalance',
            'columns[3][name]': '',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'IESupport',
            'columns[4][name]': '',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': 'IEOpposition',
            'columns[5][name]': '',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'columns[6][data]': 'BMEFor',
            'columns[6][name]': '',
            'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'true',
            'columns[6][search][value]': '',
            'columns[6][search][regex]': 'false',
            'columns[7][data]': 'BMEAgainst',
            'columns[7][name]': '',
            'columns[7][searchable]': 'true',
            'columns[7][orderable]': 'true',
            'columns[7][search][value]': '',
            'columns[7][search][regex]': 'false',
            'order[0][column]': '0',
            'order[0][dir]': 'asc',
            'start': '0',
            'length': str(max_records),
            'search[value]': name,
            'search[regex]': 'true',
        }
        response = requests.post('https://seethemoney.az.gov/Reporting/GetNEWTableData/', params=params, cookies=self.cookies, headers=self.headers, data=data)
        return response

    def campaign_transaction(self, transact_id):
        params = {
            'transactionId': transact_id,
        }
        response = requests.post('https://seethemoney.az.gov/Reporting/GetNEWTransactionDetails/', params=params, cookies=self.cookies, headers=self.headers)
        return response

    def campaign_income(self, campaign_id, max_records):
        params = {
            'Page': '20',
            'startYear': '2002',
            'endYear': '2022',
            'JurisdictionId': '0',
            'TablePage': '1',
            'TableLength': '10',
            'Name': f'1~{campaign_id}',
            'entityId': f'{campaign_id}',
            'ChartName': '20',
            'IsLessActive': 'false',
            'ShowOfficeHolder': 'false',
        }
        data = {
            'draw': '2',
            'columns[0][data]': '',
            'columns[0][name]': '',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'false',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'TransactionId',
            'columns[1][name]': '',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'TransactionDate',
            'columns[2][name]': '',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'TransactionLastName',
            'columns[3][name]': '',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'Amount',
            'columns[4][name]': '',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': 'TransactionType',
            'columns[5][name]': '',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'order[0][column]': '2',
            'order[0][dir]': 'desc',
            'start': '0',
            'length': str(max_records),
            'search[value]': 'Contribution from Individuals',
            'search[regex]': 'false',
        }
        response = requests.post('https://seethemoney.az.gov/Reporting/GetNEWDetailedTableData', params=params, cookies=self.cookies, headers=self.headers, data=data)
        return response
    
    def pac_income(self, campaign_id, max_records):
        params = {
            'Page': '30',
            'startYear': '2002',
            'endYear': '2022',
            'JurisdictionId': '0',
            'TablePage': '1',
            'TableLength': '10',
            'Name': f'2~{campaign_id}',
            'entityId': f'{campaign_id}',
            'ChartName': '30',
            'IsLessActive': 'false',
            'ShowOfficeHolder': 'false',
        }
        data = {
            'draw': '2',
            'columns[0][data]': '',
            'columns[0][name]': '',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'false',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'TransactionId',
            'columns[1][name]': '',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'TransactionDate',
            'columns[2][name]': '',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'TransactionLastName',
            'columns[3][name]': '',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'Amount',
            'columns[4][name]': '',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': 'TransactionType',
            'columns[5][name]': '',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'order[0][column]': '2',
            'order[0][dir]': 'desc',
            'start': '0',
            'length': str(max_records),
            'search[value]': 'Contribution from Individuals',
            'search[regex]': 'false',
        }
        response = requests.post('https://seethemoney.az.gov/Reporting/GetNEWDetailedTableData', params=params, cookies=self.cookies, headers=self.headers, data=data)
        return response
    
    
    def candidate_ind_contributions(self, name, num_records):
        # %%
        candidate_campaigns = json.loads(self.campaign_list(name,num_records).text)
        pac_campaigns = json.loads(self.pac_list(name,num_records).text)
        campaigns_df = pd.DataFrame(candidate_campaigns['data'])# pd.read_json(data)
        pac_df = pd.DataFrame(pac_campaigns['data'])# pd.read_json(data)
        final_data_df = pd.DataFrame()
        for index, campaign in campaigns_df.iterrows():
            income_data = json.loads((self.campaign_income(campaign['EntityID'],num_records)).text)
            income_df = pd.DataFrame(income_data['data'])# pd.read_json(data)
            if not income_df.empty:
                transactions_details = []
                for transact in income_data['data']:
                    # print(campaign['CommitteeName'], transact['TransactionId'], transact['TransactionLastName'] )
                    transact_data = json.loads((self.campaign_transaction(transact['TransactionId'])).text)
                    transactions_details.append(transact_data)
                transactions_details_df = pd.DataFrame(transactions_details)
                campaign_transactions_df = pd.merge(income_df,transactions_details_df,left_on='TransactionId', right_on='TransactionID',how='left',suffixes=(None,'_Detail'))
                final_data_df = pd.concat([final_data_df,campaign_transactions_df], ignore_index=True)
        for index, campaign in pac_df.iterrows():
            income_data = json.loads((self.pac_income(campaign['EntityID'],num_records)).text)
            income_df = pd.DataFrame(income_data['data'])# pd.read_json(data)
            if not income_df.empty:
                transactions_details = []
                for transact in income_data['data']:
                    transact_data = json.loads((self.campaign_transaction(transact['TransactionId'])).text)
                    transactions_details.append(transact_data)
                transactions_details_df = pd.DataFrame(transactions_details)
                campaign_transactions_df = pd.merge(income_df,transactions_details_df,left_on='TransactionId', right_on='TransactionID',how='left',suffixes=(None,'_Detail'))
                final_data_df = pd.concat([final_data_df,campaign_transactions_df], ignore_index=True)
        if not final_data_df.empty:
            for column in ['TransactionDate', 'TransactionDateYearMonth', 'TransactionDate_Detail']:
                final_data_df[column] = final_data_df[column].apply(lambda x: convert_unix_date(x))
        # %%
        return final_data_df, campaigns_df
    
    def individual_history(self, entityId, num_records, min_year, max_year):
        params = {
            'Page': '80',
            'startYear': str(min_year),
            'endYear': str(max_year),
            'JurisdictionId': '0',
            'TablePage': '1',
            'TableLength': '10',
            'Name': f'7~{entityId}',
            'entityId': f'{entityId}',
            'ChartName': '80',
            'IsLessActive': 'false',
            'ShowOfficeHolder': 'false',
        }

        data = {
            'draw': '2',
            'columns[0][data]': '',
            'columns[0][name]': '',
            'columns[0][searchable]': 'true',
            'columns[0][orderable]': 'false',
            'columns[0][search][value]': '',
            'columns[0][search][regex]': 'false',
            'columns[1][data]': 'TransactionId',
            'columns[1][name]': '',
            'columns[1][searchable]': 'true',
            'columns[1][orderable]': 'true',
            'columns[1][search][value]': '',
            'columns[1][search][regex]': 'false',
            'columns[2][data]': 'TransactionDate',
            'columns[2][name]': '',
            'columns[2][searchable]': 'true',
            'columns[2][orderable]': 'true',
            'columns[2][search][value]': '',
            'columns[2][search][regex]': 'false',
            'columns[3][data]': 'CommitteeName',
            'columns[3][name]': '',
            'columns[3][searchable]': 'true',
            'columns[3][orderable]': 'true',
            'columns[3][search][value]': '',
            'columns[3][search][regex]': 'false',
            'columns[4][data]': 'Amount',
            'columns[4][name]': '',
            'columns[4][searchable]': 'true',
            'columns[4][orderable]': 'true',
            'columns[4][search][value]': '',
            'columns[4][search][regex]': 'false',
            'columns[5][data]': 'TransactionType',
            'columns[5][name]': '',
            'columns[5][searchable]': 'true',
            'columns[5][orderable]': 'true',
            'columns[5][search][value]': '',
            'columns[5][search][regex]': 'false',
            'columns[6][data]': 'ReceivedFromOrPaidTo',
            'columns[6][name]': '',
            'columns[6][searchable]': 'true',
            'columns[6][orderable]': 'true',
            'columns[6][search][value]': '',
            'columns[6][search][regex]': 'false',
            'order[0][column]': '2',
            'order[0][dir]': 'desc',
            'start': '0',
            'length': str(num_records),
            'search[value]': '',
            'search[regex]': 'false',
        }

        response = requests.post('https://seethemoney.az.gov/Reporting/GetNEWDetailedTableData/', params=params, cookies=self.cookies, headers=self.headers, data=data)
        return response
#%%
def main(cookie, userid):
    # %%
    test = seethemoneyAZ(cookie,userid)
    campaign_ind_contributions_df, campaign_list_df = test.candidate_ind_contributions('jerry lewis',9999999)
    campaign_ind_contributions_df.to_csv('contrib.csv')
    campaign_list_df.to_csv('campaign_list.csv')
    
    # Build a list of all people who have donated money to candidate
    report_out_df = campaign_ind_contributions_df.sort_values(by='TransactionId',ascending=False).groupby(by=['TransactionNameGroupId','TransactionLastName']).agg({'Address':'first','TransactionOccupation':'first','TransactionEmployer':'first','Amount_Detail':'sum'}).sort_values(by='Amount_Detail',ascending=False).copy()

    # Section For each individual in that list find their historical donations
    historical_donations_df = pd.DataFrame()
    # Iterate over each row of the list of donors
    for index, row in report_out_df.iterrows():
        # Using donor ID, pull all of their donations from 2020 on
        try:
            individual_donations = json.loads(test.individual_history(row.name[0], 9999999, 2020, 2022).text)
            individual_donations_df = pd.DataFrame(individual_donations['data'])
            # If there is data then add it to an overarching history
            if not individual_donations_df.empty:
                historical_donations_df = pd.concat([historical_donations_df,individual_donations_df], ignore_index=True)
        except:
            print(row.name[0])
    # Convert the date column to Pandas readable date formats
    for column in ['TransactionDate', 'TransactionDateYearMonth']:
            historical_donations_df[column] = historical_donations_df[column].apply(lambda x: convert_unix_date(x))
    # Pull out the year of each donation for later aggregation
    historical_donations_df['YEAR'] = historical_donations_df['TransactionDate'].dt.year
    historical_donations_df.to_csv('historical.csv')
    
    # Aggregate by the donator, year and donation target and sum the amount of donations
    other_contributions_df = (historical_donations_df.fillna('')).groupby(by=['TransactionNameGroupId','TransactionLastName','YEAR','CommitteeName']).agg({'Amount':sum})
    other_contributions_df.reset_index(inplace=True)
    
    # Create a text field that shows the amount and donation target for each record
    other_contributions_df['Donor History'] = '$' + other_contributions_df['Amount'].astype(str) + ' - ' + other_contributions_df['CommitteeName']
    # Sort by Donator, Then year descending, then amount descending
    other_contributions_df.sort_values(by=['TransactionLastName','YEAR','Amount'], ascending=[True,False,False],inplace=True)

    # Aggregate by the Donator, year and then make an array of all the unique values of Donation History
    compressed_df = other_contributions_df.groupby(by=['TransactionNameGroupId','YEAR']).agg({'Donor History':pd.Series.unique})
    compressed_df.reset_index(inplace=True)
    compressed_df['Donor History'] = compressed_df['Donor History'].apply(lambda x: '\n'.join(list(x)))
    compressed_df.sort_values(by=['TransactionNameGroupId','YEAR'],ascending=[True,False],inplace=True)

    # Aggregate by the Donator then make an array of all the unique values of Donation History
    super_compressed_df = (compressed_df.groupby(by=['TransactionNameGroupId','YEAR']).agg({'Donor History':pd.Series.unique})).copy()
    super_compressed_df.reset_index(inplace=True)
    # Combine the list of Donor History into a single string
    super_compressed_df['Donations'] = (super_compressed_df['Donor History'].apply(lambda x: '\n'.join(list(reversed(x)))))
    # Prepend the year onto this string
    super_compressed_df['History'] = '*-' + (super_compressed_df['YEAR'].astype(str) + '-*' + '\n' + super_compressed_df['Donations'])
    # Sort the data according to how we want it aggregated
    super_compressed_df.sort_values(by=['TransactionNameGroupId','YEAR'],ascending=[True, False],inplace=True)

    # Aggregate by Donor generating a list of the 'History' values for each years
    history_df = super_compressed_df.groupby(by=['TransactionNameGroupId']).agg({'History':pd.Series.unique})
    
    history_df['History'] = (history_df['History'].apply(lambda x: '\n'.join(list(x))))
    
    # Combine the list of Donor History into a single string
    final_df = (pd.merge(report_out_df.reset_index(), history_df.reset_index(),left_on='TransactionNameGroupId', right_on='TransactionNameGroupId', how='left'))
    final_df.to_excel('test.xlsx')
    
    
    # %%
    pass

if __name__ == '__main__':
    main('__cf_bm=Inu3gBrqoPokS8xTeE0ezQx5LT2Qw.M8VgqGBjKzN.I-1651189506-0-ATLBwFmpn/8Vrhtk+6NZskuADOg4OsySoNylEUr6OSIZCZ8tbjLmz8U3MaEEo5n5yEeskJNSPIlAhkS4nXfiHmg=','46f1bfcd-e19b-43ec-8742-992cfb3f76cb')