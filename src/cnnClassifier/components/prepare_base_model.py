from cnnClassifier.entity.config_entity import PrepareBaseModelReturnType
import tensorflow as tf 
from pathlib import Path






class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelReturnType):
        self.config = config


    # Creating Simple layerS of VGG-16 as base model 
    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,   # input shape 
            weights=self.config.params_weights,    # weights shoud be of imagenet
            include_top=self.config.params_include_top   # we are adding custo, layers in the end 
        )

        self.save_model(path=self.config.base_model_path, model=self.model)    # save the model in base model 


    # preparing Full model with Custom Layers 
    # if Freeze_all=True then we are freesing all the layers and weight it not be trained (as already Trained On Imagenet data set ) 
    # we cal also use Freeze_till in which we can freeze as number of layers as we want to  
    @staticmethod
    def _prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):



        #Freezing the model layers All 
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        # Freezing number of layers         
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False




        #Adding Flatten Layer and before flatten we need model output(All model layers )
        flatten_in = tf.keras.layers.Flatten()(model.output)


        # Adding OutPut layer and before that flatten layer is attached 
        prediction = tf.keras.layers.Dense(
            units=classes,
            activation="softmax"
        )(flatten_in)





        # Building A Full Model 

        full_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=prediction
        )



        # Compiling A model 

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )




       #  returning Summary Of model

        full_model.summary()
        return full_model
    




    
    # This Function calls Prepare full model function and and save full model in updated model file 
    def update_base_model(self):
        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
