import os,sys
from db.mysql import create_dbengine
from db.write import df_to_sql
from fetch.StockIndex import get_index_table
from util.indCode import get_indCode,indCode_to_tickers
from util.query_data import get_df_bySec,get_df_byTicker

sys.path.insert(0, os.path.abspath(".."))

def update_all(index_name,intraday,type='compact'):
    '''
    update all
    full: all data
    compact: today only
    '''
    data = get_index_table(index_name) # All tickers in DF format
    if (type=='compact' and intraday=='none'):
        df_dic = get_df_byTicker(data,size='compact',today_only=True,sleep_timer=15,intraday='none')
    elif (type=='full' and intraday=='none'):
        df_dic = get_df_byTicker(data,size='full',today_only=False,sleep_timer=15,intraday='none')
    elif (type=='compact' and intraday !='none'):
        df_dic = get_df_byTicker(data,size='compact',today_only=True,sleep_timer=15,intraday='30min')
    elif (type=='full' and intraday !='none'):
        df_dic = get_df_byTicker(data,size='full',today_only=False,sleep_timer=15,intraday='30min')
    else:
        pass


def update_by_industry(index_name,indCode,intraday,type='full'):
    '''
    update by industry code;
    full: all data
    compact: today only
    '''
    data = get_index_table(index_name)
    df = indCode_to_tickers(data,indCode)  # ticers in that Industry in DF format
    if (type=='compact' and intraday=='none'):
        df_dic = get_df_bySec(df,size='compact',today_only=True,sleep_timer=15,intraday='none')
    elif (type=='full' and intraday=='none'):
        df_dic = get_df_bySec(df,size='full',today_only=False,sleep_timer=15,intraday='none')
    elif (type=='compact' and intraday!='none'):
        df_dic = get_df_bySec(df,size='compact',today_only=True,sleep_timer=15,intraday='30min')
    elif (type=='full' and intraday!='none'):
        df_dic = get_df_bySec(df,size='full',today_only=False,sleep_timer=15,intraday='30min')
    else:
        pass
