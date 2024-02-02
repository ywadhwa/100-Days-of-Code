import pandas as pd

states = pd.read_csv("50_states.csv")
df_states = pd.DataFrame(states)

#for state in df_states["state"]:
#    print(state)

print(df_states['state'].values)