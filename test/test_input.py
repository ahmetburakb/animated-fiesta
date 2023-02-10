import pandas as pd

def test_size():
    df = pd.read_csv("../messy_input.csv", index_col=0)
    assert df.shape[0] == 225
    assert df.shape[1] == 31

def test_world_pop():

    df = pd.read_csv("../messy_input.csv", index_col=0)

    def recode_population(population):
        result = ""
        try:
            result = float(population)
        except:
            result = "NaN"
        return result

    df['2010'] = df['2010'].apply(recode_population)
    df['2010'] = df['2010'].astype(float)
    world_pop_2010 = df['2010'].sum()
    
    assert int(world_pop_2010) == 7065
