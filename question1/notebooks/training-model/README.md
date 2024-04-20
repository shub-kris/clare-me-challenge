## Answers to the questions

### 1. Why Did You Choose distilbert-base-uncased Model?
DistilBERT is a transformers model, smaller and faster than BERT, which was pretrained on the same corpus in a self-supervised fashion, using the BERT base model as a teacher. More information can be found [here](https://huggingface.co/distilbert/distilbert-base-uncased).

As the [synthetic dataset](https://huggingface.co/datasets/shub-kris/claire-dataset) is quite simple, so it doesn't require a complex model with a large number of parameters. DistilBERT is a good choice for this task. It is also faster and requires less memory to train.

DistilBERT has shown to be a good model for text classification tasks, and it is widely used in the industry. It has achieved good results on various benchmarks like GLUE, SQuAD and others.

### 2. How did you split the dataset?
The dataset was split into training and validation sets using the `train_test_split` function from the `sklearn` library. The dataset was split into 80% training and 20% validation. 

It is an important step to split the dataset into training and validation sets to evaluate the model's performance. The training set is used to train the model, and the validation set is used to evaluate the model's performance. 

### 3. Choose the Right Metric to Measure the Model's Performance

The metric used to measure the model's performance are the following:
- Accuracy: It is the ratio of correctly predicted instances to the total instances.
- Precision: It is the ratio of correctly predicted positive observations to the total predicted positive observations.
- Recall: It is the ratio of correctly predicted positive observations to the all observations in actual class.

All these metrics are important to evaluate the model's performance. Accuracy gives an overall idea of the model's performance, while precision and recall give insights into the model's performance on positive and negative classes.

The performance was evaluated on the validation set using these metrics.

### 4. What assumptions did you make or What could I have done differently?
- I assumed that I just have access to the synthetic dataset. In real life, I would have access to more complex and real-world datasets. I would have to preprocess the data, clean it, and handle missing values. I would also have to deal with imbalanced datasets, outliers, and other issues.

- As the dataset was very simple, a simple model like DistilBERT was used. In real life, I would have to experiment with different models, hyperparameters, and architectures to find the best model for the task. However, I would still start with DistilBERT as it is a good model for text classification tasks. If the dataset is more complex, I would use a more complex model like BERT or RoBERTa. Leveraging LLMs like GPT-3 or others would be an overkill for this task and the computational resources required would be much higher. It might happen that the big LLMs might give some percentage points of improvement but the cost of training and inference would be much higher. It is always a trade-off between the model's performance and the resources required. If the context_size is large, then LLMs might be a good choice.

- I didn't follow any MLOps practices like building pipeline for training model, logging of metrics, monitoring, and versioning. In real life, I would use tools like SageMaker Pipelines or Vertex AI Pipelines to build end-to-end ML pipelines. I would also use tools like WeightsandBiases or TensorBoard to log metrics, and monitor the model's performance. I would also version the datasets, models, and other artifacts.

- I would also document the code, write tests, and follow best practices for writing clean and maintainable code. I would also use tools like flake8, black, and isort to format the code and ensure consistency.

- I would also do better dependency management, use virtual environments, and containerize the training using Docker. I would also use CI/CD tools like GitHub Actions or Jenkins to automate the testing and deployment process. I would also use tools like Terraform or CloudFormation to automate the infrastructure provisioning.

- As the dataset was small and very repetitive, I am sure that the model is overfitting. A better model would have come out if the dataset was more diverse and complex. 

