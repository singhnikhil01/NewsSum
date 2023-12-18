from TextSummerizer.components.data_transformation import DataTransformation
from TextSummerizer.config.configuration  import ConfigurationManager
from TextSummerizer.logging import logger 


class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_transformation_config = config.data_transformation_config()
            data_transformation = DataTransformation(config=data_transformation_config)
            data_transformation.convert()
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            raise