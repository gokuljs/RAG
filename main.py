from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine

population_path = os.path.join("data", "population.csv")
population_df = pd.read_csv(population_path)
population_query_engine = PandasQueryEngine(df=population_df, verbose=2)

load_dotenv()
