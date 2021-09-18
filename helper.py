def calculate_len_and_time(df,t_seq,cols_1=None,cols_2=None):
    '''
    Calculates length of possession sequence and time elapsed for each sequence
    
    Inputs:
    df: dataframe containing the events
    t_seq: list of tuples containing indices of sequence start and end
    cols_1: list of column names
    cols_2: list of column names
    
    Output:
    Displays: dataframe (start_index,team,start_xy,end_xy,Home,length,time)
    '''
    import pandas as pd
    df_sum = pd.DataFrame()

    if not cols_1 :
        cols_1 = ['teamId','x','y','endX','endY']
    if not cols_2:
        cols_2 = ['x','y']

    df_sum = df.loc[[x[0] for x in t_seq]][cols_1]   
    df_sum.loc[:,['seq_endX','seq_endY']] = df.loc[[x[1] for x in t_seq]][cols_2].values

    display(df_sum)

def sequences(df,col_name,col_name2,teamId,value):
    '''
    Input:
    df - dataframe to extract sequence
    col_name - column for applying condition 
    col_name2 - column for identifying outcomes ie True or False
    teamId - team which is currently in possession
    value - check for value
    
    Output:
    returns list of start indices 
    '''
    

    # flag the row at the start of the pattern
    seq =    ~ (df[col_name].eq(teamId)) & \
    ~ (df[col_name].shift(-1).eq(teamId)) & \
    ~ (df[col_name].shift(-2).eq(teamId))
    
    seq2 = (df[col_name2].eq(value)) & \
     (df[col_name2].shift(-1).eq(value)) & \
     (df[col_name2].shift(-2).eq(value))
    
    seq = seq & seq2
    try:
        return seq[seq].index.values[0]
    except:
        return seq.index.values[-1]

def calc_seq(df,throw_in_idx):
    '''
    Input:
    df - input dataframe
    throw_in_idx - list of start indices

    Output:
    Returns list of tuples containing sequence start end indices
    '''
    from tqdm.notebook import tqdm
    t_seq = []
    for i,s_idx in enumerate(tqdm(throw_in_idx[:-1])):
        
        e_idx = sequences(df.loc[s_idx:throw_in_idx[i+1]],
                        'teamId','outcomeType_value',
                        df.loc[s_idx]['teamId'],
                        'Successful')
        t_seq.append((s_idx,e_idx))

    t_seq.append((throw_in_idx[-1],sequences(df.loc[throw_in_idx[-1]:],
                        'teamId','outcomeType_value',
                        df.loc[throw_in_idx[-1]]['teamId'],
                        'Successful')))
    return t_seq