
from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import *
from src.cnnClassifier.entity.config_entity import DataIngestionConfig,ModelTrainingConfiguration,PreparebaseConfig,EvaluationConfig

class ConfigManager():
    def __init__(self, 
                 config_path= CONFIG_PATH,
                 params_path = PARAMS_PATH):
        
        self.config = read_yaml(CONFIG_PATH)
        self.params = read_yaml(params_path)
    
    
        create_directories([self.config.artifacts_root])
    
    
    def get_data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        
        return DataIngestionConfig(root_dir=Path(config.root_dir),
                                   source_URL=config.source_URL,
                                   local_data_file=config.local_data_file,
                                   unzip_dir=config.unzip_dir)
    
    def get_Prepare_base_config(self)->PreparebaseConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        Prepare_base_Config = PreparebaseConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            Updated_model_path= config.updated_base_model_path,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES
        )
        
        
        
        return Prepare_base_Config
    
    
    def get_training_config(self)->ModelTrainingConfiguration:
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Data_GKN")
        create_directories([training.root_dir])
        
        training_config = ModelTrainingConfiguration(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        
        )
        
        return training_config
    
    
    def get_evaluation_config(self) -> EvaluationConfig:
        eval_config = EvaluationConfig(
            path_of_model="artifacts/training/model.h5",
            training_data="artifacts/data_ingestion/Data_GKN",
            mlflow_uri="https://dagshub.com/jayrajrajput2107/Defect-Identification-for-steel-plant-.mlflow",
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        return eval_config