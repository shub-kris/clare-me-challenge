FROM nvcr.io/nvidia/pytorch:23.10-py3

WORKDIR /code

# Copy the requirements file
COPY requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app code
COPY ./app /code/app

# Download the model weights
RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
RUN apt-get install git-lfs
RUN git clone https://huggingface.co/shub-kris/claire-text-classification-model/ /code/model-weights

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
