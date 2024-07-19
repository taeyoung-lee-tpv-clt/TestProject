import os, yaml

environment = os.environ.get("RUN_ENVIRONMENT")
home_direcotry = os.environ.get("PWD")

if environment == None:
    environment = "local"

# Get common setting
config_common = {}
with open(file=f"{home_direcotry}/config/yaml/{environment}/common.yaml", mode="r") as file:
    config_common = yaml.load(stream=file, Loader=yaml.FullLoader)

