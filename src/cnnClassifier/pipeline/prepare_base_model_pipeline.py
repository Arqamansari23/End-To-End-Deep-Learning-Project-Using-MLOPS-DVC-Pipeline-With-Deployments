
from cnnClassifier.config.configuration import BAseModelConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel 
from cnnClassifier.logger import logger


STAGE_NAME=" Base Model Preparation "


class Base_Model_Pipeline:
    def __init__(self) :
        pass

    def main(self):
        try:
            config=BAseModelConfigurationManager()
            get_config=config.get_prepare_base_model_config()
            prepare_base_model=PrepareBaseModel(get_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

        except Exception as e:
              raise e

    


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = Base_Model_Pipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e