import pandas as pd
import string
import wget


def get_files():
    a_to_z = string.ascii_lowercase[:]
    for letter in a_to_z:
        url = f'https://public.wiwdata.com/engineering-challenge/data/{letter}.csv'
        wget.download(url, f'When I Work/Data/{letter}.csv')


def combine_a_to_z():
    a_to_z = string.ascii_lowercase[:]
    all_letters = pd.DataFrame()
    for letter in a_to_z:
        letter_df = pd.read_csv(f'When I Work/Data/{letter}.csv')
        all_letters = pd.concat([all_letters, letter_df])
    return all_letters


def sum_of_length(df):
    df = df[['user_id', 'path', 'length']]
    df = df.groupby(['user_id', 'path']).sum('length').reset_index()
    df = df.pivot(index='user_id', columns='path')
    return df


def main():
    get_files()
    all_letters = combine_a_to_z()
    output = sum_of_length(all_letters)
    output.to_csv('When I Work/output.csv')



