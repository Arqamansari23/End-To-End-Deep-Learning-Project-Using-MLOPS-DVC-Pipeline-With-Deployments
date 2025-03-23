# tHIS file is responsible for c Build all PAths necessary for stages. Reading from Config.yaml file and create direcoties Paths 







from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionReturnType,PrepareBaseModelReturnType









# Configuration Manager For Data Ingestion 
class DataIngestionConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    # return all the data ingestion related configuration 
    def get_data_ingestion_config(self) -> DataIngestionReturnType:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionReturnType(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    






# Configuration Manager For Base Model   
class BAseModelConfigurationManager:
    def __init__(
        self, 
        config_filepath = CONFIG_FILE_PATH,  # Taking path of config.yaml 
        params_filepath = PARAMS_FILE_PATH):  # Taking PAth of Params.yaml 
        self.config = read_yaml(config_filepath)   # Reading Config File 
        self.params = read_yaml(params_filepath)   # Reading params file 
        create_directories([self.config.artifacts_root])   # creating root directory for base model 


    def get_prepare_base_model_config(self) -> PrepareBaseModelReturnType:   # Get All the configuration which is passed into next Function or classs to start building base model 
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelReturnType(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )

        return prepare_base_model_config
      