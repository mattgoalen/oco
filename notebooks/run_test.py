import pytest
import os
import sys
sys.path.append('..')
sys.path.append('/home/mg13/Projects/oco')
os.environ["ABSCO_PATH"] = "/home/mg13/Projects/ABSCO" # "/Users/smyth/absco/v5.0.0"
from refractor.framework.factory import process_config
from refractor import framework as rf
from config import retrieval_config
from pprint import pprint

def test_load_example_config():
    data_dir = os.path.realpath('/home/mg13/Projects/oco/test/in')
    l1b_file = os.path.join(data_dir, "oco2_L1bScND_16094a_170711_B7302r_171102090317-selected_ids.h5")
    met_file = os.path.join(data_dir, "oco2_L2MetND_16094a_170711_B8000r_171017214714-selected_ids.h5")

    sounding_id = "2017071110541471"
    config_def = retrieval_config.retrieval_config_definition(l1b_file, met_file, sounding_id)
    config_inst = process_config(config_def)
    pprint(config_inst, indent=2)
    fm = config_inst.forward_model
    atm = config_inst.atmosphere
    sv = config_inst.retrieval.state_vector
    solver = config_inst.retrieval.solver
    
test_load_example_config()
