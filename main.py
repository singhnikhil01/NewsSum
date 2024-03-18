from TextSummerizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummerizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummerizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummerizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from TextSummerizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from TextSummerizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try: 
    logger.info(f">>>> stage {STAGE_NAME} started")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===========x")

except Exception as e : 
    logger.exception(e)
    raise e 

STAGE_NAME = "Data validation stage"
try: 
    logger.info(f">>>> stage {STAGE_NAME} started")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===========x")
except Exception as e : 
    logger.exception(e)
    raise e 


STAGE_NAME = "Data Transformation stage"
try: 
    logger.info(f">>>> stage {STAGE_NAME} started")
    data_transoformation = DataTransformationTrainingPipeline()
    data_transoformation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===========x")

except Exception as e : 
    logger.exception(e)
    raise e 



STAGE_NAME = "Model Trainer stage"

try: 
    logger.info(f">>>> stage {STAGE_NAME} started")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===========x")

except Exception as e : 
    logger.exception(e)
    raise e 

STAGE_NAME = "Model Evaluation stage"
try: 
    logger.info(f">>>> stage {STAGE_NAME} started")
    model_trainer =  ModelEvaluationTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\n x===========x")

except Exception as e : 
    logger.exception(e)
    raise e 